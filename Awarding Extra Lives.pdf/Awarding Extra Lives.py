# Awarding Extra Lives, Kelston Spaulding, v0.0


Lives = 3

# Allow the user to input the score AS AN INTEGER.

# If score is 10000 or less
    # Lose a Life
# If score is > 10000 but less than 100001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives

# Output the score and number of lives to the screen.


score = 10000

if score < 10000:
    print("Lose 1 life./n")
if score > 10000:
    print("Gain 1 life./n")
if score > 100000:
    print("Gain 2 Lives")