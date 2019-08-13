import random
import requests
from bs4 import BeautifulSoup


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
    print("Word: ", end=" ")
    print_letter_spaces()
    print("Wrong Letters: ", end=" ")
    print_wrong_letters()
    print("Tries Left: ", end=" ")
    print(triesLeft)


####################################
# MAIN

# get the word of the day
url = 'https://www.merriam-webster.com/word-of-the-day'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
wordOfTheDay = soup.find_all("h1")[0].get_text()

# random word
localWords = ["pulverize", "borderland", "dissociative", "literature"]
randomLocalWord = localWords[random.randint(0,len(localWords)-1)]

# random word or Word of the Day
words = [wordOfTheDay, randomLocalWord]
word = ""

while True:
    onlineOrLocal = input("(a) Word of the Day\n"
                      "(b) Random Word")
    if onlineOrLocal == 'a':
        word = wordOfTheDay
        break
    elif onlineOrLocal == 'b':
        word = randomLocalWord
        break
    else:
        print("Not a valid selection.\n")

# set up arrays
wordLetters = []
wrongLetters = []
for x in range(len(word)):
    wordLetters.append('_')

# of tries
triesLeft = 10


while True:
    print_progress()
    letter = input("Guess: ")
    print('\n')

    # check if letter has been guessed already
    if wordLetters.count(letter) > 0 or wrongLetters.count(letter) > 0:
        print("\nLETTER HAS BEEN GUESSED")
        continue

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

