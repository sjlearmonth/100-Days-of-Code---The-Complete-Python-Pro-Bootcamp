# Day 2 - Task 2 - Type Error, Checking and Conversion

# PAUSE 1.

# Using the "len(...)" function with incorrect data type.
# Comment out to run the rest of the program.
len(12345)

# Using the "len(...)" function with the correct data type
len("12345")

# PAUSE 2.

# Check the data type of any value using the "type(...)" function.
print(type("Hello"))
print(type(123))
print(type(3.14159))
print(type(True))

# PAUSE 3.

# use the "str(...)" function to convert the integer result from calling the
# "len(...)" function to a string.
print("Number of letters in your name: " + str(len(input("Enter your name: "))))


