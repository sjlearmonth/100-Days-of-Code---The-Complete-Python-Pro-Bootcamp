# Day 2 - Task 5 - Tip Calculator Project

# Print welcome message to the user.
print("Welcome to the tip calculator!")

# Get the total bill amount.
total_bill = float(input("What was the total bill? $"))

# Get the percentage tip.
percentage_tip = int(input("What percentage tip would you like to give? 10 12 15: "))

# Get the number of people to split the bill with.
number_of_people = int(input("How many people to split the bill?: "))

# Calculate the amount each person should pay.
amount_each_to_pay = (total_bill * ( 1.0 + percentage_tip / 100)) / number_of_people

# Print out how much each person should pay.
print(f"Each person should pay ${round(amount_each_to_pay, 2)}.")

