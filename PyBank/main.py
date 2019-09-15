# Py Bank
# Doug Watola


import os
import csv
import operator

#Average function that takes a list of numbers
def average(list):
    return sum(list)/len(list)

#Set the path for input budget file
budgetpath = os.path.join("C:/Users/dougw/Python-Challenge/", "budget_1.csv")
#=======================================================
#Read budget csv file and derive sum of profit and average profit
#=======================================================

with open(budgetpath, mode='r', newline='') as budget:
    budgeteval = csv.reader(budget, delimiter=',')
    
    #skip header information
    csv_header=next(budgeteval)
    
    #set empty list for profit calculation
    profit_month=[]
    
    for row in budgeteval:
        profit_month.append(float(row[1]))
                  
    sum_profit=sum(profit_month)
    average_profit=round(average(profit_month),2)

#======================================================
#   Read budget csv to sort to determine the highest and lowest month
#======================================================

with open(budgetpath, mode='r', newline='') as budget2:
    budgeteval2 = csv.reader(budget2, delimiter=',')
    
    csv_header=next(budgeteval2)
    #sort budget
    sorted_budget = sorted(budgeteval2, key=operator.itemgetter(1))
    #Create hightest month and lowest month list
    total_months=len(sorted_budget)
    highest_month=sorted_budget[(len(sorted_budget)-1)]
    
    lowest_month=sorted_budget[0]

#======================================================
#    Write information to an output text file
#======================================================

with open(outPath, mode='w', newline='') as budgetout:
    budgetout.write("Financial Analysis \n" )
    budgetout.write("----------------------- \n" )
    budgetout.write("Total Months: %s \n" % total_months)
    budgetout.write("Total: %s \n" % sum_profit)
    budgetout.write("Average Change: %s \n" % average_profit)
    budgetout.write("Greatest Increase in Profits: %s    ($ %s) \n" %(highest_month[0], highest_month[1]))
    budgetout.write("Greatest Increase in Profits: %s    ($ %s) \n" %(lowest_month[0], lowest_month[1]))
#======================================================
# Print output information in prescribed format
#======================================================

print("Financial Analysis " )
print("----------------------- " )
print("Total Months: %s " % total_months)
print("Total: %s " % sum_profit)
print ("Average Change: %s " % average_profit)
print ("Greatest Increase in Profits: %s    ($ %s) " %(highest_month[0], highest_month[1]))
print ("Greatest Increase in Profits: %s    ($ %s) " %(lowest_month[0], lowest_month[1]))
