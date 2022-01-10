# write tests for parsers
import sys
sys.path.append('~/seqparser')
##This looks for the module in the seqparser folder

from parse import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    parser_obj = FastaParser("/Users/anaalmonte/Documents/Algorithms/project1/data/test.fa")
    seq_out=[]
    for record in parser_obj:
        seq_out.append(record)
    assert seq_out[0]==('>seq0', 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA')


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    parser_obj = FastqParser("/Users/anaalmonte/Documents/Algorithms/project1/data/test.fq")
    seq_out=[]
    for record in parser_obj:
        seq_out.append(record)
    assert seq_out[99] == ('@seq99', 'CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG', '2$7)*5:"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0":02"0=!0#/>+*1$1$39!.8+9<\'1$*1$321&<\'&9,)2')

