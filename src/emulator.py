#Copyright (c) 2023 Apostolos Halis
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os 
import sys
import select
import random 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

def autoAdmitReject(mode): 
    #1 accept only 
    #2 reject only 
    if mode == 1: 
        buttonToClick = 'Admit'
    elif mode == 2: 
        buttonToClick = "Reject"

    try:
        admitButton = driver.find_element(By.XPATH, "//button[text()='" + buttonToClick + "']")
        time.sleep(3)
        admitButton.click()
    except:
        pass

def reactions(drivers, mode):
    #1 thumbs up
    #2 clapping 
    #3 laughing
    #4 wow
    #5 booing 
    #6 silence
    selectRandomDriver = random.randint(0, len(drivers) - 1)
    #initializing action chains 
    actions = ActionChains(drivers[selectRandomDriver])
    if mode == 1:
            #ALT + t thumbs up 
            print("Thumbs up")
            actions.key_down(Keys.ALT).perform()
            time.sleep(1)
            actions.send_keys('t')
            time.sleep(1)
            actions.key_up(Keys.ALT).perform()

    if mode == 2:
        #ALT + c clapping
        print("Clapping")
        actions.key_down(Keys.ALT).perform()
        time.sleep(1)
        actions.send_keys('c')
        time.sleep(1)
        actions.key_up(Keys.ALT).perform()

    if mode == 3:
            #ALT + l laughing 
            print("Laughing")
            actions.key_down(Keys.ALT).perform()
            time.sleep(1)
            actions.send_keys('l')
            time.sleep(1)
            actions.key_up(Keys.ALT).perform()

    if mode == 4:
            #ALT + o Wow 
            print("Wow")
            actions.key_down(Keys.ALT).perform()
            time.sleep(1)
            actions.send_keys('o')
            time.sleep(1)
            actions.key_up(Keys.ALT).perform()

    if mode == 5:
                #ALT + o booing 
                print("Boo")
                actions.key_down(Keys.ALT).perform()
                time.sleep(1)
                actions.send_keys('b')
                time.sleep(1)
                actions.key_up(Keys.ALT).perform()

    if mode == 6:
                #ALT + o silcence 
                print("Silence")
                actions.key_down(Keys.ALT).perform()
                time.sleep(1)
                actions.send_keys('s')
                time.sleep(1)
                actions.key_up(Keys.ALT).perform()

#branding
print("       _ _ _      _____                      _   ______                 _       _")
print("     | (_) |    / ____|                    | | |  ____|               | |     | |") 
print("     | |_| |_  | |     _ __ _____      ____| | | |__   _ __ ___  _   _| | __ _| |_ ___  _ __ ") 
print(" _   | | | __| | |    | '__/ _ \ \ /\ / / _` | |  __| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|") 
print("| |__| | | |_  | |____| | | (_) \ V  V / (_| | | |____| | | | | | |_| | | (_| | || (_) | |   ") 
print(" \____/|_|\__|  \_____|_|  \___/ \_/\_/ \__,_| |______|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   ") 
print("Version 1.0 Halis Apostolos")
                                              
#configuration
numOfInstances = int(input("Number of instances: "))
meetingID = input("Meeting ID: ") 
password = input("[OPTIONAL] Password: ")
lifespan = int(input("Lifespan of bots: "))
mode =input("[OPTIONAL] Do you want reactions?\n1) Thumbs up\n2) Clapping\n3) Laughing\n4) Surprized\n5) Booing\n6) Silence\n")
aOrR = True
acceptOrReject = input("Do you want the bots to automatically admit or reject users:\n1)Admit\n2)Reject\n")
if acceptOrReject == "": 
    aOrR = False
if acceptOrReject != "": 
    acceptOrReject = int(acceptOrReject)
react = True 
if mode == "":
    react = False
if mode != "":
    mode = int(mode)
filePath = str(input("[OPTIONAL] Username file path: "))
fOptions = Options()
driverList = []
usernames = []

if filePath != "": 
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
fOptions.set_preference("media.cubeb.backend", "alsa") #this mutes the browser's audio on Linux
fOptions.add_argument("--mute-audio") # this mutes this audio
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

    #Checking the "I understand the risks" checkbox
    checkbox = driver.find_element(By.CLASS_NAME, "checkmark")
    print("Clicking I understand the risks checkbox")
    checkbox.click()
    time.sleep(2)

    #name field manipulation 
    fieldName = driver.find_element(By.CLASS_NAME, "css-hh0z88-input") #that's the class name of the field for some reason 
    print("Typing name")
    fieldName.send_keys(usernames[num])
    time.sleep(1)
    fieldName.send_keys(Keys.RETURN)
    time.sleep(5)

    #password handling part
    #if there is a password field, type password and press enter
    try: 
        #checking for password field 
        passwordField = driver.find_element(By.CLASS_NAME, "css-hh0z88-input") #that's the class name of the field for some reason 
        print("Password protection found")

        if passwordField: 
            passwordField.send_keys(password)
            time.sleep(1)
            passwordField.send_keys(Keys.RETURN) 
    except: 
        print("No password protection found")
    
    print(usernames[num] + " is joining...")
    print(usernames[num] + " joined!")

print("Bot lifespan started")
start_time = int(time.time())
end_time = int(start_time + lifespan)

#main loop
while time.time() < end_time: 
    if react == True: 
        reactions(driverList, mode)
    if aOrR == True: 
        autoAdmitReject(acceptOrReject)

    #passive intake of input 
    ready, _, _ = select.select([sys.stdin], [], [], 0.1)
    if ready:
        userIn = sys.stdin.readline().strip()
        if userIn.lower() == "q":
            break
        elif userIn.lower() == "r":
            react = False
        elif userIn.lower() == "e":
            react = True

#shutting the instances down
for i in range(len(driverList)):
    driverList[i].close()
    print("Closed instance number " + str(i+ 1))
