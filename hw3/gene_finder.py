# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Doyung Lee
"""


# you may find it useful to import these variables (although you are not required to use them)
import random
from amino_acids import aa, codons



def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    codon_strand = []
    for i in xrange(0, len(dna), 3): #this for loop steps by 3.
        codonSeq = dna[i:i+3] #takes a set of three dna pieces into codonSeq
        for j in range(len(codons)):
            if codonSeq in codons[j]: #checks if the codonSeq (M, R, A, etc. is a codon list)
                codon_strand.append(aa[j])
    codon_strand = collapse(codon_strand) #turns codon_strand list into a string
    return codon_strand #returns the amino acid sequence from the dna 
            
        

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    inputDNA = raw_input("input: ", )
    expected_output = raw_input("expected output: ", )
    actual_output = coding_strand_to_AA(inputDNA) #calls the coding_strand_to_AA method with the inputDNA
    print "actual output: ", actual_output
    if actual_output == expected_output: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    reverse_dna = dna[::-1] #handy dandy python way of reversing a string.
    comp_reverse_dna = []
    for i in xrange(0, len(reverse_dna)):
        if reverse_dna[i] == 'G':
            comp_reverse_dna.append('C')
        if reverse_dna[i] == 'T':
            comp_reverse_dna.append('A')
        if reverse_dna[i] == 'C':
            comp_reverse_dna.append('G')
        if reverse_dna[i] == 'A':
            comp_reverse_dna.append('T')
    comp_reverse_dna = collapse(comp_reverse_dna)
    return comp_reverse_dna

    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    inputDNAseq = raw_input("input: ", )
    expected_output_seq = raw_input("expected output: ", )
    actual_output_seq = get_reverse_complement(inputDNAseq) #calls the get_reverse_complement() method with the inputDNAseq
    print "actual output: ", actual_output_seq
    if actual_output_seq == expected_output_seq: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    final_codonSeq = []
    for i in xrange(0, len(dna), 3): #this for loop steps by 3.
        codonSeq = dna[i:i+3] #takes a set of three dna pieces into codonSeq
        if codonSeq <> 'TAG' and codonSeq <> 'TAA' and codonSeq <> 'TGA':
            final_codonSeq.append(codonSeq)
        else:
            break #if it is any of the three sequences, it means it's a stop codon. Stop going through the loop.
    final_codonSeq = collapse(final_codonSeq) #turns sequence into a string
    return final_codonSeq #returns the dna sequence from the start righ to the end

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    inputDNAseq = raw_input("input: ", )
    expected_output_seq = raw_input("expected output: ", )
    actual_output_seq = rest_of_ORF(inputDNAseq) #calls the rest_of_ORF() method with the inputDNAseq
    print "actual output: ", actual_output_seq
    if actual_output_seq == expected_output_seq: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false
               
def find_all_ORFs_oneframe(j, dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        j: move frames from the beginning (0, 1, 2)
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    final_codonSeq = []
    list_of_seq = []
    dna1 = dna 
    j1 = j
    while dna[j1: j1+3] <> 'ATG': #this just makes sure what we start with is ATG.
        dna1 = dna[j1+3::]
        j1 += 3
        if j1 > len(dna):
            break
    
    for i in xrange(0, len(dna1), 3): #this for loop steps by 3.
        codonSeq = dna1[i:i+3] #takes a set of three dna pieces into codonSeq        
        if codonSeq <> 'TAG' and codonSeq <> 'TAA' and codonSeq <> 'TGA': #if it's not a stop codon, add the codon.
            final_codonSeq.append(codonSeq)
            #print "if: ", final_codonSeq
        else:
            final_codonSeq1 = collapse(final_codonSeq) #turns sequence into a string
            final_codonSeq = []
            #print "else: ", final_codonSeq1
            if final_codonSeq1[0:3] == 'ATG': #if this sequence has a start codon, keep it.
                list_of_seq.append(final_codonSeq1)
            #if it is any of the three sequences, it means it's a stop codon. Add this to the list.
    if len(final_codonSeq) <> 0 and final_codonSeq[0] == 'ATG': #this checks the last ever segment of the sequence. If it's not zero and has start codon, keep it.
        final_codonSeq = collapse(final_codonSeq)
        list_of_seq.append(final_codonSeq)
        
    return list_of_seq #returns the list of sequences.
    
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    inputDNAseq = raw_input("input: ", )
    expected_output_seq = raw_input("expected output: ", )
    actual_output_seq = find_all_ORFs_oneframe(0, inputDNAseq) #calls the find_all_ORFs_oneframe method with the inputDNAseq
    print "actual output: ", actual_output_seq
    if actual_output_seq == expected_output_seq: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    no_move = find_all_ORFs_oneframe(0, dna)
    move_one = find_all_ORFs_oneframe(1, dna)
    move_two = find_all_ORFs_oneframe(2, dna)    
    return no_move + move_one + move_two

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    
    inputDNAseq = raw_input("input: ", )
    expected_output_seq = raw_input("expected output: ", )
    actual_output_seq = find_all_ORFs(inputDNAseq) #calls the find_all_ORFs_oneframe method with the inputDNAseq
    print "actual output: ", actual_output_seq
    if actual_output_seq == expected_output_seq: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    first_way = find_all_ORFs(dna) #find the ORFs in the original direction
    reverse_dna = get_reverse_complement(dna) #get the reverse complementary strand
    other_way = find_all_ORFs(reverse_dna) #find the ORFs in the reverse complementary direction
    return first_way + other_way

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    inputDNAseq = raw_input("input: ", )
    expected_output_seq = raw_input("expected output: ", )
    actual_output_seq = find_all_ORFs_both_strands(inputDNAseq) #calls the find_all_ORFs_both_strands method with the inputDNAseq
    print "actual output: ", actual_output_seq
    if actual_output_seq == expected_output_seq: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    longest_ORF_strand = max(find_all_ORFs_both_strands(dna), key=len)
    return longest_ORF_strand

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    inputDNAseq = raw_input("input: ", )
    expected_output_seq = raw_input("expected output: ", )
    actual_output_seq = longest_ORF(inputDNAseq) #calls the longest_ORF method with the inputDNAseq
    print "actual output: ", actual_output_seq
    if actual_output_seq == expected_output_seq: #checks if the expected and the actual outputs are the same
        true_false = True
    else:
        true_false = False 
    print "Did actual and expected outputs match?: ", true_false

def longest_ORF_noncoding(dna, num_trials): #got 831 as the longest ORF noncoding.
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    longest_ORF_list = []
    for i in range(num_trials): #number of trials
        dna_list = dna.split() #turn into list
        random.shuffle(dna_list) 
        number = len(longest_ORF(collapse(dna_list))) #get the length of the longest_ORF
        longest_ORF_list.append(number) #add the number
    max_number = max(longest_ORF_list)
    return max_number

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    list_of_threshold_aa = []    
    list_of_dna = find_all_ORFs_both_strands(dna)
    for i in range(len(list_of_dna)):
        if len(list_of_dna[i]) >= threshold:
            amino_acid = coding_strand_to_AA(list_of_dna[i])
            list_of_threshold_aa.append(amino_acid)
    print list_of_threshold_aa
    return list_of_threshold_aa
    
    
    