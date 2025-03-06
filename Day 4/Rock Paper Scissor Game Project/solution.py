import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = ["rock", "paper", "scissors"]
ascii_art = [rock, paper, scissors]

user_input = int(input("Please type 0 for rock, 1 for paper, 2 for scissors:"))
user_choice = choice[user_input]
print(f"You choose {user_choice}")
print(ascii_art[user_input])

computer_input = random.randint(0, 2)
computer_choice = choice[computer_input]
print(f"Computer chooses {computer_choice}")
print(ascii_art[computer_input])

if user_input == 0 and computer_input == 2:
    print("You Win!!")

# elif user_input == 2 and computer_input == 0:
#     print("You Win!!")
# elif user_input == 1 and computer_input == 0:
##commented code above is correct, this is just to simplify it more
elif user_input > computer_input:
    print("You Win!!")
elif user_input == computer_input:
    print("It's a Draw!!")
elif user_input >= 3 and user_input <0:
    print{"You've typed an invalid number"}
else:
    print("You loose!!")
