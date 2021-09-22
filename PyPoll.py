#Copied from https://stackoverflow.com/questions/18589146/how-to-use-encoding-utf-8-py-instead-of-cp1252-py-in-python
#The data we need to retrieve
import csv
File_to_Load='Resources\\election_results.csv'
with open(File_to_Load) as election_data:
#1.The total number of votes cast
#2.A complete list of canidates who received votes
#3.The percentage of votes each canidate won
#4.The total number of votes each canidate won
#5.The winner of the election based on popular vote
    print(election_data)  
    