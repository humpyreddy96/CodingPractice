#Approach 1 
#Take two indexes 
#1. Array Index = 0 and Sequence Index =0
#Increment the array index for every iteration and only increment the sequence index for a match.

from typing import Sequence


def isValidSubsequence(array,sequence):
    arrIndex = 0
    seqIndex = 0
    while arrIndex<len(array) and seqIndex<len(sequence):
        if sequence[seqIndex] == array[arrIndex]:
            seqIndex +=1
        arrIndex +=1
    return seqIndex == len(sequence)

#Approach 2
#using a for loop

def isValidSubsequence1(array,sequence):
    seqIndex = 0
    for num in array:
        if len(sequence) == seqIndex:
            break
        if sequence[seqIndex]==num:
            seqIndex +=1
    return seqIndex == len(sequence)

array = [5,1,22,25,6,-1,8,10]
seq = [1,6,-1,10]
isValidSubsequence(array,seq)