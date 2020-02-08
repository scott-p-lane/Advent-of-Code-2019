'''
Created on Jan 11, 2020

@author: slane
'''

from aoc_helpers.IntCode import IntCode
from itertools import permutations

perms = permutations([5,6,7,8,9]) 

#initialize opcodes
permCount = 0
maxVal = 0
maxSeq = [0,0,0,0,0]
inputCount = 0
for perm in perms:
    print("Processing permutation: ",perm)
    amps = [IntCode("input_part1.txt") for _ in range(5)]
    output_signal = 0
    #Append phase settings to each instance of the program
    for amp,phase_setting in zip(amps,perm):
        amp.opInputs.append(phase_setting)
    while amps[-1].getOpCode() != '99':
        for amp in amps:
            amp.opInputs.append(output_signal)
            if amp.executeUntil('04'):
                #Execute the output intstruction, capture it then move on
                #to the next amplifier.
                amp.executeOperation()
                output_signal = amp.opOutput
        if output_signal > maxVal:
            maxVal = output_signal
            maxSeq = perm

#FEND: Iterating all permutations
print("Maximum Value is ",maxVal," from sequence ",maxSeq)