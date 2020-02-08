'''
Created on Dec 8, 2019

@author: slane
'''

from aoc_helpers.GridMap import GridMap
print("Processing input . . . ")
inputFile = open("input.txt","r")
paths = []
for line in inputFile.readlines():
    paths.append(line.rstrip().split(","))
inputFile.close()

print("Initializing grid . . .")
grid = GridMap(15000,15000,0)

print("Marking paths from input . . . ")
for path in paths:
    for instr in path:
        grid.markPath(instr)
    grid.setStartPos()
    
print ("Done!! Shortest distance is: ", grid.shortestDistance,"Shorest step count is: ",grid.shortestSteps)