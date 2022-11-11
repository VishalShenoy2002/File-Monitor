# File Monitor
File Monitoring Systems (FMSs) are used to notify sysadmins of modification, deletion, or creation of files on. the system. Commonly in system administration, File Monitoring Systems are deployed to track changes of. important system configuration files.

This application will notify the user through email when it detects any change in the files that the user has specified to track.

## Configuration
This application, when run initially will run the configuration program for you and create a config file called ```config.json```.

The configuration file i.e config.json has 5 keys
```
name,path,email,interval,files_to_track
```
**name**: This parameter is the name of the user
**path**: This parameter is the path the user wants to track
**email**: This parameter is the email of the user 
**interval**: This parameter is the time interval that the monitor will use to check 
**files_to_track**: This parameter will contain the files the user wants to track in the directory.

## How to Start Using the Monitor (Setup) ?
Now the question arises how to start using the monitor. For this first try running the following command
```
python main.py
```
If there are any *ImportErrors* try running the following command:
```
pip install requirements.txt
```

## Images
![Image of File Monitor](https://user-images.githubusercontent.com/61897464/201341764-90777194-7cb3-49a8-9d4f-603940d816cb.png)




