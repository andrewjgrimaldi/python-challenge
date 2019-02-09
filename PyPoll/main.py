# -*- coding: utf-8 -*-
#"""Andrew_1.ipynb
#
#Automatically generated by Colaboratory.
#
#Original file is located at
#    https://colab.research.google.com/drive/1PQjLz2kaI0YBD63FpGZchH-8HLlOsSUI
#"""
# Dependencies
import csv

# Files to load and output (Remember to change these)
file_to_load = "C:\\Users\\andre\\Desktop\\Data Analysis Class\\Homework 3\\budget_data1.csv"
file_to_output = "C:\\Users\\andre\\Desktop\\Data Analysis Class\\Homework 3\\budget_analysis.txt"

#Jisan note:  the file didn't save as a normal csv so we had to split it using the split method below
#Jisan note:  One instrutor helped me with the first one.  Another with the 2nd one.  

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
total_net = 0
prev_net = 0
  

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
  reader = csv.reader(financial_data)
  
  header = next(reader)
  
#jisan note:  as you will see from other file, the other teacher used a different method for this.  This method: 
#        if index == 0:
#           continue # continue - Keyword that means "skip to next iteration"


  for row in reader:

    # Track the total
    total_months = total_months + 1
    total_net = total_net + int(row[0].split(",")[1])

#jisan note:  this is where we had to do the split because we couldn't download the file correctly.

    # Track the net change
    net_change = int(row[0].split(",")[1]) - prev_net
    prev_net = int(row[0].split(",")[1])
    net_change_list = net_change_list + [net_change]
#jisan note:  we spent a lot of time on this.  the logic was confusing for me. (subtracting out the previous amount to get the change)

#    print(month_of_change)
    month_of_change = month_of_change + [row[0].split(",")[1]]

    # Calculate the greatest increase
    if net_change > greatest_increase[1]:
      greatest_increase[0] = row[0].split(",")[0]
      greatest_increase[1] = net_change

    # Calculate the greatest decrease
    if net_change < greatest_decrease[1]:
      greatest_decrease[0] = row[0].split(",")[0]
      greatest_decrease[1] = net_change

    # Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)

    

# Generate Output Summary
output = (
f"\nFinancial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: ${net_monthly_avg:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

#export to a new file
with open(file_to_output, 'w') as financial_data:
  financial_data.write(output)

#jisan note:  we did this at first in pandas because the csv wasn't splitting like expected becase of the way i downloaded the file
#import pandas as pd  
# df = pd.read_csv(csvpath, sep=",", header=0)
# df.head()
# def split_up(x):
#   return x.split(",")[0]
# def split_up2(x):
#   return x.split(",")[1]
# df['Date'] = df['Date,Profit/Losses'].apply(lambda x: split_up(x))
# df['PL'] = df['Date,Profit/Losses'].apply(lambda x: int(split_up2(x)))
# df = df[['Date','PL']]
#df['PL'].mean()
