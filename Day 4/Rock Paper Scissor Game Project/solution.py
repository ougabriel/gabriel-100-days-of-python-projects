import random

# Rock Paper Scissors ASCII Art
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choices = ["rock", "paper", "scissors"]
ascii_art = [rock, paper, scissors]

#Get user input
user_input = int(input("Choose a number; 0 for rock, 1 for paper, or 2 for scissors: "))

#validate user input
if user_input < 0 or user_input > 2:
    print("Please choose a correct number from 0 -2")
else:
    user_index = choices[user_input]
    user_choice = user_index
    print(f"You choose {user_choice}")
    print(ascii_art[user_input])



#Computer randomly chooses a number
computer_random_num = random.randint(0, 2)
computer_choice = computer_random_num

print(f"Computer chooses {computer_choice}")
print(ascii_art[computer_random_num])

if user_choice == computer_choice:
    print("You Loose; GAMEOVER!!")
else: 
    print("You Won!!")




