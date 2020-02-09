'''
Created on Feb 8, 2020

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
grid = GridCoordinates(black)
program.opInputs.append(white)

while program.executeUntil('03'):
    #Pass in color of the current cell.
    program.opInputs.append(grid.getCoordinate()[-1])
    
    #Get the color to paint the cell.
    program.executeUntil('04')
    program.executeOperation()
    tileColor = int(program.opOutput)
    if tileColor not in [black,white]:
        print("*** ERROR: Unexpected color value - ", tileColor)

    #Get the direction to advance the point to
    program.executeUntil('04')
    program.executeOperation()
    direction = int(program.opOutput)
    if direction == TurnDirection.left.value:
        grid.changeOrientation(TurnDirection.left)
    elif direction == TurnDirection.right.value:
        grid.changeOrientation(TurnDirection.right)
    else:
        print("*** ERROR: Unhandled TurnDirection value: ",program.opOutput)
        
    #Paint and advance 1
    grid.setCoordinateValue(tileColor)
    grid.advance(1)

#Now we need to print out each row in order (to get letters)
for row in range(grid.rowCount(),-1,-1):
    rowstr = grid.renderGridRow(row, [0])
    print(rowstr)
      
print("DONE!! ")