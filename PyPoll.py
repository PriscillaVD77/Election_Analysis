#The data we need to retrieve
import csv
import os
#Assign a variable for the file to load and the path.
File_to_Load= os.path.join("Resources", "election_results.csv")
#Assign a filename variable to save the file to a path.
file_to_save=os.path.join("Analysis", "election_analysis.txt")
#Initialize a total vote counter.
total_votes= 0
#candidate options
Candidate_options = []
#declare empty dictionsary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(File_to_Load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #2.Add to the total vote count
        total_votes +=1
        #prints the candidates name from each row.
        candidate_name = row[2]
        #Add candidates name to the candidate list.
        if candidate_name not in Candidate_options:
            Candidate_options.append(candidate_name)
            #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        #add votes to candidates count
        candidate_votes[candidate_name] +=1
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
            #retrieve vote count of a candidate
        votes= candidate_votes[candidate_name]  
            #calculate the percentages of votes.
        vote_percentage = float(votes)/float(total_votes) * 100
         #print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% {votes:,})\n")
        #print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        #save candidate results to text file
        txt_file.write(candidate_results)   
        #determing winning vote count and candidate
        #determine if votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage> winning_percentage):
            #if true then set winning_count = votes and winning_percent= vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to candidate name
            winning_candidate = candidate_name

    winning_candidate_summary = (
            f"---------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

