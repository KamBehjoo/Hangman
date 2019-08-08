import random

def find_occurrences( ch ):
    return [i for i, ltr in enumerate(word) if ltr == ch]


def update_letter_spaces( ch ):
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
    #Word: _ _ _ T _ _     ##
    #Wrong Letters: x y g  ##
    #Tries Left: 5         ##
    #########################
    print("################################")
    print("Word: ", end=" ")
    print_letter_spaces()
    print("Wrong Letters: ", end=" ")
    print_wrong_letters()
    print("Tries Left: ", end=" ")
    print(tries)




tries = 10

#list of words
words = ["pulverize", "borderland", "dissociative", "literature"]

#pick a word
word = words[random.randint(0,len(words)-1)]
wordLetters = []
for x in range(len(word)):
    wordLetters.append('_')

wrongLetters = []

while True:
    print_progress()
    letter = input("Guess: ")
    if word.find(letter) < 0:
        tries -= 1
        wrongLetters.append(letter)
    else:
        update_letter_spaces(letter)

    if wordLetters.count("_") == 0:
        print("\n\nYou Win!!\n"
              "The word is {}"
              .format(word))
        break;
    if tries == 0:
        print("\n\nYou Lose\n"
              "The word is {}"
              .format(word))
        break