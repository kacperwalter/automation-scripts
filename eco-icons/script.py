import csv
import os
import json


def csv_to_lst(filename):
    with open(str(filename), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        values = []

        for row in csv_reader:
            if line_count == 0:
                pass
                line_count += 1
            values.append([
                row['Kod produktu'],
                row['Numer strony'],
                row['eco_icon_1'],
                row['eco_icon_2'],
                row['eco_icon_3'],
                row['eco_icon_4'],
            ])
            line_count += 1

        for element in values:
            if(len(element[0]) < 5):
                element[0] = ('0' + element[0])

    return values


def dir_files_without_json():
    files_in_directory = [ files for files in os.listdir(os.getcwd()) ]
    without_extension = []

    for file in files_in_directory:
        if (file.endswith("json")):
            without_extension.append(file[0:-5])

    return without_extension


def csv_iterator(csv_file):
    files_in_directory = dir_files_without_json()
    files_lst = csv_file

    for element in files_lst:
        if element[0] in files_in_directory:
            index = files_in_directory.index(element[0])
            with open(files_in_directory[index] + '.json') as json_file:
                data = json.load(json_file)

                try:
                    if(data[json_file.name[0:-5]]['eco_icon_1'] == "True"):
                        element[2] = "True"
                    if(data[json_file.name[0:-5]]['eco_icon_2'] == "True"):
                        element[3] = "True"
                    if(data[json_file.name[0:-5]]['eco_icon_3'] == "True"):
                        element[4] = "True"
                    if(data[json_file.name[0:-5]]['eco_icon_4'] == "True"):
                        element[5] = "True"
                except KeyError:
                    continue

    return files_lst


def save_csv(filename):
    filled_data = csv_iterator((csv_to_lst('wszystko-v2.csv')))
    
    with open(filename, mode='w') as csv_file:
        fieldnames = ['Kod produktu', 'Numer strony', 'eco_icon_1', 'eco_icon_2', 'eco_icon_3', 'eco_icon_4']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for data in filled_data:
            writer.writerow(
                {
                    'Kod produktu': data[0],
                    'Numer strony': data[1],
                    'eco_icon_1': data[2],
                    'eco_icon_2': data[3],
                    'eco_icon_3': data[4],
                    'eco_icon_4': data[5],
                }
            )


def main():
    save_csv('gotowe.csv')


if __name__ == '__main__':
    main()