import os
import csv

#  Path to collect data from the Resources fold
budget_csv = os.path.join('.', 'pybank', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    months = []
    profit = []
    
    count = 0
    total = 0
    totalchange = 0
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
        totalchange = totalchange + (profit[i]-profit[i-1])
        if profit[i]-profit[i-1] > giamount:
            gidate = months[i]
            giamount = profit[i]-profit[i-1]
        
        
        if profit[i]-profit[i-1] < gdamount:   
            gddate = months[i]
            gdamount = profit[i]-profit[i-1]
            
    average = totalchange/(count-1)        

print ("Financial Analysis")
print("----------------------------")
print("Total Months: ", count)
print("Total: $" + str(total))
print("Average Change: $" + "%.2f" % average)
print("Greatest Increase in Profits: " + str(gidate) + " $" + str(giamount))
print("Greatest Decrease in Profits: " + str(gddate) + " $" + str(gdamount))

