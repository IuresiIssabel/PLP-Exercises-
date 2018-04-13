"""Exercise 2:
The challenge for this exercise is to write a version of wc (word count) in Python.
However, your version of wc will return four different types of information about the files:

Number of characters (including whitespace)
Number of words (separated by whitespace)
Number of lines
Number of unique words

The program should ask the user for the name of an input file, and then produce output for that file.

Usage:
    use this txt file as input: /Users/issabel.iuresi/Documents/foo.txt

"""

from collections import Counter


def get_file():
    file = input("Enter the file name: ")
    f = open(file)
    data = f.read()
    f.close()

    return data


def number_of_words():
    data = get_file()

    words = data.split(" ")
    print("Number of words:", len(words))


def number_of_lines():
    data = get_file()

    lines = data.split("\n")
    print("Number of lines:", len(lines))


def number_of_characters():
    data = get_file()

    counts = Counter(letter for line in data
                     for letter in line.lower())

    print("Number of characters:", sum(counts.values()))


def number_of_unique_words():
    data = get_file()
    myset = set(data.split())

    print("Number of unique words:", len(myset))


number_of_lines()
number_of_words()
number_of_characters()
number_of_unique_words()
