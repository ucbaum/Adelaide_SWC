import sys

seqCounter=0
N=0
Gc=0.0


def do_stats (DNAstring):
    Nc=DNAstring.count('N') 
    s=DNAstring.replace('N',"")
    gcount=s.count('G')
    ccount=s.count('C')
    if gcount+ccount<>0:
        GCtotal = float(len(s)/float(gcount+ccount))
    else:
        GCtotal= 0
    return Nc, GCtotal

reader=open("fastEx2.txt", "r")
line=reader.readline()
print line

while line != '':
    #check whether fasta first line
    if line.startswith('>'):
        #read sequence and do the calculation
        seqCounter+1
        seqName=line.rstrip()
        SeqLine=reader.readline()
        N,Gc = do_stats(SeqLine)
    else:
        print"something wrong with your file"
    line=reader.readline()
        
    print seqName, 'Number of Ns: ',N, 'GCcontent: ' , Gc





