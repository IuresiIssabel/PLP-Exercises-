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
