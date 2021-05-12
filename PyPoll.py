<<<<<<< HEAD
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize the total vote counter and set to 0.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare empty dictionary for candidate vote tally.
candidate_votes = {}

# Declare winning Candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
            
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any exisitng candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking candidate's votes.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve the vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percent of votes to the terminal.

    # Determine winning vote count and candidate.

    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
=======
# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load=os.path.join("resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file.
# election_data = open(file_to_load,'r')
with open(file_to_load) as election_data: 
    
    # To do: Read and analyze data here.
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    




# Get the total number of votes cast
# Create a complete list of candidates who received votes
# Sum the total number of votes each candidate received
# Calculate the votes each candiate won
# Determine who is the winner based on the highest percent of population
>>>>>>> c91120b (uploading analysis)