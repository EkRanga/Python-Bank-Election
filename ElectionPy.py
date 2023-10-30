import os
import csv
result=[]
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
 
    # CSV reader specifies delimiter and variable that holds contents
      csvreader = list(csv.reader(csvfile, delimiter=','))

#assign the variablr foe each candidate for total vote count
charlscount=0
dianascount=0
raymonscount=0

#Looping through all each candidate and adding every vote for total vote count
for row in csvreader:
    
    if row[2] == "Charles Casper Stockham" :
       charlscount +=1
      
    elif row[2] == "Diana DeGette" :
                dianascount +=1

    elif row[2] == "Raymon Anthony Doane" :
                 raymonscount +=1

# Every single vote appending in variable for final vote count number
result.append(["Charles Casper Stockham",charlscount])
result.append(["Diana DeGette",dianascount])
result.append(["Raymon Anthony Doane",raymonscount])
winner=max(result,key=lambda x:x[1])

#Displaying the results as per project display Requirement
Totalvote=len(csvreader)-1
print("Election Results")
print("-----------------------------")
print("Total Votes: ",Totalvote )
print("-----------------------------")
print(f"Charles Casper Stockham: {round((charlscount/Totalvote)*100,4)}% ({charlscount})") 
print(f"Diana DeGette: {round((dianascount/Totalvote)*100,4)}% ({dianascount})") 
print(f"Raymon Anthony Doane: {round((raymonscount/Totalvote)*100,4)}% ({raymonscount})") 
print("-----------------------------")

print("Winner: ", winner[0])


  