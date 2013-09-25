
Class UnknowBaseException(Exception):
    pass
    


def dna_starts_with(SeqInput,tSeq):
    '''EXPLANATIONS 
    >>> dna_starts_with('tggt','t')
    True
    >>> dna_starts_with('ATG','ATG')
    True
    >>> dna_starts_with('ggtgcc','1')
    False
    >>> dna_starts_with('GAATTC',' ')
    False
    '''

    if tSeq=
    if SeqInput.startswith(tSeq):
        return True
    else:
        return False
 
if __name__=='__main__':
    import doctest
    doctest.testmod()


