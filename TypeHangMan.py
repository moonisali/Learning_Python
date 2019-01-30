import random
import sys
print("hangM ver 1.2")

# lets set some variables
wordList = [
"club", "football", "window", "computer", "snow", "juice", "chair", "desktop",
 "laptop", "stadium", "cat", "lemon", "cabel", "mirror", "hat"
           ]

guess_word = []
secretWord = random.choice(wordList) # lets randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []



def beginning():
    print("Hello Player!\n")

    while True:
        name = input("Please enter Your name\n").strip()

        if name == '':
            print("You can't do that! No blank lines")
        else:
            break

beginning()



def newFunc():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gameChoice = input("Would You?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue

newFunc()



def change():

    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)
