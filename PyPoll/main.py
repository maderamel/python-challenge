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

    for row in csvreader:
        totalBallots = totalBallots + 1
        
        fullCandidateList = [(row[2])]
        
        print(fullCandidateList)
        candidateList = []
        
        for i in fullCandidateList:
            if i not in candidateList:
                candidateList.append(i)

    for i in candidateList:
        print(i)

    


    print(f"Total Votes: {totalBallots}")
    print("----------------------------")



