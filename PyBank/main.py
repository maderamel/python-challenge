# open csv file
import os
import csv
csvpath = os.path.join("./Resources/budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next (csvfile)

#print analysis title and break
    print("Financial Analysis")
    print("----------------------------")
# calculate total number of months included in dataset
    print("Total Months: ", len(list(csvreader)))

#calculate net total of profit/losses over entire period   
    #iterates over csvreader again
    csvfile.seek(0)
    next(csvreader)

    sum_profit = 0
    sum_loss = 0
    totalPL = 0
    profitLoss = 0

    for row in csvreader:
        profitLoss = int(row[1])
        if profitLoss > 0:
            sum_profit = sum_profit + profitLoss
        elif profitLoss < 0:
            sum_loss = sum_loss + profitLoss
    totalPL = sum_profit -sum_loss

    print(totalPL)
    


# changes in profit/losses over entire period then average


# the greatest increase in profits (date & amount) over entire period
 

# the greatest decrease in profits (date & amount) over entire period  