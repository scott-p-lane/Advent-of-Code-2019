'''
Created on Dec 8, 2019

@author: slane
'''
from aoc_helpers.IntCode import IntCode

#initialize opcodes
program = IntCode("input_Part2.txt")
program.opInputs.append(1)
instrCount = program.executeAll()
print ("PROGRAM COMPLETED!")
        
    