import sys

reader=open("Pitching.csv", "r")

line=reader.readline()
# print line
# this should be the headerline
# I could ask where the IPouts is by
#x=line.split()
#y=x.rindex('IPout')
print y
counter=0.0
countLine=0

line=reader.readline()
while line !="":
    l=line.split(',')
    counter+=float(l[12])
    countLine+=1
    line=reader.readline()

reader.close()

print "length of all lines: ", countLine
print "IPouts summed ", counter
print "Average: ", counter/countLine

# or print "length of all lines: ", %d

