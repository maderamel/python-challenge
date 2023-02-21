# open csv file
import os
import csv
csvpath = os.path.join("./Resources/budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(next(csvreader)) #printed header row just to see if path worked and it did 

    #skip the header
    csv_header = next (csvfile)

# calculate total number of months included in dataset
    print(len(list(csvreader)))

#calculate net total of profit/losses over entire perios
    

# changes in profit/losses over entire period then average


# the greatest increase in profits (date & amount) over entire period
 

# the greatest decrease in profits (date & amount) over entire period  