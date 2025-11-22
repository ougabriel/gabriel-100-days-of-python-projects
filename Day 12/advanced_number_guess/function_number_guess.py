import random
from art import logo

# 1. Display messages for the user
print(logo)
print("Welcome to number guess game!!")

# 2. Define a function that tell the user to choose game difficulty mode

difficulty = str(input("How do you want to play; 'easy' or 'hard': ")).lower()
def game_diff():
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
            return  5
    else: 
        print("Invalid input, defaulting to 'Hard': ")
        return 5 
    
attempts = game_diff()
print(attempts)


# 3. Define a function for Game logic
secret_num = random.randint(1,100)

is_playing = True
while is_playing:
    
    
    def game_logic(): 
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("You've ran out of attempts. GAME OVER!!")

        choice = int(input("Choose a number between 1 & 100: "))
        if choice < secret_num:
            print("Too Low.")
            return attempts - 1
        elif choice > secret_num:
            print("Too High.")
            return attempts - 1
        else:
            print(f"You're correct, you got {secret_num} right.")
    game_logic()
    
is_playing = False