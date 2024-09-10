# Loops, Kelston Spaulding, v0.0
import random # import the random module for us to use.
# Generally put all your import statements at the top.

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# while < -- Used when you do not know how many loops you'll need.

# for loop is like Go Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use for a loop

# for loop Example -- Iterating a List
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachfruit in fruits:
    print(eachfruit)

# continue Keyword -- Skips the current iteration and then finishes the loop.
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachfruit in fruits:
    if eachfruit == "banana":
        continue
    print(eachfruit)

# break Keyword -- Immediately exit the loop.
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachfruit in fruits:
    if eachfruit == "banana":
        break
    print(eachfruit)

# for loops using range(). range(x) is EXCLUSIVE, it starts at 0 and ends at x - 1
for i in range(10): # range is 0 - 9
    print(i)

# Might not always want to start at zero
for i in range(10, 100): #
    print(i)

# Not want to count by 1 -- RARE
for i in range(10, 100, 5): # 10 = start, 100 - 1 = stop, 5 = # to count by
    print(i)

# Sometimes you're not done writing the loops.
for x in range(10):
    pass # tells Python this loops isn't finished, don't freak out.

# while loops -- Musical Chairs
playerScore = 0
counter = 0
while playerScore < 100: # Run as long as this is true.
    print(f"Starting: {playerScore}")
    playerScore += random.randit(1, 3)
    print(f"After: {playerScore}")
    counter += 1
print(counter)