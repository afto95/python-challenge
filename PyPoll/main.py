import csv 

file = ('D:\\Github - Cloned Repositories\\python-challenge\\PyPoll\\election_data.csv')

Votes = []
CandidateVotesDict = {}

#Open and read csvfile, then place all votes in "Votes" as a list.
with open(file,'r') as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter=',')

    for row in csvreader:
        Votes.append(row['Candidate'])

#Find Total Votes and make a set using "Votes" to determine all candidates that received votes.
TotalVotes = len(Votes)
Candidates = set(Votes)

#Determine percentage of votes for each candidate and make a list of all votes for each candidate. Use this list to find winner.
CandidateVotes = []
for candidate in Candidates:
    NumberVotes = Votes.count(candidate)
    CandidateVotesDict[NumberVotes] = candidate
    CandidateVotes.append(NumberVotes)

Winner = CandidateVotesDict[max(CandidateVotes)]

#Print final results
print('Election Results')
print('----------------------')
print(f'Total Votes: {len(Votes)}')
print('----------------------')
for votes,candidate in sorted(CandidateVotesDict.items(),reverse=True):
    print(f'{candidate}: {int((int(votes)/TotalVotes)*100)}% ({votes})')
print('----------------------')
print(f'Winner: {Winner}')
print('----------------------')

#Export text file with results
with open('results_PyPoll.txt','w') as text:
    text.write('Election Results\n')
    text.write('----------------------\n')
    text.write(f'Total Votes: {len(Votes)}\n')
    text.write('----------------------\n')
    for votes,candidate in sorted(CandidateVotesDict.items(),reverse=True):
        text.write(f'{candidate}: {int((int(votes)/TotalVotes)*100)}% ({votes})\n')
    text.write('----------------------\n')
    text.write(f'Winner: {Winner}\n')
    text.write('----------------------')