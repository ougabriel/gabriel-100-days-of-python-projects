#this project uses if/elif/else and logical operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    #using operators to determine if users are within the age of a mid life crises
    elif age >= 45 or age <= 65:
        print("Keep calm, you've got this")

    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")