# gc content
# base_count("G")
# reverse complement

class DNAString:
    def __init__(self,seqString):
    # this is the initializer
        self.seqString=seqString

    def GCContent(self):
        g = self.baseCount('G')
        c = self.baseCount('C')
        return float(g+c)/len(self.seqString)

    def baseCount(self,base):
    # should return a dictionary with base counts
        return self.seqString.count(base) 


    def revComp(self):
        # now complement
        revC=''
        base_complement={'G':'C','C':'G','A':'T','T':'A'}
        for base in self.seqString:
            revC=base_complement[base]+revC   
            # I'm reversing simulatenously  
        return revC
            


