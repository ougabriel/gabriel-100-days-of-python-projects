# You can combine different conditions using logical operators.

# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false

# PAUSE 1 - Age 45 to 55 Modifier
# Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than 45, and it's also less than 55.

# NOTE: The warning for simplification is just a suggestion. You can consider it and chose it, or you can ignore it. In this lesson I wanted to show you the and, or and not logical operators. So I recommend keeping the original code in case you come back to this lesson for review.

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