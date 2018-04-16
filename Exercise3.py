"""Exercise 3:

In a CSV ("comma-separated values") file, each record is stored on one line, and fields are separated by commas.
Sometimes, the comma is replaced by another character, so as to avoid potential ambiguity;
use a TAB character ('\t' in Python strings).

Python comes with a csv module that handles many of the tasks associated with writing to and reading from CSV files.
For example, you can write to a file with the following:

import csv

with open('/tmp/stuff.csv', 'w') as f:
   o = csv.writer(f)
   o.writerow(range(5))
   o.writerow(['a', 'b', 'c', 'd', 'e'])

For this exercise, create a program that reads from one CSV file (/etc/passwd), and writes to another one.
You are to read from /etc/passwd, and produce a file whose contents are the username (index 0) and
the user ID (index 2). Note that a record may contain a comment, in which it will not have anything at index 2;
you should take that into consideration when writing the file.
The output file should use TAB characters to separate the elements.

Thus, the input will look like:

root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false



… and the output will look like:
root    0
daemon  1
_ftp    98

"""


import csv


def read_file_by_line(file):
    username_value, id_value = [], []

    with open(file, 'r') as f:
        while True:
            lines = f.readlines()

            if not lines:
                break

            lines = [line.strip() for line in lines]
            new_lines = lines.copy()

            for i in lines:
                if i[0].__contains__("#"):
                    new_lines.remove(i)

            for j in new_lines:
                words = j.split(":")
                username_value.append(words[0])
                id_value.append(words[2])

    return username_value, id_value


def create_dictionary(file):
    usernames, ids = read_file_by_line(file)
    users_dict = {}

    for i in range(len(usernames)):
        users_dict[usernames[i]] = ids[i]

    return users_dict


def write_in_csv_file(input_file, output_file):
    dictionary = create_dictionary(input_file)

    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for key, value in dictionary.items():
            writer.writerow([key, value])


write_in_csv_file('/etc/passwd', '/Users/issabel.iuresi/Documents/stuff.csv')
