# Awarding Extra Lives, Kelston Spaulding, v0.0


lives = 3 # Don't start with CAPITAL LETTERS. 
score = 9000 # This should be an int(input()) line.  


# Allow the user to input the score AS AN INTEGER.

# If score is 10000 or less
    # Lose a Life
# If score is > 10000 but less than 100001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives

# Output the score and number of lives to the screen.

print(lives)
if score <= 10000:
    print("Lose 1 life.\n")
    # What code will actually change the number of lives stored in computer memory?
    lives += -1 
elif score < 100001:
    print("Gain 1 life.\n")
    # What code will actually change the number of lives stored in computer memory?
else:   
    print("Gain 2 Lives.\n")
    # What code will actually change the number of lives stored in computer memory?

print(f"Your score is {score}! You now have {lives}. ")
print(lives)