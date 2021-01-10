import csv
import os
from statistics import mean 

csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join('Analysis','results.csv')

total_months = 0
total_amount = 0
monthly_statement = []
GIP_month = []

with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    header = next(data)

    #lets go through each row and extract some data...
    for row in data:
        #get the total number of months by counting each row of column 1
        total_months = total_months + row.count(row[0])
        #get the total sum of amount by adding each row of column 2
        total_amount = total_amount + int(row[1])
        #create a list with the amount for each month
        monthly_statement = monthly_statement + row
    
    #turn monthly_statement list into a dictionary
    dictionary_statement = dict([(k,int(v)) for k,v in zip (monthly_statement[::2], monthly_statement[1::2])])
    #get all the value and keys from the statement
    amount = list(dictionary_statement.values())
    dates = list(dictionary_statement.keys())
    #subtract the next amount from the previous amount to get the profit/loss
    PnL = [y - x for x, y in zip(amount, amount[1:])] #PnL shortcut for Profit and Loss
    
    #now that we have all the profit and loss, let's get the average
    average = round(mean(PnL),2)
    
    #let's build a new dictionary called monthy_PnL with date and PnL
    monthly_PnL = {dates[i]: PnL[i] for i in range(len(PnL))}
    #then we'll get the GIP (Greatest Increase Profit) and GDP (Greatest Decrease Profit) by sorting the value from the monthly_PnL
    GIP = max([i for i in monthly_PnL.values()])
    GIP_month = list(monthly_PnL.keys())[list(monthly_PnL.values()).index(GIP)]
    GDP = min([i for i in monthly_PnL.values()])
    GDP_month = list(monthly_PnL.keys())[list(monthly_PnL.values()).index(GDP)]
    
    #enter all the variables in the output statement
    output = (f'''
    Financial Analysis
    -----------------------------
    Total Months: {total_months}
    Total: ${total_amount}
    Average Change: ${average}
    Greatest Increase in Profits: {GIP_month} ({GIP})
    Greatest Decrease in Profits: {GDP_month} ({GDP})''')
    
    print(output)
with open(output_path, "w") as txt_file:
    txt_file.write(output)