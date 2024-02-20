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
    print(csvreader)
    
    # Loop through the data
    for row in csvreader:
        count = count + 1
        
print(count)   
