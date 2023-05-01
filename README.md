# Jit Crowd Emulator 
## What is this? 
Jit Crowd Emulator is a python script that utilizes the Selenium browser automation suite to create an artificial crowd in your Jit.si meeting.
## What are the capabilities of this crowd
This crowd can: 
1. Join meetings (even password protected ones)
2. React using the Jit.si default reactions
3. Admit or reject other members from the lobby 
The third item in the list gives this script a moderator bot attribute. 
## How to use
The script is pretty straight forward but here is a cheatsheet if you will: 
- ```Number of instances``` refers to the populations of your artificial crowd
- ```Meeting ID``` refers to the id of your meeting e.g.: https://meet.jit.si/meeting-id
- ```Password``` referes to the passowrd
- ```Lifespan of bots``` is the amount of time that the bots will attend your meeting
- ```Do you want reactions``` this prints out a list and you are called to choose between the reactions or even choose to not have reactions at all by hitting enter. It is to be noted that during runtime you can disable reactions by pressing r and enable them again by pressing e 
- ```Username file path``` this file will contain the usernames that the bots will use, if you do not have a file tha contains usernames, you can enter some usernames manually after hitting enter. 
## Disclaimer 
This project is a crowd emulator and it is advised to be used like that and not in any malicious way. I as the creator I do not condone the use of my program as way to disrupt meetings or annoy individuals.
