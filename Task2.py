import csv

with open('data_2023-02-11.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

