#PyPoll Application
#Doug Watola

import os
import csv
import operator


election_data_path = "./Resources/election_data.csv"
outPath = "./Resources/election_results.txt"

#=======================================================
#Read election csv file and derive unique list of canidates
#=======================================================

with open(election_data_path, mode='r', newline='') as electiondata:
    electioneval = csv.reader(electiondata, delimiter=',')
          
    csv_header=next(electioneval)
    
    county = []
    canidates = []
    
    for row in electioneval:
        county.append(row[1])
        canidates.append(row[2])
    
    total_votes=len(canidates)
    #Use set to create a unique set of canidates    
    unique_canidates = set(canidates)
    unique_canidates_list=list(unique_canidates)
        
#=======================================================
#Count to votes for each of the unique canidates
#=======================================================
vote_results = {}
canidate_count = 0
for x in range(len(unique_canidates_list)):
    
    canidate_dict = unique_canidates_list[x]
    canidate_count = 0  #initiate the count before counting votes for canidate on list
    for i in range(len(canidates)):
        if (canidate_dict == canidates[i]):  #cycle through all of the unique canidates
            canidate_count = canidate_count + 1
        else:
            vote_results.update({canidate_dict:canidate_count})
#=======================================================
#Print the results in the required format
#=======================================================

print("Election Results")
print("------------------------")
print("Total Votes:  %s" % sum(vote_results.values()))

percentage = 0
print("------------------------")
for key, value in sorted(vote_results.items(), key=lambda item: item[1], reverse=True):
    percentage = round(100 * (value/(sum(vote_results.values()))),2)
    #print(percentage)
    print("%s: %s %%  (%s)" % (key,percentage,value))
    #print("%s: (%s)" % (key,value))
    
print("------------------------")
vote_results_sorted = sorted(vote_results.items(), key=operator.itemgetter(1), reverse=True)

#Extract the winning canidate from the vote results
winner = next(iter(vote_results_sorted))
print("Winner: %s" % (list(winner)[0]))
print("------------------------")  

#=======================================================
#Write the results in the required format
#=======================================================

with open(outPath, mode='w', newline='') as election_results:
    election_results.write("Election Results \n" )
    election_results.write("----------------------- \n" )
    election_results.write("Total Votes:  %s \n" % sum(vote_results.values()))
    election_results.write("----------------------- \n" )
    for key, value in sorted(vote_results.items(), key=lambda item: item[1], reverse=True):
        percentage = round(100 * (value/(sum(vote_results.values()))),2)
        election_results.write("%s: %s %%  (%s)\n" % (key,percentage,value))
    election_results.write("----------------------- \n" )
    election_results.write("Winner: %s \n" % (list(winner)[0]))
    election_results.write("----------------------- \n" )
