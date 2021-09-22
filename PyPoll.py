#The data we need to retrieve
import csv
import os
#Assign a variable for the file to load and the path.
File_to_Load= os.path.join("Resources", "election_results.csv")
#Assign a filename variable to save the file to a path.
file_to_save=os.path.join("Analysis", "election_analysis.txt")
#Open the election results and read the file
with open(File_to_Load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    print(headers)

#1.The total number of votes cast 
#2.A complete list of canidates who received votes
#3.The percentage of votes each canidate won
#4.The total number of votes each canidate won
#5.The winner of the election based on popular vote
