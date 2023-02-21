# open csv file
import os
import csv
csvpath = os.path.join("./Resources/budget_data.csv")


netPL = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(next(csvreader)) #printed header row just to see if path worked and it did 

    #skip the header
    csv_header = next (csvfile)

# calculate total number of months included in dataset
    print("Total Months: ", len(list(csvreader)))

#calculate net total of profit/losses over entire perios
    profitLoss = csvreader
    for row in profitLoss:
        if not str(row[1]).startswith ('P'):
            profitLoss = profitLoss+ int(row[1])
    print(profitLoss)
    


# changes in profit/losses over entire period then average


# the greatest increase in profits (date & amount) over entire period
 

# the greatest decrease in profits (date & amount) over entire period  