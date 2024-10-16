# Rock, Paper, Scissors, by Kelston Spaulding, v3.0

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Test Player"
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
def playerName(): # Function Signature -- name of function 
    playerName = input("Please type your name and press enter.\n")
    print(f"Hello {playerName}!.\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

    # .lower() can turn ALL input into lowercase.
    # .upper() can turn ALL input into uppercase.

    if isCorrect == "yes":
        print(f"ok {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Please type your name and press enter.\n")
    
# calling the function
playerName()

# THE RULES using MULTI-LINE STRINGS
print(f"""
Welcome {playerName} to the Rock, Paper, Scissors Robot!
It's Time To Play Rock, Paper, Scissors!
    
You will play against the CPU. The first person to score 5 points wins.
You will select from ROCK, PAPER, SCISSORS.
The CPU will select ROCK, PAPER, or SCISSORS at random.
      
1) ROCK BEATS SCISSORS
2) SCISSORS BEATS PAPER
3) PAPER BEATS ROCKS
""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of double-quotes is just ignored.
If you need to write large comments, it's easier to use multi-line strings than
putting a # in frontof 15 different times
"""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    
    # let cpu select choice at random.
    cpuChoice = random.randint(0, 2) # randomly select 0, 1, or 2.
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice ="scissors"
    elif cpuChoice ==2:
        cpuChoice = "paper"
    else:
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()
    #print(f"CPU Choice: {cpuChoice}")
        
    # compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    elif playerChoice == "rock" and cpuChoice == "scissors":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "rock" and cpuChoice == "rock":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw.\n")
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuChoice += 1
    elif playerChoice == "scissors" and cpuChoice == "paper":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW
        print(f"The chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw.\n")
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw.\n")
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    

    # award point to winner and output results.
