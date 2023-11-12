import os
import csv
#calling csv file and passing to filepath variable
filepath=os.path.join(os.getcwd(),"Resources","budget_data.csv")

with open(filepath) as f: 
    #skip the first row of the file
    next(f)
    # CSV reader specifies delimiter and variable that holds contents
    data=list(csv.reader(f,delimiter=","))
    
   #Reading first to last row of the data through looping
    for i in range(len(data)):
        if i != len(data)-1:
            #calculating the closing balace- opening balance, Passed the index value
            pnl=int(data[i+1][1])-int(data[i][1])
            #inserting all the row in variable named pnl and assign to list
            data[i+1].insert(2,pnl)
    #handling the forst row value as closing balance for first month should be 0   
    data[0].insert(2,0)
    #intialised  the variable to handle the calculation for sum, greastest increase and decrease
    plsum=0
    grtchange=[]
    avgchange=0
    
    #looping to read all the value in index 0
    for i in range(len(data)):
        #sum up the all no by reading and add up every time
        plsum += int(data[i][1])
        avgchange +=int(data[i][2])
      
    #Displaying all the records as per project results assignment
    with open('Financial_Analysis.txt', 'w') as f:
        f.writelines("Financial Analysis \n")
        print("Financial Analysis") 

        f.writelines("-------------------------------------------------------- \n")
        print("--------------------------------------------------------")   
        
        f.writelines(f"Total Months : {len(data)} \n")
        print("Total Months :", len(data))
        
        f.writelines(f"Total : $ plsum \n")
        print("Total : $",plsum)
        
        f.writelines(f"Average Change: {round(avgchange/(len(data)-1),2)} \n")
        print("Average Change:",round(avgchange/(len(data)-1),2))
    
        maxpl = max(data, key=lambda x: x[2])
        minpl = min(data, key=lambda x: x[2])

        f.writelines(f"Greatest Increase in Profits : {maxpl[0]} ($ {maxpl[2]} ) \n")
        print(f"Greatest Increase in Profits : {maxpl[0]} ($ {maxpl[2]} )")
        
        f.writelines(f"Greatest Decrease in Profits : {minpl[0]} ($ {minpl[2]} ) \n")
        print(f"Greatest Decrease in Profits : {minpl[0]} ($ {minpl[2]} )")
        f.close()