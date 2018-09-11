'''
#A script to find attributes for data samples. The resulting list may be used later to find patterns in the data. 

Usage: >python acollector.py "[file data entry names]" "[data file]" "[the column number of the desired attribute data]" "[separator in data file]"
Example: python acollector.py "example/townlist.txt" "example/weather.csv" "6" ","

To put the results in a text file: python acollector.py "example/townlist.txt" "example/weather.csv" "6" "," > results.txt
'''

import sys

#Set some variables from the terminal input
listfile=sys.argv[1]
tablefile=sys.argv[2]
thecolumn=int(sys.argv[3])
theseparator=sys.argv[4]

#Python counts from zero, therefore the column number needs to be reduced by one. 
thecolumn=thecolumn-1

#Prepare a list for the data
thedata=[]
namelist=[]

#Open the list file to read it
fileopen = open(listfile,'r')

#Read the list from the file.
for row in fileopen:
    #First, remove the newline (\n) from the text. They will mess with display and possibl
    line=row.strip()
    #Make a 2-d list, with the names from the file and an empty column next to it.
    namelist.append([line,""])

#Close the fileopen
fileopen.close()

#For every name in the list, find their attributes from the datafile. 
for i in range(len(namelist)):
    #Open the data table to read it
    fileopen = open(tablefile,'r')
    
    for row in fileopen:
        #Split the line with the separator, given by the user. 
        tableline=row.split(theseparator)

        #Check if this row has our element. Then we can add the attribute, in a semicolon-separated manner. 
        if namelist[i][0] in tableline:
                    #Get rid of newlines.
                    tableline[thecolumn]=tableline[thecolumn].strip()
                    #Add the attribute from the data table. 
                    namelist[i][1]=namelist[i][1]+";"+tableline[thecolumn]
        
    fileopen.close()

    #Remove redundant elements
    temporary=namelist[i][1].split(';')
    temporary=set(temporary)
    temporary=list(temporary)
    #Remove first element
    temporary=temporary[1:]
    #Convert to semicolon-separated format and add to the main list.
    namelist[i][1]=";".join(temporary)
    
#Print out the results
for entry in namelist:
    print(entry[0]+','+entry[1])
