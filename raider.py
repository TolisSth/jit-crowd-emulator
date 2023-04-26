from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os 
import random 
import time

#branding
print("       _ _ _     _____       _     _ ")
print("      | (_) |   |  __ \     (_)   | |")
print("      | |_| |_  | |__) |__ _ _  __| | ___ _ __ ")
print("  _   | | | __| |  _  // _` | |/ _` |/ _ \ '__|")
print(" | |__| | | |_  | | \ \ (_| | | (_| |  __/ |   ")
print("  \____/|_|\__| |_|  \_\__,_|_|\__,_|\___|_|   ")
print("-----------------------------------------------")
print("Version 1.0 Halis Apostolos")
                                               
#configuration
numOfInstances = int(input("Number of instances: "))
meetingID = input("Meeting ID: ") 
lifespan = int(input("Lifespan of bots: "))
filePath = str(input("[OPTIONAL] Username file path: "))
fOptions = Options()
driverList = []
usernames = []

if filePath is not "": 
    file = open(filePath, "r")
    contents = file.readlines()
    for line in contents: 
        usernames.append(line.strip())
else: 
    n = int(input("How many usernames: "))
    for i in range(n):
        name = input("Username " + str(i + 1) + ": ")
        usernames.append(name)

#this settings deny permissions
print("Starting browser instance")
fOptions.set_preference("permissions.default.microphone", 2)
fOptions.set_preference("permissions.default.camera", 2)
fOptions.add_argument('--headless')
fOptions.add_argument('--disable-gpu')

for i in range(numOfInstances):
    num = random.randint(0, len(usernames) -1)
    print(usernames[num] + " is queing up to join")
#connecting to the jit.si meeting
    driver = webdriver.Firefox(options= fOptions)
    driverList.append(driver) # adding them to an object list so I can shut the instances down later
    print("Going to: " + "https://meet.jit.si/" + meetingID)
    driver.get("https://meet.jit.si/" + meetingID) 

    #name field manipulation 
    fieldName = driver.find_element(By.CLASS_NAME, "css-hh0z88-input") #that's the class name of the field for some reason 
    print("Typing name")
    fieldName.send_keys(usernames[num])
    time.sleep(1)
    fieldName.send_keys(Keys.RETURN)
    print(usernames[i] + " is joining...")

    print(usernames[i] + "Joined!")

#Freezing program 
print("Bot lifespan started")
start_time = time.time()
while time.time() - start_time < lifespan: 
    print(time.time() - start_time)
    emIn = input()
    if emIn == "q":
        break        

#shutting the instances down
for i in range(len(driverList)):
    driverList[i].close()
    print("Closed instance number " + str(i+ 1))
