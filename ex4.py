import sys

a=int(sys.argv[1])

if (a % 2) > 0:
    print("number is uneven")
else:
    print ("number is even")


if a >0 and a<100:
    print ("number is between zero and hundred")

if a <0 or a>100:
    print("number is either below zero or above 100")

