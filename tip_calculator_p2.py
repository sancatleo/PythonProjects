# Description: A simple tip calculator that calculates the amount each person should pay after splitting the bill.

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))  # Number of people splitting the bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)    # Round the final amount to 2 decimal places
print(f"Ecah person should pay: ${final_amount}") # Print the final amount each person should pay

