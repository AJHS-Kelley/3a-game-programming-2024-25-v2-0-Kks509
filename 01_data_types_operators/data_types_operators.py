# Data Types and Operators, Kelston SPaulding, v0.0

# Fundamental Data Types
# String - str - Sequence of Letter, number, spaces, or other characters.
# Strings in Pyhthon are inside ' ' or " "
# idc if you use ' ' or " " just be consistent.

# Boolean - bool - True or False values.

# Float - float - any number value with a decimal, +/-

# Integers - int - any whole number, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABLES NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER
# cames=lCA=seVariableNames
# snake_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 7692847 # int data type

car_speed = 12.73 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playername = "Kelston Spaulding" # string data type
monsterType = "Lightning" # string data type

# ASSIGN NEW VALUES
playername = "Keon Spauld"
carspeed = -1.25

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 5.0

# Printing Data Types
newInt = 3
newFloat = 4.0
newString = "sketch mech"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

# printing Variables to Console / screen
print(playername)
print(isPurple)
print(high_score)
print(carspeed)

# printing variables and expressions to console / screen
print(high_score + 3000)
print(5 * 13)
print(high_score)

# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello {playername}. Your high score is {high_score}.\n")

# ARTHMETIC OPERATORS
myInt = 3
myFloat = 2.57
myNum = 0 

# addition
myInt = 7 + 10
myFloat = 2.0 + 3.25

myInt = myInt + 5

myNum = myInt + myFloat
# When you add an int and a float together, the answer becomes float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

# multiplication
myNumber = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER  after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS.
numStudents = 6
numSlicesPizza = 36

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# EXPONENTS **
numSquared = 5 ** 2 # 5 is the base, 2 is the exponent.

# FLOOR-DIVISION // -- Divides, throws out any decimal
myNum = myInt // myFloat

# Addition-Assignment Operator - Mostly used for counters.
myNum = 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness
myNum *= 1
myNum /= 1


# COMPARISON OPERATORS
# IS-EQUAL-TO == Are the two values equal to each other
# Returns True or False based on evaluation
X = 5
print(X == 5)

# NOT-EQUAL-TO != Are the two values NOT equal?
# Returns True or False based on evaluation
print(X !=12)

# GREATER THAN / GREATER-THAN-EQUAL TO
print(5 > 3) # Greater Than
print(12 >= 2) #Greater Than or Equal TO

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS Than
print(12 <= 2) # Less Than or Equal TO

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 16
height = 67.5
eyeColor = "Black"
# In order to ride the teacups, you must be at least 18 years old and 60" tall.
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Black")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
# print(defeatedBoss == True and level > 5 and hasBlueKey == True)


# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
# print(age >= 18 or height >= 60)
# print(age >= 18 or height >= 60 or eyeColor == "Black")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
# print(defeatedBoss == True or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 5
print(a == 5)
print(not (not (a == 5)))


# COMBINING LOGICAL OPERATORS
#print(a == 5 and hasKey == True or isCloud == True)

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)