print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

#Pizza sizes

#Small pizza S
S = 15
#medium pizza M
M = 20
#Large pizza L
L = 25

#how much they need to pay based on their pizza size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You've chosen the wrong pizza size")

#How much they need to add on their bill based on their pepperoni size
if pepperoni == "Y":
    if size == "S":
        bill += 2
else:
        bill += 3


#How much they need to pay if they want an extra cheese on top.
if extra_cheese == "Y":
     bill += 1

print(f"Your final bill is £{bill}")