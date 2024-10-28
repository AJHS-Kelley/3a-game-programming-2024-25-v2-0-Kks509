# Awarding Extra Lives, Kelston Spaulding, v0.0


lives = 3 # Don't start with CAPITAL LETTERS. 
score = input("Enter score.\n").lower()
print(f"Your score is.\n")


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
    lives += -1
    # What code will actually change the number of lives stored in computer memory?
elif score < 100001:
    print("Gain 1 life.\n")
    lives += 1
    # What code will actually change the number of lives stored in computer memory?
else:
    score >= 100000
    print("Gain 2 Lives.\n")
    lives += 2
    # What code will actually change the number of lives stored in computer memory?
print(f"Your score is {score}! You now have {lives}. ")
print(lives)