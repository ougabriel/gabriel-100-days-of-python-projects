import random

print("Welcome to Who's gonna pay the bill selector")

friends = input("Enter your names separated by a comma ',':").split()

#Option 1
choosen_friend = random.choice(friends)
print(f"{choosen_friend} is going to pay the bill.")

#
# Lucy, Mandy, Sue, Rain, John, April, Phillip, William, Gabby

#option 2 

choosen_index = random.randint(0, 8)  #since we have nine names and friends list will not increase or decrease
choosen_friend = friends[choosen_index]
print(f"{choosen_friend} will sort the bill.")

#Option 3  Advanced
choosen_index = random.randint(0, len(friends) -1) 
choosen_friend = friends[choosen_index]

print(f"{choosen_friend} is paying the bill.") 