"""Exercise 4:

JSON (JavaScript Object Notation) is an increasingly popular format for data exchange.
It is compatible with a large number of programming languages, is lightweight, and is easy to validate.
Python's json module lets us read JSON easily with the json.load function.

In this exercise, you are analyzing test data in a high school.
Test scores are in a set of files in the `scores` directory;
each file represents the scores for one class, and contains JSON.
Thus, if we are trying to analyze the scores from class 9a, the scores would be in a file called `9a.json`:

[{"math" : 90, "literature" : 98, "science" : 97},
{"math" : 65, "literature" : 79, "science" : 85},
{"math" : 78, "literature" : 83, "science" : 75},
{"math" : 92, "literature" : 78, "science" : 85},
{"math" : 100, "literature" : 80, "science" : 90}
]

The directory may also contain files for 10th grade (10a.json, 10b.json, and 10c.json)
and other grades and classes in the high school.

Note that valid JSON uses double quotes ("), not single quotes (').
This can be surprising and frustrating for Python developers to discover!
Also notice that the file contains the JSON equivalent of a list of dicts.

For this exercise, you must summarize, for each class, the highest, lowest, and average test scores for each subject,
in each class. Given two files (9a.json and 9b.json) in the scores directory, we would see the following output:

scores/9a.json
   science: min 75, max 97, average 86.4
   literature: min 78, max 98, average 83.6
   math: min 65, max 100, average 85.0
scores/9b.json
   science: min 35, max 95, average 82.0
   literature: min 38, max 98, average 72.0
   math: min 38, max 100, average 77.0

"""

import json
import functools


def read_from_json(file):
    with open(file, 'r') as infile:
        data_from_file = json.load(infile)

    return data_from_file


def write_to_json(file, data):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def create_dictionary(file):
    scores = read_from_json(file)
    math_list = []
    science_list = []
    literature_list = []

    for score in scores:
        for i in scores[score]:
            for keys, value in i.items():
                if keys == 'math':
                    math_list.append(value)
                if keys == 'science':
                    science_list.append(value)
                if keys == 'literature':
                    literature_list.append(value)
    return math_list, science_list, literature_list


def create_data_to_send(file):
    math_list, science_list, literature_list = create_dictionary(file)

    data_for_json = "science: min {min_science}, max {max_science}, avg {avg_science}\n literature: " \
                    "min {min_literature}, max {max_literature}, avg {avg_literature}\n math: min {min_math}, " \
                    "max {max_math}, avg {avg_math}".format(min_science=min(science_list),
                                                            max_science=max(science_list),
                                                            avg_science=functools.reduce(lambda x, y: x + y,
                                                                                         science_list) / len(
                                                                science_list),
                                                            min_literature=min(literature_list),
                                                            max_literature=max(literature_list),
                                                            avg_literature=functools.reduce(lambda x, y: x + y,
                                                                                            literature_list) / len(
                                                                literature_list),
                                                            min_math=min(math_list),
                                                            max_math=max(math_list),
                                                            avg_math=functools.reduce(lambda x, y: x + y,
                                                                                      math_list) / len(
                                                                math_list))

    write_to_json("9b.json", data_for_json)


create_data_to_send('9a.json')
