# open csv file
import os
import csv
csvpath = os.path.join("./Resources/budget_data.csv")

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next (csvfile)

#print analysis title and break
    print("Financial Analysis")
    print("----------------------------")
    #set profit & loss equal to 0
    sum_profit = 0
    sum_loss = 0
    # variables for total number months in dataset
    totalMonths = 0
    averageChange = 0
    previous_value = 1088983
    # list to hold change values
    avgChangeList = []

    # loop through file
    for row in csvreader:
        #variables for total month and total p/l
        profitLoss = 0
        totalMonths = totalMonths + 1 
        profitLoss = int(row[1]) + profitLoss
        #for average change & max/min profits
        averageChange = int(row[1]) - previous_value
        previous_value = int(row[1])
        avgChangeList += [averageChange]

        #to differentiate between profit and loss values
        if profitLoss > 0:
            sum_profit = sum_profit + profitLoss
        elif profitLoss < 0:
            sum_loss = sum_loss + profitLoss
    totalPL = sum_profit + sum_loss
    average = round(sum(avgChangeList)/(len(avgChangeList)-1), 2)

    #iterate through avg change list for max/min
    maxInc = max(avgChangeList)
    maxDec = min(avgChangeList)
    
    #to match max/min to corresponding month
    if row[1] == maxInc:
        maxMonth = (row[0])

    if maxDec:
        minMonth = (row[0])

    #print analysis
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalPL}")
    print(average)
    print(f"Greatest Increase in Profits: {maxMonth} (${maxInc})")
    print(f"Greatest Decrease in Profits: {minMonth} (${maxDec})") 