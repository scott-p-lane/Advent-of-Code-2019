'''
Created on Jan 21, 2020

@author: slane
'''
from aoc_helpers.IntCode import IntCode

program = IntCode("input_day9.txt")
program.opInputs.append(2)
outputstr = ''
while program.executeUntil('04'):
    program.executeOperation()
    outputstr += str(program.opOutput) + ','
print("Done. Output is ",outputstr)