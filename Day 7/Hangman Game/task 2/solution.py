import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

#step 1
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


#step 2

#todo1

#placeholder = ""
# masked_word = "_" * len(chosen_word)
# print(masked_word)

#option2
placeholder = ""
word_length = len(word_list)
for position in range(word_length):
    placeholder += "_"
    print(placeholder)

#todo2

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
        print(display)
