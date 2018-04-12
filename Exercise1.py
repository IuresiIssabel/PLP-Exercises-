#!/usr/bin/env python3
"""Exercise 1

This exercise assumes that you have access to a copy of /etc/passwd, the file in which basic user information is stored on Unix computers.
If you don't, then you can likely find such a file by searching for "/etc/passwd example" on the Web. The format is:

nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false

In other words, each line is a set of fields, separated by colon (:) characters.
The first field is the username, and the third field is the ID of the user.
The nobody user has ID -2, the root user has ID 0, and the daemon user has ID 1.
You can ignore all but the first and third fields in the file.

There is one exception to this format: A line that begins with a # character is a comment, and should be ignored by the parser.

For this exercise, you must create a dictionary based on /etc/passwd, in which the dict's keys are usernames and the values are the numeric IDs of those users.
You should then iterate through this dict, displaying one username and user ID on each line in alphabetical order.

"""


def read_file_by_line(file):
    f = open(file)
    username_value, id_value = [], []

    while True:
        lines = f.readlines()

        if not lines:
            break

        lines = [line.strip() for line in lines]
        new_lines = lines.copy()

        for i in range(len(lines)):
            if lines[i][0].__contains__("#"):
                new_lines.remove(lines[i])

        for j in range(len(new_lines)):
            words = new_lines[j].split(":")
            username_value.append(words[0])
            id_value.append(words[2])

    return username_value, id_value


def create_dictionary():
    usernames, ids = read_file_by_line('/etc/passwd')

    professions_dict = {}

    for i in range(len(usernames)):
        professions_dict[usernames[i]] = ids[i]

    return professions_dict


def display_usernames_alphabetical():
    dictionary = create_dictionary()

    for key in sorted(dictionary.__iter__()):
        print(key, dictionary[key])


display_usernames_alphabetical()