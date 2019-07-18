#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies
import os
import csv


# In[2]:


#Path to collect data from Resources folder
election_csv = os.path.join("..","Homework","PyPoll","electiondata.csv")


# In[4]:


# create variables
candidate_names = []
canvote_count = {}
can_percentage = []
totalvote_count = 0
unique_names = []
percentages = []
win_count = 0
winner = ""


# In[5]:


#Read csv and convert into dictionaries
with open("electiondata.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    #Begin loop
    for row in reader:
        
        #add to total number of votes
        totalvote_count = totalvote_count + 1
        
        #Grab candidate name as you go through rows
        unique_names = row["Candidate"]
        
        #Create conditional statement if candidate name is different than those previous
        if unique_names not in candidate_names:
            
            #Add to the existing list of candidates
            candidate_names.append(unique_names)
            
            #Set candidate's corresponding vote counter to zero and track
            canvote_count[unique_names] = 0
            
        #Add vote to individual candidate's count
        canvote_count[unique_names] = canvote_count[unique_names] + 1


# In[6]:


#Print test
print("Election Results\n")
print("-------------------------------------")
print(f"Total Votes: {totalvote_count}")
print("-------------------------------------")


# In[7]:


#Create output text file
with open ("poll_output.txt","w") as file:
    file.write("Election Results\n")
    file.write("-------------------------------------\n")
    file.write(f"Total Votes: {totalvote_count}\n")
    file.write("-------------------------------------\n")


# In[8]:


#Start loop to find winner and percentages
for unique_names in canvote_count:
    
    #Retrieve vote count and percentage
    ind_vote = canvote_count.get(unique_names)
    can_percentage = float(ind_vote)/float(totalvote_count) * 100
    can_info = f"{unique_names}: {can_percentage:.2f}% {ind_vote}\n"
    
    #Print candidate info (can_info)
    print(can_info)
  
    #Open and append candidate info to text file
    with open ("poll_output.txt","a") as file:
        file.write(can_info)
    
    #Determine winner based on votes
    if(ind_vote > win_count):
        win_count = ind_vote
        winner = unique_names
        
    


# In[9]:


#Print winner info
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")


# In[10]:


#Export winner info to text file
with open ("poll_output.txt","a") as file:
    file.write("-------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------------------\n")


# In[ ]:





# In[ ]:




