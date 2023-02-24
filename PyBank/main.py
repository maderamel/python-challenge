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

#calculate net total of profit/losses over entire period   
    #iterates over csvreader again
    #csvfile.seek(0)
    #ext(csvreader)
    
    sum_profit = 0
    sum_loss = 0
    #total number months in dataset
    totalMonths = 0
    averageChange = 0
    #avgMonths = 0

    for row in csvreader:
        profitLoss = 0
        totalMonths = totalMonths + 1 
        profitLoss = int(row[1]) + profitLoss
        averageChange = int(row[1]) - averageChange
        avgChangeList = [averageChange]

        #avgMonths = avgMonths + 1
        if profitLoss > 0:
            sum_profit = sum_profit + profitLoss
        elif profitLoss < 0:
            sum_loss = sum_loss + profitLoss
    totalPL = sum_profit + sum_loss
    average = round(sum(avgChangeList)/len(avgChangeList), 2)

    print(f"Total Months: {totalMonths}")
    print(totalPL)
    print(average)
    print(avgChangeList)
    
# changes in profit/losses over entire period then average


# the greatest increase in profits (date & amount) over entire period
 

# the greatest decrease in profits (date & amount) over entire period  