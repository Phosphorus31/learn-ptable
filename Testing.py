import csv

with open('Elements.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    symbz = []
    names = []
    for row in readCSV:
        symbz.append(row[1])
        names.append(row[2])
        print(row[3])

elem = input()

if elem in symbz:
    print(symbz.index(elem))
elif elem in names:
    print(names.index(elem))
else:
    print('This is not an element in our database, if your spelling is otherwise correct, the database simply does not include that element.')