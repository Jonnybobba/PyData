# Define modules
import os
import csv


# Open Py_Bank_Data.csv and read
with open('Bank/Py_Bank_Data.csv') as csv_file:
    # Seperate by ,
    csvreader = csv.reader(csv_file, delimiter = ',')
    header = next(csvreader)
    # Initialize results
    months = 0
    total = 0
    big_change = 0
    big_time = ""
    little_change = 0
    little_time = ""

    # For loop counting months and adding total
    for row in csvreader:
        months = months + 1
        # Pull data from csv
        time = str(row[0])
        change = float(row[1])
        
        total = total + change
        
        # If conditional finding max increase and max decrease
        if (change >= big_change):
            big_change = change
            big_time = time
        elif(change <= little_change):
            little_change = change
            little_time = time  
    #Equation to find average change    
    avg_change = total / months
    avg_change = format(avg_change, ',.2f')
    
# Export data to Terminal
print("")
print(f'Financial Analysis')
print(f'-------------------------------')
print(f'Total Months: {months}')
total = format(total, ',.2f')
print(f'Total: ${total}')
print(f'Average Change: ${avg_change}')
big_change = format(big_change, ',.2f')
print(f'Greatest Increase in Profits: {big_time} ({big_change})')
little_change = format(little_change, ',.2f')
print(f'Greatest Decrease in Profits: {little_time} ({little_change})')


# Export data to file pybank_results.txt
Export = open(r"output/pybank_results.txt","w")

Export.write(f'Financial Analysis \n')
Export.write(f'-------------------------------\n')
Export.write(f'Total Months: {months}\n')
Export.write(f'Total: ${total}\n')
Export.write(f'Average Change: ${avg_change}\n')
Export.write(f'Greatest Increase in Profits: {big_time} ({big_change})\n')
Export.write(f'Greatest Decrease in Profits: {little_time} ({little_change})')
