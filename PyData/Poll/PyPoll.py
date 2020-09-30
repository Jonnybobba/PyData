# Define modules 
import os
import csv


# Initialize winning variables
winner = ""
winner_count = 0

# Open Py_Poll_Data.csv and read
with open('Poll/Py_Poll_Data.csv') as csv_file:
    # Seperate by ,
    csvreader = csv.reader(csv_file, delimiter = ',')
    header = next(csvreader)
    # Initialize results
    total = 0
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Tooley_count = 0
    # For loop counting votes and adding total
    for row in csvreader:
        total = total + 1
        # Pull data from csv
        ID = float(row[0])
        county = str(row[1])
        Candidate = str(row[2])

        # If condtional seperating votes by candidate
        if (Candidate == "Khan"):
            Khan_count = Khan_count + 1
        elif (Candidate == "Correy"):
            Correy_count = Correy_count + 1
        elif (Candidate == "Li"):
            Li_count = Li_count + 1
        elif (Candidate == "O'Tooley"):
            Tooley_count = Tooley_count + 1
        else:
            print(f"{Candidate} didn't win")

# Equation to calculate % of vote
Khan_percent = "{:.3%}".format(Khan_count / total)
Correy_percent = "{:.3%}".format(Correy_count / total)
Li_percent = "{:.3%}".format(Li_count / total)
Tooley_percent = "{:.3%}".format(Tooley_count / total)

# If conditional to write out winner
if (Khan_count > Correy_count) and (Khan_count > Li_count) and (Khan_count > Tooley_count):
    winner ="Khan"
elif(Correy_count > Li_count) and (Correy_count > Tooley_count):
    winner ="Correy"
elif(Li_count > Tooley_count):
    winner = "Li"
else:
    winner = "O'Tooley"

# Export data to Terminal
print(f'Election Results')
print('--------------------------------------')
print(f'Total Votes: {total}')
print('--------------------------------------')
print(f'Khan: {Khan_percent} ({Khan_count})')
print(f'Correy: {Correy_percent} ({Correy_count})')
print(f'Li: {Li_percent} ({Li_count})')
print(f"O'Tooley: {Tooley_percent} ({Tooley_count})")
print('--------------------------------------')
print(f'Winner: {winner}')

#Export data to file pypoll_results.txt
Export = open(r"output/pypoll_results.txt","w")
Export.write(f'Election Results\n')
Export.write('--------------------------------------\n')
Export.write(f'Total Votes: {total}\n')
Export.write('--------------------------------------\n')
Export.write(f'Khan: {Khan_percent} ({Khan_count})\n')
Export.write(f'Correy: {Correy_percent} ({Correy_count})\n')
Export.write(f'Li: {Li_percent} ({Li_count})\n')
Export.write(f"O'Tooley: {Tooley_percent} ({Tooley_count})\n")
Export.write('--------------------------------------\n')
Export.write(f'Winner: {winner}')

        
        