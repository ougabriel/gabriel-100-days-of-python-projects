#Rollercoaster ride by childs age using nested if
height = int(input("What is your height? "))

if height >= 120:
    print("You can use the rollercoater")

    child_age = int(input("What is your age? "))

    if child_age <12:
        print("Please pay: £7.")
    elif child_age <=18: 
        print("Please pay: £10.")
    else: 
        print("Pleaae pay £12.")

else:
    print("Sorry!!, you cannot use this ride.")