import os
import csv

#  Path to collect data from the Resources fold
budget_csv = os.path.join('.', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    months = []
    profit = []
    
    count = 0
    total = 0
    gidate = ""
    giamount = 0
    gddate = ""
    gdamount = 0
    average = 0
    # Loop through the data
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        count = count + 1
        total = total + int(row[1])
    
    for i in range(1,len(months)):    
        
        if profit[i]-profit[i-1] > giamount:
            gidate = months[i]
            giamount = profit[i]-profit[i-1]
        
        
        if profit[i]-profit[i-1] < gdamount:   
            gddate = months[i]
            gdamount = profit[i]-profit[i-1]
            
    average = total/count        

print(count)
print(total)
print(giamount)
print(gidate)
print(gdamount)
print(gddate)
print(average)
