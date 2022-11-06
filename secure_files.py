import datetime
import logging
import os
import time

from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers import Observer

import monitor_mail


class FileMonitor:
    def __init__(self,folderPath:str,filePaths:list=os.listdir(os.getcwd())):

        # Configuring Path and Credentials
        self.folderPath=folderPath
        self.filePaths=filePaths
        self.emailID,self.password=monitor_mail.getCred()

        # Initializing a Detector and Observer
        self.detector=FileSystemEventHandler()
        self.observer=Observer()

        # Configuring the Detector
        self.detector.on_created=self.on_created
        self.detector.on_modified=self.on_modified
        self.detector.on_deleted=self.on_deleted

        # Scheduling the process
        self.observer.schedule(self.detector, self.folderPath,recursive=True)
         

    def run(self):
        
        print("Monitoring Started")
        self.observer.start()
        programStopped=False

        while programStopped==False:
            try:
                while True:
                    time.sleep(5)
                    print("No Change Detected")


            except KeyboardInterrupt:
                print("Monitoring Terminated")
                programStopped=True
                self.observer.stop()
            self.observer.join()

    def on_created(self,event):

        timestamp=datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
        print(f"{timestamp} - File {event.event_type.title()} : {event.src_path}")
        
    def on_modified(self,event):

        timestamp=datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
        print(f"{timestamp} - File {event.event_type.title()} : {event.src_path}")
        
        if event.event_type=="modified" and (event.src_path in self.filePaths or event.src_path.split(os.sep)[-1] in self.filePaths):
            monitor_mail.sendMail(self.emailID, self.password, "vishal.bshenoy@gmail.com", event)

    def on_deleted(self,event):
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
        print(f"{timestamp} - File {event.event_type.title()} : {event.src_path}")

        if event.event_type=="deleted" and (event.src_path in self.filePaths or event.src_path.split(os.sep)[-1] in self.filePaths):
            monitor_mail.sendMail(self.emailID, self.password, "vishal.bshenoy@gmail.com", event)


if __name__=="__main__":
    app=FileMonitor()
    app.run()
    