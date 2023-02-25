# open csv file
import os
import csv
csvpath = os.path.join("./Resources/election_data.csv")

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next (csvfile)