#The data we need to retrieve
File_to_Load='\Resources\election_results.csv'
with open(File_to_Load) as election_data:
#1.The total number of votes cast
#2.A complete list of canidates who received votes
#3.The percentage of votes each canidate won
#4.The total number of votes each canidate won
#5.The winner of the election based on popular vote
    print(election_data)