# import modules
import os
import csv 

# import budget
csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# define variables
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
                 

# calculate total months     
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    
 # calculate total revenue
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    

 # calculate average change monthly
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # adjust for profit loss
        revenue_change.append(profit_loss)
        Total = sum(revenue_change)
        monthly_change = Total / len(revenue_change)
        monthly_change = round(monthly_change,2)  
#Greatest Increase
        profit_increase = max(revenue_change)
        k = revenue_change.index(profit_increase)
        month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total Months: " + str(len(month)))
print("Total Revenue: $ " + str(total_revenue))
print("Average Change: $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")