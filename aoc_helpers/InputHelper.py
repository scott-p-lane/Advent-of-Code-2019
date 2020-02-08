'''
Created on Jan 19, 2020

@author: slane
'''

class InputHelper(object):
    
    def __init__(self, inputFileName):
        self.inputFileName = inputFileName
        inputFile = open(inputFileName,"r")
        self.fileLines = inputFile.readlines()
        inputFile.close()
    
    def produceLayers(self,colCount,rowCount):
        startIndex = 0
        endIndex = colCount
        currHeight = 0
        line = self.lines[0]
        layer = []
        while endIndex < len(line):
            layer.extend(line[startIndex:endIndex])
            
            
            
