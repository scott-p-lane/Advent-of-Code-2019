'''
Created on Dec 8, 2019

@author: slane

Creates a 2D grid of specified dimensions and supports marking a "path" through it. 

'''
from pip._vendor.pyparsing import col

class GridMap (object):
       
    '''
    classdocs
    '''
    def __init__(self, colCount, rowCount, initVal):
        '''
        Constructor
        '''
        self.rowCount = rowCount
        self.colCount = colCount
        self.initVal = initVal
        self.currentPath = 0
        self.pathStepCount = 0
        #orientation can be u, l, r, d. 
        self.orientation = ['l','u','r','d']
        self.orientationIndex = 1
        
        '''
        Initialize grid using arr = [[0 for i in range(cols)] for j in range(rows)] 
        '''
        self.grid = [[initVal for i in range(rowCount)] for j in range(colCount)] 
        self.setStartPos()
        self.shortestDistance = colCount - self.startCol + rowCount - self.startRow
        self.shortestSteps = colCount * rowCount

    '''
    Changes the orientation of current location (the direction it will move in) by 90 degrees left/right.
    Returns the new orientation.
    '''
    def changeOrientation(self,turnDirection):
        if turnDirection == 'l':
            self.orientationIndex -= 1
        else:
            self.orientationIndex += 1
            
        if (self.orientationIndex > len(self.orientation) - 1):
            self.orientationIndex = 0
        if (self.orientationIndex < 0):
            self.orientationIndex = len(self.orientation) - 1
        return self.getOrientation()
    
    def getOrientation(self):
        return self.orientation[self.orientationIndex]
                
    def manhattanDistance(self):
        return self.rowDistance(self.currRow) + self.colDistance(self.currCol)

    def rowDistance(self,row):
        return abs(row - self.startRow) 
    
    def colDistance(self,col):
        return abs(col - self.startCol)

    def getCellValue(self):
        return self.grid[self.currCol][self.currRow]
    
    '''
    Sets the values, but also checks for intersections and calculates the shortest manhattan distance.
    When settting the value, we'll use first digit for path, second is the step count.
    '''
    def set(self, col, row, val):
        currVal = self.grid[col][row]
        mdist = self.colDistance(col) + self.rowDistance(row)
        if currVal == self.initVal:
            self.grid[col][row] = str(self.currentPath) + str(val)
        else:

            #Do not count path intersections for same path
            pathID = int(currVal[0]) 
            if (pathID != self.currentPath):
                steps = int(currVal[1:]) + val
                if (steps < self.shortestSteps):
                    self.shortestSteps = steps
                if (mdist < self.shortestDistance):
                    self.shortestDistance = mdist
        self.currCol = col
        self.currRow = row
        
    def setCurrCellTo(self,cellVal):
        self.grid[self.currCol][self.currRow] = cellVal
    
    '''
    Advances current position in the grid to the next cell using the orientation.
    Returns the value in the cell that was advanced too.
    '''
    def advanceToNextCell(self):
        colOffset = 0
        rowOffset = 0
        if self.getOrientation() == 'l':
            colOffset = -1
        if self.getOrientation() == 'r':
            colOffset = 1
        if self.getOrientation() == 'd':
            rowOffset = 1
        if self.getOrientation() == 'u':
            rowOffset = -1
        self.currCol += colOffset
        self.currRow += rowOffset
        return self.getCellValue()
            
  
    def markPath(self,rludInstr):
        instr = str(rludInstr).lower()
        direction = instr[0]
        distance = int(instr[1:])
        indexDirection = 1
        if direction == "l" or direction == "u":
            distance *= -1
            indexDirection = -1
            
        if (direction == "r" or direction == "l"):
            endIndex = self.currCol + distance
        else:
            endIndex = self.currRow + distance
        
        if direction == "r" or direction == "l":
            while self.currCol != endIndex:
                self.pathStepCount += 1
                markChar = self.pathStepCount
                self.set(self.currCol + indexDirection, self.currRow, markChar)
            
        if (direction == "u" or direction == "d"):
            while self.currRow != endIndex:
                self.pathStepCount += 1
                markChar = self.pathStepCount
                self.set(self.currCol, self.currRow + indexDirection, markChar)
        return [self.currCol,self.currRow]
                   
    '''
    Sets the start position to the center of the grid (or approximately center)
    '''
    def setStartPos(self):
        '''
        Setting the start position implies a new path to process, so increment path and
        reset step counts
        '''
        self.currentPath += 1
        self.pathStepCount = 0
        self.currCol = int(self.colCount/2)+1
        self.currRow = int(self.rowCount/2)+1
        self.startRow = self.currRow
        self.startCol = self.currCol
        
        
    def printGrid(self,startRow,startCol):
        for i in range(startRow,self.rowCount):
            gridstr = ""
            for j in range(startCol,self.colCount):
                gridstr += " "
                gridstr += str(self.grid[j][i])
            print(gridstr)
  
        