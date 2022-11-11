import json
import os


def displayMessage(message:str,style:int=0):

    pointer=""

    if style is 0:
        pointer="-"

    elif style is 1:
        pointer="*"
        
    else:
        pointer=" "
    
    print(f"[{pointer}] {message}")


def getLogo():

    with open("art.txt","r",encoding="utf-8") as f:
        logo=f.read()
        f.close()

    return logo


def getConfigData():

    print("\n")
    displayMessage("Running Configuration as config file is not present. Please Enter the required details :")
    print("\n")

    data={"name":"","path":"","email":"","interval":1,"files_to_track":[]}

    data["name"]=input("Enter your Name: ")
    data["path"]=input("Enter the folder path you want to track: ")
    data["email"]=input("Enter your email id: ")

    data["interval"]=int(input("Enter the frequency of tracking (in seconds) : "))

    files_in_directory=os.listdir(data["path"])

    for index,file in enumerate(files_in_directory):
        print(f"[{index}]  {file}")

    fileIndicies=list(map(int,input("Enter Option Numbers with comma (,):").split(",")))

    for index in fileIndicies:
        data["files_to_track"].append(files_in_directory[index])

    print("\n")
    displayMessage("Configuration Complited Successfully")
    print("\n")
    
    return data


def createConfig(data:dict):

    with open("config.json","a") as f:
        json.dump(data, f)
        f.close()


def loadConfig():

    try:
        with open("config.json","r") as f:
            config=json.load(f)
            f.close()
        
        return config
    except FileNotFoundError:
        data=getConfigData()
        createConfig(data)
        return data

