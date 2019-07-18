#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import dependencies
import os
import csv


# In[5]:


#specify path for file
budget_data = os.path.join("..","Homework","PyBank","budget_data.csv")


# In[6]:


#Create variables for placeholders
total_months = []
net_profit = []
monthly_change = []


# In[7]:


#Open and read CSV file
with open("budget_data.csv", newline = "") as csvfile:
    reader = csv.reader(csvfile,delimiter =",")
    
    #Read header
    header = next(reader)
    
    #Start initial loop for net profit and total total total months
    for row in reader:

        #Append net_profit and total_months to correct lists
        total_months.append(row[0])
        net_profit.append(int(row[1]))
        
    #Start loop to get profit change by month
    for i in range(len(net_profit)-1):

        #Find difference between every two months and append to monthly_change variable
        monthly_change.append(net_profit[i+1]-net_profit[i])

#Calculate average monthly change in profits
Ave_Change = round((sum(monthly_change)/len(monthly_change)),2)


# In[8]:


#Find biggest increase and decrease in list of monthly_change
max_increase = max(monthly_change)
max_decrease = min(monthly_change)


# In[9]:


#Pull up corresponding dates for max increase and decrease
max_increase_m = monthly_change.index(max(monthly_change)) + 1
max_decrease_m = monthly_change.index(min(monthly_change)) - 1


# In[10]:


#Print Financial Analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total:${sum(net_profit)}")
print(f"Average Change:${(Ave_Change)}")
print(f"Greatest Increase in Profits:{total_months[max_increase_m]}(${(str(max_increase))})")
print(f"Greatest Decrease in Profits:{total_months[max_decrease_m]}(${(str(max_decrease))})")


# In[11]:


#Create output text file
with open ("bank_output.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total:${sum(net_profit)}\n")
    file.write(f"Average Change:${(Ave_Change)}\n")
    file.write(f"Greatest Increase in Profits:{total_months[max_increase_m]}(${(str(max_increase))})\n")
    file.write(f"Greatest Decrease in Profits:{total_months[max_decrease_m]}(${(str(max_decrease))})\n")


# In[ ]:




