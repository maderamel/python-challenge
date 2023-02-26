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
    percentDiana = 0
    totalDiana = 0
    counterDiana = []
    percentRaymon = 0
    totalRaymon = 0
    counterRaymon = []

    for row in csvreader:
        totalBallots = totalBallots + 1
        
        #makes candidate column a list
        fullCandidateList = [(row[2])]
        
        #look through candidate column list to get new unique list
        for i in fullCandidateList:
            if i not in candidateList:
                candidateList.append(i)
        
        #add to counter for each candidate to track vote counts 
        for i in fullCandidateList:
            if i == candidateList[0]:
                counterCharles += [i]
            elif i == candidateList[1]:
                counterDiana += [i]
            elif i == candidateList[2]:
                counterRaymon += [i]
        
    #len counter for vote counts & vote count/total ballots for %
    totalCharles = len(counterCharles)
    percentCharles = round((totalCharles/totalBallots)*100, 3)

    totalDiana = len(counterDiana)
    percentDiana = round((totalDiana/totalBallots)*100, 3)

    totalRaymon = len(counterRaymon)
    percentRaymon = round((totalRaymon/totalBallots)*100, 3)

    #to find winner
    totalslist = [totalCharles, totalDiana, totalRaymon]
    winnerVal = max(totalslist)

    for i in range(len(totalslist)):
        if totalslist[i] == winnerVal:
            winner = candidateList[i]

    print(f"Total Votes: {totalBallots}")
    print("----------------------------")
    print(f"{candidateList[0]}: {percentCharles}% ({totalCharles})")
    print(f"{candidateList[1]}: {percentDiana}% ({totalDiana})")
    print(f"{candidateList[2]}: {percentRaymon}% ({totalRaymon})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

