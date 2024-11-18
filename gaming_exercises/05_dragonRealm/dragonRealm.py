# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime 

# SAVING THE DATA TO A FILE
# STEP 1 -- Create the file name to use.
logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
# logFileName = "dragonRealmLog.txt"
# EXAMPLE: dragonRealmLog1132AM.txt

# STEP 2 -- Create / Open the File to save the data.
saveData = open(logFileName, "x")
# FILE MODES
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE. 
# "w" CREATES FILE, IF FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS.
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now))

hasAxe = False
location = None
def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves and a tundra. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chosenLocation():
    location = ''
    while location != '1' and location != '2' and location != '3':
        print('Which path will you take? (1, 2 or, 3) location 1 is cave 1 location 2 is cave 2 location 3 is a tundra')
        location = input()
    return location

def checkPath(location):
    if location == "1":
        print('You approach the location 1')
    print('You approach the tundra...')
    time.sleep(2)
    print('It is cold...')
    time.sleep(1)
    print('you find a axe')

pickUpItem = ("You see an axe on the ground. Do you want to pick it up? Type 1 for yes or 2 for no,")
if  pickUpItem == "yes":
    hasAxe = True

if hasAxe:
    print("you one shotted the goblin")
else:
    print("The goblin squashed you like a bug")
    time.sleep(2)
    print('A goblin jumps out the ground and attacks you...')
    print()
    time.sleep(2)

    

    friendlyCave = random.randint(1, 2,)

    if location == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chosenLocation()
    checkPath(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()

hasAxe = False
pickUpItem = input("You see an axe on the ground. Do you want to pick it up? Type yes or no,")
if pickUpItem == "yes":
    hasAxe = True

if hasAxe:
    print("you one shotted the goblin")
else:
    print("The goblin squashed you like a bug")


saveData.write
saveData.close()