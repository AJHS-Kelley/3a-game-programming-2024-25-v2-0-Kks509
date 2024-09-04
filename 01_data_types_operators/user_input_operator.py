# User Input Practice, Kelston Spaulding, v0.0

# input() is the built-in function to get information from the KEYBOARD.
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter.\n")
print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!

# INCORRECT, CAUSES A CONCANTATION ERROR
# myNumber = input("Please type an INTEGER number and press enter.\n")
# print(myNumber + 5)

# CORRECT -- Use a wrapper.
myNumber = int(input("Please type an INTEGER number and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
# int() will convert the date to an INTEGER if possible.
newNumber = input("Please type a value and press enter.\n")
print(int(newNumber)) # can convert STRING to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.

# float() will convert the date to a FLOAT if possible.
newNumber = input("Please type a value and press enter.\n")
#print(int(newNumber)) <-- cannot convert FLOAT to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.

# str() will convert the date to a STRING if possible.
newNumber = 5
print(newNumber + newNumber) # Should print 10
print(str(newNumber + newNumber)) # Should print 55.

