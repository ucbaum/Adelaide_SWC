def dna_start_with(SeqInput, seq2):
    if SeqInput.startswith(seq2):
        return True
    else:
        return False

tests =[['a','a',True],['ct','c',True]]  
#dnaTest=dna_start_with("actgttg",'agt')
# print dnaTest

# Run and report
passes=0 
for (i, (seq,prefix,expected)) in enumerate(tests):
    print i, seq, prefix, expected


  
