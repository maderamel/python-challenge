# open csv file
import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvflie, delimiter=',')
    print(csvreader)




# calculate total number of months included in dataset



#calculate net total of profit/losses over entire perios


# changes in profit/losses over entire period then average


# the greatest increase in profits (date & amount) over entire period
 

# the greatest decrease in profits (date & amount) over entire period  