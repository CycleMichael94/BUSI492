import csv
with open('teststrings.csv','r') as csvfile:

    menureader = csv.reader(csvfile, delimiter=',')
    for row in menureader:
        print(', '.join(row))
