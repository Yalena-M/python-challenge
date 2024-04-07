import os
import csv

#csv path
election_data_csv = "C:\\Users\\jacya\\.ssh\\.ssh\\Starter_Code\\python-challenge\\PyPoll\\resources\\election_data.csv"

# Analyze votes and calculate values
with open(election_data_csv, "r") as file:
    election_reader = csv.reader(file)
    next(election_reader)
    
    # Variables for total number of votes casted and candidates who received votes
    Total_votes = 0
    candidates_voted = {}

    # Iterate through each line in the file
    for line in election_reader:
        ballot_id, county, candidate = line

        # Count total votes
        Total_votes += 1

        # Votes for each candidate
        if candidate in candidates_voted:
            candidates_voted[candidate] += 1
        else:
            candidates_voted[candidate] = 1

# Calculate percentage of votes each candidate won
percent_votes = {}
for candidate, votes in candidates_voted.items():
    percent_votes[candidate] = (votes / Total_votes) * 100

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")
for candidate, votes in candidates_voted.items():
    print(f"{candidate}: {percent_votes[candidate]:.3f}% ({votes})")
print("-------------------------")

# Find the winner based on popular vote
winner = max(candidates_voted, key=candidates_voted.get)
print(f"Winner: {winner}")
print("-------------------------")
