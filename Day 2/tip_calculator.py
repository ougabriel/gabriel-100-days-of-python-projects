print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill?"))
tip = int(input("How much tip wil you like to give?"))
tippers = int(input("How many people to split the bill?"))

total_tip = (1 + tip/100)
bill_to_pay = float(total_bill * total_tip/tippers)

print(f"Each person should pay £{bill_to_pay: .2f}")