# Loops, Kelston Spaulding, v0.0

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
