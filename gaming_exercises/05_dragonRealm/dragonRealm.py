# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves and a tundra. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print('in the tundra there is a goblin and a axe')
    print()

def choosePath():
    location = ''
    while location != '1' and location != '2' and location != '3':
        print('Which path will you take? (1, 2 or, 3)')
        cave = input()
        tundra = input()
    return tundra

def checkPath(chosenPath):
    if chosenPath == tundra:
        print('You approach the tundra')
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2,)

    if chosenPath == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = choosePath()
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