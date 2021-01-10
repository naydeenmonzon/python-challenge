import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('Analysis','results.csv')

total_votes = 0
dict_vote = {}
candidate_list = []

with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    header = next(data)
    
    #loop through each row...
    for row in data:
        
        #select the candidate value from the header list
        candidate = row[2]
        #then add the name into an empty list(candidate_list)
        if candidate not in candidate_list:
            candidate_list.append(candidate)

        #create a dictionary with names as key and total votes as value and add all the total votes(value) of each candidate(key)
        votes = dict_vote.get(candidate, 0)
        dict_vote[candidate] = votes + 1
        
    
    #get the total vote count by adding all the values from the dictionary
    total_votes = sum(dict_vote.values())

    #instead of using actual names from the file, list each candidate names in generic format so the script can be used again
    Candidate1 = candidate_list[0]
    Candidate2 = candidate_list[1]
    Candidate3 = candidate_list[2]
    Candidate4 = candidate_list[3]
    
    #get the total vote count for each candidate
    Candidate1_votes = list(dict_vote.values())[0]
    Candidate2_votes = list(dict_vote.values())[1]
    Candidate3_votes = list(dict_vote.values())[2]
    Candidate4_votes = list(dict_vote.values())[3]
    
    #get the percentage vote from each candidate by dividing the value of each key from the total votes
    Candidate1_percent = format(((dict_vote[Candidate1] / total_votes) * 100), '.3f')
    Candidate2_percent = format(((dict_vote[Candidate2] / total_votes) * 100), '.3f')
    Candidate3_percent = format(((dict_vote[Candidate3] / total_votes) * 100), '.3f')
    Candidate4_percent = format(((dict_vote[Candidate4] / total_votes) * 100), '.3f')

    #winner would be the key with the highest value
    winner = max(dict_vote, key=dict_vote.get)
    
    #print results
    output = (f'''
    Election Results
    ------------------------------------------------------------
    Total Votes: {total_votes}
    ------------------------------------------------------------
    {Candidate1}: {Candidate1_percent}% ({Candidate1_votes})
    {Candidate2}: {Candidate2_percent}% ({Candidate2_votes})
    {Candidate3}: {Candidate3_percent}% ({Candidate3_votes})
    {Candidate4}: {Candidate4_percent}% ({Candidate4_votes})
    ------------------------------------------------------------
    Winner: {winner}
    ------------------------------------------------------------''')
    print(output)
    
with open(output_path, "w") as txt_file:
    txt_file.write(output)
