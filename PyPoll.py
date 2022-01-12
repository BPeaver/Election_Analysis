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

#Open election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze data here
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    print(headers)