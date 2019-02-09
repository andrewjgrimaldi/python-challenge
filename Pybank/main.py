# PyRoll
# Andrew
# 2/1/2019
import csv

csvpath = r"C:\Users\andre\Desktop\Data Analysis Class\Homework 3\election_data.csv"
    
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    total_voters = 0
    candidates = { }

    #jisan note:  we did this a different way that the solution.  We used enumerate in the loop to get the count.  
    
    for index, value in enumerate(reader):
        if index == 0:
            continue
        total_voters += 1
        voter_id = value[0]
        county = value[1]
        candidate = value[2]
        #      ( boolean expression - True or False )
        # if the item is not in the list
        if not candidate in candidates:
            # { candidate : 0 }
            candidates[candidate] = 0
        else:
            candidates[candidate] += 1
        
    for key, value in candidates.items():
        print("Candidate: " + key)
        print(" -> Votes: " + str(value))
        print(" -> %: " + str(total_voters / value * 100)
