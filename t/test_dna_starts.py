def dna_starts_with(SeqInput,tSeq):
    if SeqInput.startswith(tSeq):
        return True
    else:
        return False



def test_dna_starts_with_correct():
    st1='AGT'; st2="AGTAAAA"
    return st1[0:len(st2)]==st2

def test_dna_starts_with_itself():
    dna="ATGTGTG"
    assert dna_starts_with(dna,dna)

def test_dna_starts_with_one():
    assert dna_starts_with('tgggt','t')

def test_dna_starts_with_letter():
    assert not dna_starts_with('ggtgcc','1')

def test_dna_starts_with_emptyString():
    assert not dna_starts_with('GAATTC',' ')


