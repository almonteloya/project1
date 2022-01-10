def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    rna=""
    for i in seq:
        if i not in 'ATGC':
            rna = "Invalid Input"  ##only accepts ATGC as a input 
            break
        ##builds a rna string by concataning each letter
        if i == 'A':
            rna += 'U'
        elif i == 'C':
            rna += 'G'
        elif i == 'T':
            rna += 'A'
        else:
            rna += 'C'
    return(rna)



def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    ##calls trasncribe function
    ## Then reverse the string using slicing
    reverse=transcribe(seq)
    reverse=reverse[::-1]
    return(reverse)