import random

#print logo
from art import logo
print(logo)

#Display messages for users
print("Welcome to the number guessing game")

#Choosing game mode
difficulty = str(input("Choose a difficulty type: 'Easy' or 'Hard': ")).lower()
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts")
else:
    attempts = 5
    print(f"You have {attempts} attempts")

#Define game logic using loop
secret_num = random.randint(1, 100)

while True:
    guess = int(input("Pick a number: "))
    if guess > secret_num:
        attempts -= 1
        print("Too High!!")
    elif guess < secret_num:
        attempts -= 1
        print("Too Low!")
    else:
        print(f"Weldone!, you got {secret_num} correctly")
        break

    if attempts > 0:
        print(f"You have {attempts} attempts remaining.")
    else:
        print("You've exhausted all your attempts. GAME OVER!!")

    


