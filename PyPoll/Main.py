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
        
        #create a candidate list by adding all the candidate names into an empty list
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    
        #create a dictionary with names as key and total votes as value then add all the total votes(value) of each candidate(key)
        votes = dict_vote.get(candidate, 0)
        dict_vote[candidate] = votes + 1
        

    #get the total vote count by adding all the values from the dictionary
    total_votes = sum(dict_vote.values())

    
    #winner would be the key with the highest value
    winner = max(dict_vote, key=dict_vote.get)
    

    #note: since the total votes and percentage result is dependent on the number of candidates,
    #      we'll need to do a loop function based on total candidates.
    #      And since the print statement for the results needs to be listed per candidate,
    #      the print funtion needs to be inside the loop
    

    
#print the summary statement and write in the text_file for every print 
with open(output_path, "w") as txt_file:

    
#-------------------------------------------------HEADER-------------------------------------------------
    header = (f'''
Election Results
------------------------------------------------------------
Total Votes: {total_votes}
------------------------------------------------------------\n''')
    print(header)
    txt_file.write(header)
#--------------------------------------------------------------------------------------------------------


    #do a loop for each candidate based on candidate list
    for candidate in candidate_list:

        #total number of votes
        candidate_total_vote = dict_vote.get(candidate)
        #percentage of votes
        candidate_percentage_vote = format(((candidate_total_vote / total_votes) * 100), '.3f')
        #print results for each candidate
        output = f"{candidate}: {candidate_percentage_vote}% ({candidate_total_vote})\n"
        print(output)
        txt_file.write(output)


#-------------------------------------------------FOOTER-------------------------------------------------
    winner_result = (f'''
------------------------------------------------------------
Winner: {winner}
------------------------------------------------------------''')
    print(winner_result)
    txt_file.write(winner_result)
#--------------------------------------------------------------------------------------------------------

