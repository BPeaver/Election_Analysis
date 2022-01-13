# The data we need to retrieve.
#1. Total number of votes cast
#2. List of candidates who received votes
#3. % of votes each candidate won
#4. Total number of votes each candidate won
#5. Election winner based on popular vote

# Assign a variable for the file to load and the path
#file_to_load = 'Resources\election_results.csv'

# Open election results and read the file.
# LONG WAY => election_data = open(file_to_load, 'r')
# SHORTER WAY, replace "open()" function with "with" statement
#with open(file_to_load) as election_data:

    #To do: perform analysis.
    #print(election_data)

# Close the file
#election_data.close()

# Add our dependencies
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    #print(election_data)

# Create filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open() function with the "w" mode to write data to the file
#open(file_to_save, "w")

# Create filename variable to direct/indirect path to the file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open file as text w/ open()
#outfile = open(file_to_save, "w")
# Write some data to the file
#outfile.write("Hello World")
# Close file
#outfile.close()

# THIS IS CLEANER CODE
# Create filename variable to direct/indirect path to file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Use 'with' statement to open file as text file
#with open(file_to_save, "w") as txt_file:

        #Write data to the text file
        #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

#Add dependencies
import csv
import os
#Assign Variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign Variable to save file to path
file_to_save = os.path.join("Analysis", "election_results.txt")

#Set accumulator variable
total_votes = 0
#Declare a new list
candidate_options = []
#Declare empty dictionary for candidate votes
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #Increment total_votes by 1
        total_votes += 1
        #Print candidate name from each row
        candidate_name = row[2]
        #Add candidate name does not match existing name, add to candidate list variable
        if candidate_name not in candidate_options:
            #Add it to list 
            candidate_options.append(candidate_name)
            #Start tracking candidate vote count
            candidate_votes[candidate_name] = 0
        #Add votes to candidate's count
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------\n"
            )
        print(election_results, end="") 
        txt_file.write(election_results)

    #Determine % of votes for each candidate by looping through the counts
    #Iterate through candidate list
        for candidate_name in candidate_votes:
            #Retrieve vote count of candidate
            votes = candidate_votes[candidate_name]
            #Calculate the % of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            #Determine winning vote count and candidate
            #Determine if the votes is greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #And, set the winning_candidate = to candidate's name
                winning_candidate = candidate_name

            #To Do: print out each candidate's name, vote count, and % of votes to terminal
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
           

        winning_candidate_summary = (
            f"-----------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------\n")   
        print(winning_candidate_summary)
        
        
        
        # Save the winning candidates results to text file
    
        txt_file.write(winning_candidate_summary)

