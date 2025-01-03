# Description: BAND NAME GENERATOR

# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in and store it in a variable.
# 3. Ask the user for the name of a pet and store it in a variable.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:

print("Hello! Welcome to the Band Name Generator Created by Gabriel")

city = input("What is the name of your city?")
pet = input("What is the name of your favorite pet?")

band_name = city + pet
print(band_name \n)






###another a bit advanced way to do this 
####

Greeting = "Hello! Welcome to the Band Name Generator Created by Gabriel"
print(Greeting)

city = input("What is the name of your city?")
pet = input("What is the name of your favorite pet?")

band_name = city + pet
print(f"Your band name is {band_name}")

