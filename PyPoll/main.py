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
    percentCharles = 0
    totalCharles = 0
    counterCharles = []

    for row in csvreader:
        totalBallots = totalBallots + 1
        
        #makes candidate column a list
        fullCandidateList = [(row[2])]
        
        #look through candidate column list to get new unique list
        for i in fullCandidateList:
            if i not in candidateList:
                candidateList.append(i)
    
        for i in fullCandidateList:
            if i == candidateList[0]:
                counterCharles += [i]
        totalCharles = len(counterCharles)
        percentCharles = round((totalCharles/totalBallots)*100, 3)


    


    print(f"Total Votes: {totalBallots}")
    print("----------------------------")
    print(f"{candidateList[0]}: {percentCharles}% ({totalCharles})")
    print(f"{candidateList[1]}: ")
    print(f"{candidateList[2]}: ")
    print("----------------------------")
    print(f"Winner: ")
    print("----------------------------")

