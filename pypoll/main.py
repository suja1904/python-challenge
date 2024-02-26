import os
import csv

#  Path to collect data from the Resources fold
election_csv = os.path.join('.', 'pypoll', 'Resources', 'election_data.csv')

#List to store data
ID = []
candidate_votes = {}
winner = ""

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:

        # Add ID
        ID.append(row[0])

        if row[2] in candidate_votes:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        else:
            candidate_votes[row[2]] = 1

    for c in candidate_votes:
        if winner in candidate_votes:
           if candidate_votes[winner] < candidate_votes[c]:
               winner = c
        else:
            winner = c

print("Election Results")
print("----------------------------")
print("Total Votes: ", len(ID))
print("----------------------------")

for c in candidate_votes:
    percent = candidate_votes[c]/len(ID)*100
    print(c + ": " + "%.2f" % percent + "% (" + str(candidate_votes[c]) + ")")

print("----------------------------")
print("Winner: "+ winner)
print("----------------------------")

# f = open('workfile', 'w', encoding="utf-8")
