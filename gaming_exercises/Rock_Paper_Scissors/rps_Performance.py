# Rock, Paper, Scissors, by Kelston Spaulding, v0.1

# MODULE IMPORTS
import random, time

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerChoice = None
numDraws = 0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("How many loops do you want?\nEnter an integer, no commas, and press ENTER.\n"))
# req is the universal abbreviation in computer programming for REQUEST. reqs = REQUESTS
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq:
    
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

    # let PLAYER select choice at random.
    playerChoice = random.randint(0, 2) # randomly select 0, 1, or 2.
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice ="scissors"
    elif playerChoice == 2:
        playerChoice = "paper"
    else:
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit() 

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
        numDraws += 1
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
        numDraws += 1
        # CPU WINS
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw.\n")
        numDraws += 1
        # CPU WINS
    print(f"Your Final Score: {playerScore}CPU Final Score: {cpuScore}.\n ")
    if playerScore > cpuScore:
        print(f"Congratulations. a winner is you!\n")
    elif cpuScore > playerScore:
        print(f"The CPU wins. You are a dissapointment to all.\n")
    else:
        print("Unable to determine a winner.\nPlease restart.\n")
        exit()
    loopCount +=1

    # award point to winner and output results.
