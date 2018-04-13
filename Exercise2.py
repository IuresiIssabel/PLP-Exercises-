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


def select_an_option():
    while True:
        print(
            '\nMenu: \n\n1. Number of characters (including whitespace)\n2. Number of words (separated by '
            'whitespace)\n3. Number of lines \n4. Number of unique words\n')
        option = input("Enter an option\n")

        if option == '1':
            number_of_characters()
        elif option == '2':
            number_of_words()
        elif option == '3':
            number_of_lines()
        elif option == '4':
            number_of_unique_words()
        else:
            print("This is not an option!")
            break


select_an_option()
