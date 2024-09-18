# Rock, Paper, Scissors, by Kelston Spaulding, v0.1

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
playerName = input("Please type your name and press enter.\n")
print(f"Hello{playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

# .lower() can turn ALL input into lowercase.
# .upper() can turn ALL input into uppercase.

if isCorrect == "yes":
    print(f"ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type your name and press enter.\n")

# THE RULES using MULTI-LINE STRINGS
print("""
Welcome {testPlayer} to the Rock, Paper, Scissors Robot!
It's Time To Play Rock, Paper, Scissors!
    
You will play against the CPU. The first person to score 5 points wins.
You will select from ROCK, PAPER, SCISSORS.
The CPU will select ROCK, PAPER, or SCISSORS at random.
      
1) ROCK BEATS SCISSORS
2) SCISSORS BEATS PAPER
3) PAPER BEATS ROCKS
""")