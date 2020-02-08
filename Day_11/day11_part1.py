'''
Created on Feb 3, 2020

@author: slane
'''
from aoc_helpers.IntCode import IntCode
from aoc_helpers.GridMap import GridMap

#define some handy constants to use in the program
black = 0
white = 1
left = 0
right = 1
direction = 'u'

program = IntCode("input_part1.txt")
grid = GridMap(10000,10000,black)


paint_count = 0
turn_count = 0
while program.executeUntil('03'):
    #Pass in color of the current cell.
    program.opInputs.append(int(grid.getCellValue()))
    
    #Get the color to paint the cell.
    program.executeUntil('04')
    program.executeOperation()
    tileColor = int(program.opOutput)

    #Get the direction to advance the point to
    program.executeUntil('04')
    program.executeOperation()
    if program.opOutput == left:
        grid.changeOrientation("l")
    else:
        grid.changeOrientation("r")
        
    #Paint and advance 1
    grid.setCurrCellTo(tileColor)
    grid.advanceToNextCell()
print("DONE!! ")
print("Painted squares: ", paint_count, " Turns: ", turn_count)