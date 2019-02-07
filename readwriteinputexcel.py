import csv
with open('teststrings.csv','r') as csvfile:

    menureader = csv.reader(csvfile, delimiter=',')

nameinput = input("Please Input Name: ")
ageinput = input("Please Input Your Age: ")
jobinput = input("Please Input Your Job: ")

with open('teststrings.csv','a', newline='') as csvfile:

    menuwriter = csv.writer(csvfile, delimiter=',')
    menuwriter.writerow([nameinput, ageinput, jobinput])

    for row in menureader:
                print(', '.join(row))
