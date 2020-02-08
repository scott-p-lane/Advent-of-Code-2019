'''
Created on Jan 11, 2020

@author: slane
'''

from aoc_helpers.IntCode import IntCode
from itertools import permutations

perms = permutations([0,1,2,3,4]) 

#initialize opcodes
program = IntCode("input_part1.txt")

permCount = 0
maxVal = 0
maxSeq = [0,0,0,0,0]
for perm in perms:
    print("Processing permutation: ",perm)
    program = IntCode("input_part1.txt")
    program.opOutput = '0'
    permCount += 1
    for val in perm:
        program.opIndex = 0
        program.opInputs.append(val)
        program.opInputs.append(int(float(program.opOutput)))
        opCode = program.executeOperation()
        while (opCode != '99'):
            opCode = program.executeOperation()
        #WEND Executing entire program
    #FEND: Iterating all values in a single permutation
    if program.opOutput > maxVal:
        maxVal = program.opOutput
        maxSeq = perm
#FEND: Iterating all permutations
print("Maximum Value is ",maxVal," from sequence ",maxSeq)

print ("PROGRAM COMPLETED! Processed ",permCount," permutations.")