import random
import arts

print(arts.logo)
print("\n")
print("I am thinking of a number between 1 & 20: ")
print("\n")

to_continue = True
while to_continue:
    num = random.randint(1, 20)
    attempts = 0

    is_guessing = True
    while is_guessing:
        entry1 = int(input("Pick a number: "))
        attempts += 1
        if entry1 > num:
            print("Too High. ")
        elif entry1 < num:
            print("Too Low. ")
        elif entry1 == num:
            print(f"You are correct, you guessed {num}, with {attempts} guesses. ")
            print(arts.you_win) 
            is_guessing = False
    answer = input("Will you like to start again? Type 'Yes/No'. ")
    if answer.lower() == 'no':
            print("Thanks for playing, Goodbye!!. 👋 ")
            print(arts.goodbye)
            to_continue = False



    
    
    
    



