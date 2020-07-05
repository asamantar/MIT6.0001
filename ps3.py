
# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
#
#
# Name          : Abdullahi Samantar
# Collaborators : -
# Time spent    : -

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

WORDLIST_FILENAME = "ps3-words.txt"


def load_words():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    word = word.lower()
    word = word.split()
    subscore1 = 0
    word_length = 0

    for x in range(0, len(word)):
        for y in range(0, len(word[x])):
            subscore1 = SCRABBLE_LETTER_VALUES[word[x][y]] + subscore1

    for x in range(0, len(word)):
        word_length = len(word[x]) + word_length

    subscore2 = 7 * word_length - 3 * (n - word_length)

    if subscore2 > 1:
        subscore2 = subscore2
    else:
        subscore2 = 1

    score = subscore1 * subscore2

    return score


def display_hand(hand):

    vocab = list(hand.keys())
    letters = [None] * sum(hand.values())
    i = 0
    j = -1

    for letter in vocab:
        j = j + 1
        for k in range(0, hand.get(letter)):
            letters[i] = str(vocab[j])
            i = i + 1

    return letters


def deal_hand(n):

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = hand.get('*', 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):

    word = word.lower()
    temp = hand.copy()
    new_hand = temp

    for letter in range(len(word)):
        if hand.get(word[letter], 0) > 0:
            new_hand[word[letter]] = new_hand.get(word[letter], 0) - 1

    return new_hand


def is_valid_word(word, hand, word_list):

    word = word.lower()
    word = word.split()

    k = [0] * len(word)
    for x in range(0, len(word_list)):
        for y in range(0, len(word)):
            i = [False] * len(word[y])
            if len(word[y]) == len(word_list[x]):
                for z in range(0, len(word[y])):

                    i[z] = word[y][z] == '*' and word_list[x][z] in VOWELS or word[y][z] == word_list[x][z]

                i = sum(i)

                if i == len(word[y]):
                    k[y] = k[y] + 1

    i = all(i > 0 for i in k)

    temp = hand.copy()
    new_hand = temp

    j = True
    for x in range(0, len(word)):
        for letter in range(len(word[x])):
            if hand.get(word[x][letter], 0) > 0:
                new_hand[word[x][letter]] = new_hand.get(
                    word[x][letter], 0) - 1
                if new_hand.get(word[x][letter], 0) < 0:
                    j = False
            else:
                j = False

    if j == True and i == True:
        return True
    else:
        return False


def calculate_handlen(hand):

    handlen = sum(hand.values())

    return handlen


def play_hand(hand, word_list):

    word = ''
    Total_score = 0

    while calculate_handlen(hand) > 0 and word != "!!":

        print("Current hand: " + ' '.join(display_hand(hand)))
        word = input('Enter word, or "!!" to indicate that you are finished: ')

        if word == "!!":
            Total_score = Total_score

        elif calculate_handlen(hand) < 0:
            print("Ran out of letters.")

        elif is_valid_word(word, hand, word_list) == True:
            score = get_word_score(word, n)
            print(word + " Earned " + str(score) + " points.")
            Total_score = Total_score + score

            hand = update_hand(hand, word)

        else:

            print("That is not a valid word. Please choose another word.")

        print("Total score: " + str(Total_score) + " points.")


def substitute_hand(hand, letter):

    pass


def play_game(word_list):

    print("play_game not implemented.")


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)


n = 7
hand = deal_hand(n)

play_hand(hand, word_list)
