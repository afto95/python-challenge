import csv
import os

#Change directory to directory containing currently running python file
CurrentDirectory = os.path.dirname(__file__)
os.chdir(CurrentDirectory)

DataFile = 'budget_data.csv'

#Create objects which can be used later for analysis
Dates = []
ProfitsLosses = []
TotalProfit = 0
ProfitChanges = []
AverageChange = 0
Profits_Dates = {}

#Read csv file and fill Dates and ProfitsLosses with their respective values, also fill dictionary with profit as keys and date as values
with open(DataFile,'r') as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter=',')

    for row in csvreader:
        Dates.append(row['Date'])
        ProfitsLosses.append(row['Profit/Losses'])


#Iterate over all Profits and Losses and get sum
for item in ProfitsLosses:
    TotalProfit = TotalProfit + int(item)

#Find all the changes in profits/losses from month to month and store in list called ProfitChanges
for n in range(len(ProfitsLosses)-1):
    ProfitChanges.append(int(ProfitsLosses[n+1]) - int(ProfitsLosses[n]))
 
#Find average change using ProfitChanges divided by number of profit/losses changes
for item in ProfitChanges:
    AverageChange = AverageChange + item
AverageChange = AverageChange/len(ProfitChanges)

#Find max and min Profit Changes
for i in range(len(ProfitChanges)):
    Profits_Dates[ProfitChanges[i]] = Dates[i+1]

GreatestIncrease = max(ProfitChanges)
GreatestDecrease = min(ProfitChanges)

#Final print statements
print('Financial Analysis')
print('------------------')
print(f'Total Months: {len(Dates)}')
print(f'Total: ${str(TotalProfit)}')
print(f'Greatest Increase in Profits: {Profits_Dates[GreatestIncrease]} (${GreatestIncrease})')
print(f'Greatest Decrease in Profits: {Profits_Dates[GreatestDecrease]} (${GreatestDecrease})')

#Export text file with results
with open('results_PyBank.txt','w') as text:
    text.write('Financial Analysis\n')
    text.write('------------------\n')
    text.write(f'Total Months: {len(Dates)}\n')
    text.write(f'Total: ${str(TotalProfit)}\n')
    text.write(f'Greatest Increase in Profits: {Profits_Dates[GreatestIncrease]} (${GreatestIncrease})\n')
    text.write(f'Greatest Increase in Profits: {Profits_Dates[GreatestDecrease]} (${GreatestDecrease})\n')

