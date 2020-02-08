'''
Created on Dec 8, 2019

@author: slane
'''
from aoc_helpers.IntCode import IntCode

#initialize opcodes
program = IntCode("input.txt")
instrCount = program.executeAll()
print ("Part 1 is DONE! Position 0 has a value of:",program.returnResult(0),"with",instrCount,"operations run.")

#Part two: Find p1/p2 overrides that will lead to 19690720
for i in range(100):
    for j in range(100):
        program = IntCode("input.txt")
        program.setParam(1, i)
        program.setParam(2,j)
        program.executeAll()
        if program.returnResult(0) == 19690720:
            print("Part 2 DONE:",100*i+j)
            break
print ("PROGRAM COMPLETED!")
        
    