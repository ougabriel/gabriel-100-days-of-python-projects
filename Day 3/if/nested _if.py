#Develop a program that tells if a number is even or odd using if/else statement
number_to_check = int(input("Insert any number: "))

if number_to_check % 2 == 0: #checks if the number is divisible by 2
    print("Even")

else: 
    print("Odd")

###
######
#Rollercoaster ride by childs age using nested if
height = int(input("What is your height? "))

if height >= 120:
    print("You can use the rollercoater")

    child_age = int(input("What is your age? "))

    if child_age <12:
        print("Please pay: £7.")
    else: 
        print("Please pay: £10.")

else:
    print("Sorry!!, you cannot use this ride.")