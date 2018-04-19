"""Exercise 5:
Write a program which reads from a text file (text file to be provided) and returns
individual words in lowercase and stripped from digits and punctuation. It should return a list of words.

    Problem 5.1
Make a function which takes as input the list of words
and returns a dict that has as a key the word and as value the number of occurrences.

    Problem 5.2
Return the word with the most occurrences.
"""

import string


def make_a_word_list_from_a_file(file):
    words = []
    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(remove_punctuation(word, string.punctuation))
    return words


def remove_punctuation(word, punctuation_char):
    for char in word.strip():
        if char in punctuation_char:
            word = word.replace(char, "")
    return word


def occurrences_in(list_name):
    out = [0] * len(list_name)
    for i in range(len(list_name)):
        out[i] = list_name[:i].count(list_name[i])
    return out


def create_dictionary(file):
    values = make_a_word_list_from_a_file(file)
    keys = occurrences_in(values)
    dictionary = {}
    y = 0

    for item in values:
        dictionary[item] = keys[y]
        y = y + 1

    return dictionary


def return_maximum(dictionary):
    return max(dictionary, key=dictionary.get)


print("Dictionary:\n", create_dictionary('data.txt'))
print("\nThe word with the most occurrences:", return_maximum(create_dictionary('data.txt')))