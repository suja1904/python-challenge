import os
import csv

#  Path to collect data from the Resources fold
budget_csv = os.path.join('.', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    count = 0
    total = 0
    gidate = ""
    giamount = 0
    gddate = ""
    gdamount = 0
    
    # Loop through the data
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        if count == 1 and int(row[1]) > 0:
            gidate = row[0]
            giamount = int(row[1])
        if giamount < int(row[1]) and int(row[1]) > 0:
            giamount = int(row[1])
            gidate = row[0]
        if count == 1 and int(row[1]) < 0:
            gddate = row[0]
            gdamount = int(row[1])
        if gdamount > int(row[1]) and int(row[1]) < 0:    
            gddate = row[0]
            gdamount = int(row[1])
            
print(count)
print(total)
print(giamount)
print(gidate)
print(gdamount)
print(gddate)
