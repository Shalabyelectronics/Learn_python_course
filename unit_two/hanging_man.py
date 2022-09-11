# We will import system from os library to use shell command to clear our screen terminal
from os import system


# first lets darw the hanging man
# The parts that we are going to use to draw our hanging man.
HANGING_MAN = ["|","_","0","/","\\"]
# We have 5 parts to draw our hanging man.
draw_it = {
        0: HANGING_MAN[1]*4,
        1: HANGING_MAN[0]+" "*2+HANGING_MAN[0],
        2: HANGING_MAN[0]+" "*2+HANGING_MAN[2],
        3: HANGING_MAN[0]+" "+HANGING_MAN[3]+HANGING_MAN[0]+HANGING_MAN[4],
        4: " "* 2 + HANGING_MAN[3] +" "+ HANGING_MAN[4] 
        }

# First we need to ask player one about the word.
# As the word must be only more the 2 letters and not a number.
while True:
    word = input("Player 1: Choose the word? ")
    if len(word)> 2 and word.isdigit() != True:
        break
    else:
        system("clear")
        print(f"Please choose the word have more than 2 letters\nand it is not a number.\n")
# After that we need to clear the screen so player 2 can't cheat.
system("clear")
# creat a guessd_letters list from word to be ____ like this>
guessed_letters = []
for _ in word:
    guessed_letters.append("_")
# After that we are going to start the game by setting the below variables.

# tries it will hold the length of our tries when we choose wrong letter
tries = len(draw_it)

# Here we will save all parts to draw our hanging man.
draw_hanging_man = []

# Here we will save all right guessed tries number.
correct_guessed_number = 0

while tries:
    print("\nPlayer 2: Please Guess The word.\n")
    choosen_letter = input("Choose the letter : ")
    if choosen_letter in word and choosen_letter not in guessed_letters:
        for index,letter in enumerate(word):    
            if letter == choosen_letter:
                guessed_letters[index] = choosen_letter
                correct_guessed_number += 1
        system("clear")
        if correct_guessed_number == len(word):
            system("clear")
            print(" ".join(guessed_letters))
            print(f"Woow you gussed it the word is {word}.")
            break
        else:
            print(f"Nice you need to guss [{len(word) - correct_guessed_number}] letter(s)")
            print(" ".join(guessed_letters))

    elif choosen_letter in guessed_letters:
        system("clear")
        print(f"You already guessed the letter {choosen_letter}")
        print("_"*34)
        print(" ".join(guessed_letters))
    else:
        system("clear")
        part_number = len(draw_it) - tries
        draw_hanging_man.append(draw_it[part_number])
        tries -= 1
        print(f"Oops it is a wrong letter\nYou have [{tries}] tries left!!!")
        for part in draw_hanging_man:
            print(part)
        print("_"*34)
        print(" ".join(guessed_letters))
        
else:
    system("clear")
    for part in draw_hanging_man:
            print(part)
    print(f"\tThe word was [{word}].")
    print("\n\tGame over")
    
