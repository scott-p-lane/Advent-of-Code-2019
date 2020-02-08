'''
Created on Feb 3, 2020

@author: slane
'''
from aoc_helpers.IntCode import IntCode
from aoc_helpers.GridCoordinates import GridCoordinates
from aoc_helpers.GridCoordinates import GridOrientation
from aoc_helpers.GridCoordinates import TurnDirection

#define some handy constants to use in the program
black = 0
white = 1
direction = GridOrientation.up

program = IntCode("input_part1.txt")
grid = GridCoordinates()


paint_count = 0
overlap_count = 0
while program.executeUntil('03'):
    #Pass in color of the current cell.
    program.opInputs.append(grid.getCoordinateValue()[-1])
    
    #Get the color to paint the cell.
    program.executeUntil('04')
    program.executeOperation()
    tileColor = int(program.opOutput)

    #Get the direction to advance the point to
    program.executeUntil('04')
    program.executeOperation()
    if program.opOutput == TurnDirection.left.value:
        grid.changeOrientation(TurnDirection.left)
    else:
        grid.changeOrientation(TurnDirection.right)
        
    #Paint and advance 1
    paint_count += 1
    if grid.processedCoordinate()[-1]:
        print("Already processed coordinate: ",grid.processedCoordinate())
        overlap_count += 1
    grid.setCoordinateValue(tileColor)
    grid.advance(1)
    
print("DONE!! ")
print("Painted squares: ", paint_count, " Overlap: ", overlap_count)
print("Tiles painted at least once: ",str(paint_count - overlap_count))