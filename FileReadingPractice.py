# File Reading Practice
# Matthew Christie
# First Commit 05/06/2019

            #Notes#
#of = open("OpenFile.txt", "r") #"w" for write, "a" for append, "r" for reading
#print(of.read())                    #read full file
#of.close    #Remember to close File after use

#print(of.read())           #Print 1-Big-String
#print(of.readline())       #printline 1
#print(of.readline(5))      #print 5 characters of line 3

#print(of.readlines())      #Returns a list of lines



array = []

with open("FileReadingList.txt", "r") as f:
    display = f.readlines()

print(display[5])

#of = open("FileReadingList.txt", "r")



for display in array:
    print(display)


display = (of.readlines())

#print(display)

#of.close("FileReadingList.txt")         # Closes File after use
