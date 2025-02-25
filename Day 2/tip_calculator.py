# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill?"))
# tip = int(input("How much tip wil you like to give?"))
# tippers = int(input("How many people to split the bill?"))

# total_tip = (1 + tip/100)
# bill_to_pay = float(total_bill * total_tip/tippers)

# print(f"Each person should pay £{bill_to_pay: .2f}")


print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? £"))
tip = int(input("How much tip wil you like to give? 10 12 15"))
tippers = int(input("How many people to split the bill?"))

tip_as_percent = tip/100
total_bill_with_tip = total_bill * tip_as_percent
bill_amount = total_bill + total_bill_with_tip
bill_per_tippers = bill_amount/tippers
final_amount = round(bill_per_tippers, 2)

print(f"Each pays will pay the amount of £{final_amount}")

