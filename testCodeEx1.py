Tests= [
 ['AGTCTG', {'A':1,'C':1,'G':2,'T':2}],
 ['CCC',   {'A':'','C':3,'G':'','T':''}],
 ['GGTT', {'A':0,'C':0,'G':2,'T':2}],
 ['gaatt', {'A':0,'C':0,'G':0,'T':0}]
]

# Run and report    
passes = 0    
for (i, (seq, expected)) in enumerate(Tests):    
    if nucleotideContent(seq) == expected:    
        passes += 1    
    else:    
        print 'test %d failed' % i

print '%d/%d tests passed' % (passes, len(Tests))

# I just add another test line
