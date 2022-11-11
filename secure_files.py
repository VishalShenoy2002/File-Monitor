# secure_files.py
# File Monitor which detects change in the file system

import datetime
import logging
import os
import json
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import monitor_mail
import utilities


class FileMonitor:

    def __init__(self,folderPath:str,filePaths:list=os.listdir(os.getcwd()),configFile:str="config.json"):

        # Configuring Path and Credentials
        self.folderPath=folderPath
        self.filePaths=filePaths
        self.emailID,self.password=monitor_mail.getCred()

        with open("config.json","r") as f:
            self.configData=json.load(f)
            f.close()

        # Initializing a Detector and Observer
        self.detector=FileSystemEventHandler()
        self.observer=Observer()

        # Configuring the Detector
        self.detector.on_created=self.on_created
        self.detector.on_modified=self.on_modified
        self.detector.on_deleted=self.on_deleted

        # Scheduling the process
        self.observer.schedule(self.detector, self.folderPath,recursive=True)
         

    def run(self,interval:int):

        utilities.displayMessage("Monitoring Started")
        self.observer.start()
        programStopped=False

        while programStopped==False:
            try:

                # Running an infinite loop to track changes every 5 seconds
                while True:
                    time.sleep(interval)
                    utilities.displayMessage("No Change Detected",style=2)


            except KeyboardInterrupt:

                # If user presses (Ctrl + C) Monitoring is Terminated
                utilities.displayMessage("Monitoring Terminated")
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
            monitor_mail.sendMail(self.emailID, self.password, self.configData["email"], event)

    def on_deleted(self,event):

        timestamp=datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
        print(f"{timestamp} - File {event.event_type.title()} : {event.src_path}")

        if event.event_type=="deleted" and (event.src_path in self.filePaths or event.src_path.split(os.sep)[-1] in self.filePaths):
            monitor_mail.sendMail(self.emailID, self.password, self.configData["email"], event)

    