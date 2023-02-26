# open csv file
import os
import csv
csvpath = os.path.join("./Resources/election_data.csv")

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next (csvfile)

    #print analysis title and break
    print("Election Results")
    print("----------------------------")

    #variables
    totalBallots = 0
    fullCandidateList = []
    candidateList = []

    for row in csvreader:
        totalBallots = totalBallots + 1
        
        fullCandidateList = [(row[2])]
        
        
        for i in fullCandidateList:
            if i not in candidateList:
                candidateList.append(i)

    print(candidateList)

    


    print(f"Total Votes: {totalBallots}")
    print("----------------------------")



