'''
Created on Feb 8, 2020

@author: scott-p-lane
'''
from enum import Enum

class GridOrientation(Enum):
    left = 0
    up = 1
    right = 2
    down = 3

class TurnDirection(Enum):
    left = 0
    right = 1

class GridCoordinates (object):
    """
    Dictionary based implementation that represents grid coordinates and state for
    each coordinate. For certain types of grid related problems, this can be more optimal
    than a large, multi-dimensaional grid. Also useful in situations where grid sizes 
    are not known up front.     
    """

    def __init__(self, defaultVal=0):
        """
        Parameters
        ----------
        defaultVal: optional
            Default value of any coordinate in the grid that was not explicitly
            assigned a value. (default is 0)
        """
        self.grid = {}
        self.defaultVal = defaultVal
        #orientation is used to specify the direction we are facing/moving within the grid
        self.orientation = [GridOrientation.left, GridOrientation.up,
                            GridOrientation.right,GridOrientation.down]
        self.currentOrientation = GridOrientation.up    
        self.currentRow = 0
        self.currentCol = 0
        self.maxRow = 0
        self.minRow = 0
        self.maxCol = 0
        self.minCol = 0
   
    
    def changeOrientation(self,turnDirection: TurnDirection) -> GridOrientation:
        """
        Changes orientation by accepting a direction (l or r) and turning
        "1 step" in that direction.
        Parameters:
        ------------
        turnDirection : str
            Values are "l" (left), or "r" (right)
        """
        orientationIndex = self.currentOrientation.value
        if turnDirection == TurnDirection.left:
            orientationIndex -= 1
        else:
            orientationIndex += 1
            
        if (orientationIndex > len(self.orientation) - 1):
            orientationIndex = 0
        if (orientationIndex < 0):
            orientationIndex = len(self.orientation) - 1
        self.currentOrientation = self.orientation[orientationIndex]
        return self.currentOrientation
    
    def __createkey__(self):
        """
        Constructs a key for a coordinate using currentCol and currentRow values.
        """
        return str(self.currentCol) + "," + str(self.currentRow)
    
    def createKey(self,colIndex,rowIndex):
        return str(colIndex) + "," + str(rowIndex)
            
    def processedCoordinate(self):
        """
        Returns tuple in the form of (col,row,processed:bool)
        
        Which establishes the current coordinate and whether or not we have processed it before.
        Processing indicates that we explicitly performed an operation on it (like setting a value).
        """
        vals = self.getCoordinate()
        vals[-1] = False
        gridkey = self.__createkey__()
        if gridkey in self.grid.keys():
            vals[-1] = True
        return vals
      
    def setCoordinateValue(self,coordVal):
        """
        Sets the current coordinate to the specified value.
        
        Returns coordinate value (see getCoordinate)
        """
        gridkey = self.__createkey__()
        self.grid[gridkey] = coordVal
        return self.getCoordinate()
    
    def advance(self,distance = 1):
        """
        Advances specified distance in current orientation (default distance is 1)
        and returns coordinate value (see getCoordinate)
        """
        colOffset = 0
        rowOffset = 0
        if self.currentOrientation == GridOrientation.left:
            colOffset = -1 * distance
        if self.currentOrientation == GridOrientation.right:
            colOffset = distance
        if self.currentOrientation == GridOrientation.down:
            rowOffset = -1 * distance
        if self.currentOrientation == GridOrientation.up:
            rowOffset = distance
        self.currentCol += colOffset
        self.currentRow += rowOffset
        
        #See if we've expanded the grid
        if self.currentCol > self.maxCol:
            self.maxCol = self.currentCol
        if self.currentCol < self.minCol:
            self.minCol = self.currentCol
        if self.currentRow > self.maxRow:
            self.maxRow = self.currentRow
        if self.currentRow < self.minRow:
            self.minRow = self.currentRow
        
        return self.getCoordinate()        
    
    def getCoordinate(self):
        return self.getCoordinateAt(self.currentCol,self.currentRow)
    
    def getCoordinateAt(self,colIndex,rowIndex):
        """
        Returns tuple in the form of (col,row,val)
        """
        gridval = self.grid.get(self.createKey(colIndex,rowIndex),self.defaultVal)
        retvals = [self.currentCol,self.currentRow,gridval]
        return retvals
    
    def rowCount(self):
        """
        Returns absolute number of rows in the grid.
        """
        return abs(self.minRow) + abs(self.maxRow)
    
    def columnCount(self):
        """
        Returns absolute number of columns in the grid.
        """
        return abs(self.minCol) + abs(self.maxCol)
    
    def renderGridRow(self,rowIndex,whitespaceSet=[]):
        """
        Renders the specified row of a grid (first row is 0). 
        Uses "whitespace set" such that any value at that coordinate in the whitespace set
        will simply be outputted as a space.
        
        """
        rowstr = ""
        internalRowIndex = self.minRow + rowIndex
        for c in range(self.minCol,self.maxCol,1):
            gridval = self.grid.get(self.createKey(c,internalRowIndex),self.defaultVal)
            if gridval not in whitespaceSet:
                rowstr += str(gridval)
            else:
                rowstr += " "
        return rowstr
        
            