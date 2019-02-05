import csv
with open('teststrings.csv','r') as csvfile:

    menureader = csv.reader(csvfile, delimiter=',')
    for row in menureader:
        print(', '.join(row))

    with open('teststrings.csv','a', newline='') as csvfile:

        menuwriter = csv.writer(csvfile, delimiter=',')
        menuwriter.writerow(['starbucks', 'reserve', 'coffee'])

        for row in menureader:
            print(', '.join(row))
