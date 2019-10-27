import csv

with open('/Users/ricardohavill/Desktop/pics.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)

