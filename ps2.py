# Problem Set 2, hangman.py
# Name: Abdullahi Samantar
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2-words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file.....")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    i = [False] * len(letters_guessed)
    for x in range(0, len(letters_guessed)):
        i[x] = letters_guessed[x] in secret_word

    i = sum(i)

    return i == len(set(secret_word))


def get_guessed_word(secret_word, letters_guessed):
    i = [' _ '] * len(secret_word)
    for x in range(0, len(secret_word)):
        indices_of_guess = [idx for idx, letter in enumerate(
            secret_word) if letter == letters_guessed[x]]
        for y in range(0, len(indices_of_guess)):
            i[indices_of_guess[y]] = letters_guessed[x]

    i = ''.join(i)
    return i


def get_available_letters(letters_guessed):
    s = string.ascii_lowercase
    for x in range(0, len(letters_guessed)):
        s = s.replace(letters_guessed[x], '')

    return s


def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " +
          str(len(secret_word)) + " letters long.")
    i = ('_') * 50

    print(i)
    j = 0
    x = 0
    r = 0

    while j < len(secret_word) and is_word_guessed(secret_word, letters_guessed) == False:
        print(secret_word)
        print("You have " + str(len(secret_word) - j) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        char_guessed = input("Please guess a letter: ")
        char_guessed = char_guessed.lower()
        if char_guessed == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            my_word = my_word.replace(' ', '')

            print('Possible word matches are: ')
            print(show_possible_matches(my_word))

        # & letters_guessed[x] in get_available_letters(letters_guessed):
        elif char_guessed in get_available_letters(letters_guessed):

            letters_guessed[x] = char_guessed
            if letters_guessed[x] not in secret_word:

                print("Oops! That letter is not in my word:" +
                      get_guessed_word(secret_word, letters_guessed))
                if letters_guessed[x] in "aeiou":
                    x = x + 1
                    j = j + 2
                else:
                    x = x + 1
                    j = j + 1

            else:
                print("Good guess:" +
                      get_guessed_word(secret_word, letters_guessed))

                x = x + 1

        elif r < 3 and char_guessed.isalpha():
            r = r + 1
            print("Oops! You have already guessed that letter. You have " +
                  str(3 - r) + " warnings left:")

        elif char_guessed.isalpha():
            print("Oops! You have already guessed that letter.")

            j = j + 1

        elif r < 3:
            r = r + 1
            print("Oops! That is not a valid letter. You have " +
                  str(3 - r) + " warnings left:")
        else:
            print("Oops! That is not a valid letter.")
            j = j + 1

    if is_word_guessed(secret_word, letters_guessed) == True:
        print("Congratulations, you won!")
        s = set(secret_word)

        print('Your total score for this game is: ' +
              str(len(s) * (len(secret_word) - j)))
    else:
        print("Sorry you ran out of guesses. The word was " + secret_word + ".")


def show_possible_matches(my_word):

    j = 0
    matches = [None] * len(wordlist)

    for x in range(0, len(wordlist)):

        i = [False] * len(my_word)
        if len(wordlist[x]) == len(my_word):
            for y in range(0, len(my_word)):

                i[y] = my_word[y] == '_' or my_word[y] == wordlist[x][y]

            i = sum(i)

            if i == len(wordlist[x]):
                matches[j] = wordlist[x]

                j = j + 1

        else:
            j = j

    res = list(filter(None, matches))

    return res


wordlist = load_words()
secret_word = choose_word(wordlist)
letters_guessed = ['-'] * (len(secret_word))

hangman(secret_word)
