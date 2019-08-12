import random


def find_occurrences(ch):
    return [i for i, ltr in enumerate(word) if ltr == ch]


def update_letter_spaces(ch):
    for occ in find_occurrences(ch):
        wordLetters[occ] = ch


def print_letter_spaces():
    for ltr in wordLetters:
        print(ltr, end=" ")
    print("")


def print_wrong_letters():
    for wl in wrongLetters:
        print(wl, end=" ")
    print("")


def print_progress():
    #########################
    # Word: _ _ _ T _ _
    # Wrong Letters: x y g
    # Tries Left: 5
    #########################
    print("\n")
    print("Word: ", end=" ")
    print_letter_spaces()
    print("Wrong Letters: ", end=" ")
    print_wrong_letters()
    print("Tries Left: ", end=" ")
    print(triesLeft)


####################################
# MAIN

triesLeft = 10

# list of words
words = ["pulverize", "borderland", "dissociative", "literature"]

# pick a word
word = words[random.randint(0,len(words)-1)]

# set up arrays
wordLetters = []
wrongLetters = []
for x in range(len(word)):
    wordLetters.append('_')


while True:
    print_progress()
    letter = input("Guess: ")

    # check if letter has been guessed already
    if wordLetters.count(letter) > 0 or wrongLetters.count(letter) > 0:
        print("\nLETTER HAS BEEN GUESSED")

    # check if letter is in the word
    if word.find(letter) < 0:
        # if not, lose a try and add letter to wrongLetters
        triesLeft -= 1
        wrongLetters.append(letter)
    else:
        # if so, then fill in the blanks
        update_letter_spaces(letter)

    # check if word is complete or player ran out of tries
    if wordLetters.count("_") == 0:
        print("\n\nYou Win!!\n"
              "The word is {}"
              .format(word))
        break
    if triesLeft == 0:
        print("\n\nYou Lose\n"
              "The word is {}"
              .format(word))
        break

