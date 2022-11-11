from secure_files import FileMonitor
from utilities import *



logo=getLogo()
print(logo)

# Loading Configuration
config=loadConfig()
name=config['name']
path=config['path']
email=config['email']
displayMessage(f"Welcome {name}.\nFile Monitor will be monitering {path}\nand we will notify you on {email} if we notice any changes. ")

app=FileMonitor(path)
app.run(config['interval'])
