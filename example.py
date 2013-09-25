import sys
# print sys.argv

# print a
b=sys.argv[1:]; b.sort()
#
# newB=[b[0][0].upper()+b[0][1:], b[1][0].upper()+b[1][1:], b[2][0].upper()+b[2][1:]]
#
# alternatively I could have use capitalize
#
newB= [b[0].capitalize()]# ,b[1].capitalize(),b[2].capitalize()]

print(newB[0]+", "+newB[1]+ " " +"and "+ newB[2]+ ".")

# now one should actually done this 

newB= ", ".join(b[0:-1])



