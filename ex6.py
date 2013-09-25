import sys

reader=open('fruits.txt', 'r')
line= reader.readline()

print line

while line!="":
    print line
    line=reader.readline()

iter = 0
while iter<10:
    iter+=1
    print iter

