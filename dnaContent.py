# 
def nucleotideContent(dnaString):    
    '''This function must return the contribution of 
    nucleotides ATCG (as uppercase) from a given DNA     
    string inside a dictionary, where each key refers to 
    a nucleotide'''    
    dnaDict = {}  # create an empty dictionary to store results  
    uniques=set(dnaString)    
    for nucleotide in uniques:    
        dnaDict[nucleotide]=dnaString.count(nucleotide)    
    
    return dnaDict






