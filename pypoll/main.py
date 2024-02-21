import os
import csv

#  Path to collect data from the Resources fold
election_csv = os.path.join('.', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        
        count = count + 1
        
           

print(count)

