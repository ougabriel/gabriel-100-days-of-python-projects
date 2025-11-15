from art import logo

print("Welcome to the Number Guessing Game: ")
print("I'm thinking of a number between 1 and 100: ")


difficulty = input(str("Please pick a difficulty level; type 'Easy' or 'Hard': ")).lower()
if difficulty == "easy":
        attempts = 5
else:
        attempts = 10
print(f"You have {attempts} attempts remaining to guess the number.")




