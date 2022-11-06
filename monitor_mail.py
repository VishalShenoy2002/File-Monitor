# monitor_mail.py
# Contains function which helps the file monitor to notify you through mail

import smtplib
import pickle
from email.message import EmailMessage

def createMail(emailID,receiver_email:str,subject:str,content:str,attachment_present:bool=False):

    message=EmailMessage()
    message['Subject']=subject
    message['From']=emailID
    message['To']=receiver_email
    message.set_content(content)

    return message


def getCred():
    with open('cred.txt','rb') as f:
        data=pickle.load(f)
        emailID=data['Email']
        password=data['Password']
        f.close()
    return (emailID,password)


def sendMail(emailID:str,password:str,recvEmail:str,event):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) 
    server.login(emailID,password)
    content=f"Secure File Monitor has detected a change in your file system.\n{event.src_path} has been {event.event_type} in your absence.\n\n Please Check."
    message=createMail(emailID,recvEmail, f"ALERT : File {event.event_type.title()}", content)
    server.sendmail(emailID,recvEmail, message.as_string())
    print("Mail Sent")
    server.close()