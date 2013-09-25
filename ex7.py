import sys

reader=open("pg76.txt", "r")
line=reader.readline()
# print line
countLine=0
countLength=0

while line !="":
    countLine+=1
    countLength+=len(line)
    line=reader.readline()

reader.close()

print "length of all lines: ", countLength
print "Number of lines: ", countLine

# or print "length of all lines: ", %d

