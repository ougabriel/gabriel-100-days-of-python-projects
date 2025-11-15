import random
from art import logo

print("Welcome to the Number Guessing Game: ")
print("I'm thinking of a number between 1 and 100: ")

#Define difficulty level and number of attempts
difficulty = input(str("Please pick a difficulty level; type 'Easy' or 'Hard': ")).lower()
if difficulty == "easy":
        attempts = 5
else:
        attempts = 10

print(f"You have {attempts} attempts remaining to guess the number.")

#Generate a secret number 
choice = random.randint(1, 100)

#Run a loop for each guess attempt
while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess > choice:
        attempts -= 1
        print("Too High.")
    elif guess < choice:
        attempts -= 1
        print("Too Low.")
    else:
        print(f"You're right this time, you guessed {choice} correctly.")
        break
    #Show the number of attempts left 
    if attempts > 0:
         print(f"You have {attempts} attempts remaining.")
    else:
         print("You've used up all your attempts, GAME OVER!!")
         print(f"The correct number is {choice}")







