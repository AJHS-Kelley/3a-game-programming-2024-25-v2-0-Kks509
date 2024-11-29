# Flow Control Structures, Kelston Spaulding, v0.0
# Making Computer Programs Make Decisions

temperature = 89.54
color = "Cyan"
height = 8
LikesPineappleOnPizza = True

# SINGLE DECISION POINT - if statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time.
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 80:
    print("It is hot as the sun outside.\n")

if height > 7:
    print("They are too tall.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if LikesPineappleOnPizza:
    print("Yummy.\n")

# What if we want something different to happen?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color.\n")

if height == "8":
    print("You are the perfect height.\n")
else:
    print("You are not the perfect height.\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height to ride.

# When writing if-elif-else blocks check for the HIGHEST value first when using > or >=
if height >= 3:
    print("You're tall enough to ride the Tea cups!\n")
elif height >= 6:
    print("You're too tall to ride the Tea cups!\n")
else: # "oh, no, something's wrong"
    print("Error, height not detected. Do not ride.\n")


# When writing if-elif-else blocks check for the LOWEST value first when using < or <=
if height <= 3:
    print("You're not tall enough to ride the Tea cups!\n")
elif height < 6:
    print("You're too tall to ride the Tea cups!\n")
else: # "oh, no, something's wrong"
    print("Error, height not detected. Do not ride.\n")
temperature = 99
if temperature >= 100:
    print("It is too hot.\n")
elif temperature >= 50:
    print("Recess is allowed today.\n")
elif temperature > 0:
    print("Recess will be in the gym.\n")
else:
    print("Error detecting temperature.\n")
