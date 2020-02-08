'''
Created on Dec 8, 2019

@author: slane
'''
from enum import Enum



'''
Enum that contains a mapping of label to index in tuple holding the information.
'''
class OpCodesMeta(Enum):
    OPERATION = 0
    OPLENGTH = 1
    OPCODELEN = 2
    STORERESULT = 3


class ParamModes(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2
    
class IntCode (object):
    
    def __init__(self, opFile):
        '''
        Constructor
        '''
        self.opCodeMeta = {'99':('END',0,0), 
                           '01':('ADD',4,1),
                           '02':('MULT',4,1),
                           '03':("INPUT",2,1),
                           '04':("OUTPUT",2,0),
                           '05':("JUMP_TRUE",3,0),
                           '06':("JUMP_FALSE",3,0),
                           '07':("LT",4,1),
                           '08':("EQ",4,1),
                           '09':("BASE",2,0)}
        self.instrCount = 0
        self.relativeBase = 0
        self.opInputs = []
        self.opOutput = 'uninitialized output'
        self.opIndex = 0
        self.instructions = []
        self.inputFile = opFile
        inputFile = open(opFile,"r")
        for line in inputFile.readlines():
            self.instructions.extend(line.split(","))
        inputFile.close()
    
    '''
    Executes instructions until the specified opCode is encountered.
    OpCode should be presented as 2 two digit string value (e.g., '01')
    Return True if we are at the specified operation or False if we reached
    the end of the program wihtout hitting the specified opCode.
    '''
    def executeUntil(self,opCode):
        currOp = self.getOpCode()
        while currOp != opCode and currOp != '99':
            currOp = self.executeOperation()
        if currOp == opCode:
            return True
        return False   
           
    '''
    Executes all the instructions and returns the number of instructions run
    '''   
    def executeAll(self):
        opCode = int(self.executeOperation())
        count = 1
        while (opCode != '99'):
            opCode = self.executeOperation()
            count += 1  
        return count   
    
              
                  
    '''
    Executes the current operation and advances to the next operation. 
    Returns the operation code that was executed.
    '''
    def executeOperation (self):
        op = self.getOpCode()
        if op == '99':
            return op
        params = self.getParams()
        paramModes = self.getParamModes()
        oplen = self.getOpLength(op)
        instr = self.instructions[self.opIndex:self.opIndex+oplen]
        ip = self.opIndex #Store to see if it gets modified by the instructions.
        wasRun = self.add(op, params, paramModes)
        if wasRun == False:
            wasRun = self.multiply(op, params, paramModes)
        if wasRun == False:
            wasRun = self.getInput(op,params, paramModes)
        if wasRun == False:
            wasRun = self.output(op, params, paramModes)     
        if wasRun == False:
            wasRun = self.lessThan(op, params, paramModes)
        if wasRun == False:
            wasRun = self.equal(op, params, paramModes)   
        if wasRun == False:
            wasRun = self.jumpIfTrue(op, params, paramModes)
        if wasRun == False:
            wasRun = self.jumpIfFalse(op,params, paramModes)
        if wasRun == False:
            wasRun = self.setRelativeBase(op, params, paramModes)
        
        if wasRun == False:
            print("*** ERROR: Unhandled instruction encountered - ",instr," Will return 99 and abort.")
            return '99'

        #Advance to next instruction set
        if ip != self.opIndex:
            return self.getOpCode()
        return self.advanceToNextOperation(op)
    
    '''
    Locations are position or offset based (never literal). Need to calculate the location 
    based on its mode.
    '''
    def getOutputLoc(self,loc,mode):
        loc = int(loc)
        if int(mode) == ParamModes.RELATIVE.value:
            return loc + self.relativeBase
        return loc
        
    '''
    Stores the value in the specified location. Will grow array if loc is out of bounds.
    '''
    def storeResult(self,val,loc):
        if loc >= len(self.instructions):
            newmem = [0] * (loc + 1 - len(self.instructions))
            self.instructions.extend(newmem)       
        self.instructions[loc] = val
    
    '''
    If the first parameter is less than the second parameter, 
    it stores 1 in the position given by the third parameter. Otherwise, it stores 0
    '''       
    def lessThan(self,op,params,paramModes):
        if op != '07':
            return False
        val1 = float(self.getParamValue(params[0],paramModes[0]))
        val2 = float(self.getParamValue(params[1],paramModes[1]))
        loc = self.getOutputLoc(params[2], paramModes[2])
        if val1 < val2:
            self.storeResult(1, loc)
        else:
            self.storeResult(0, loc)
        return True
    
        '''
    If the first parameter is equal to the second parameter, 
    it stores 1 in the position given by the third parameter. Otherwise, it stores 0
    ''' 
    def equal(self,op,params,paramModes):
        if op != '08':
            return False
        val1 = float(self.getParamValue(params[0],paramModes[0]))
        val2 = float(self.getParamValue(params[1],paramModes[1]))
        loc = self.getOutputLoc(params[2], paramModes[2])
        if val1 == val2:
            self.storeResult(1, loc)
        else:
            self.storeResult(0, loc)
        return True
            
    def jumpIfTrue(self,op,params,paramModes):
        if op != '05':
            return False
        val1 = float(self.getParamValue(params[0],paramModes[0]))
        val2 = int(self.getParamValue(params[1],paramModes[1]))
        #Assuming we wouldn't advance instruction pointer beyond the end of the program.
        if val1 != 0:
            self.opIndex = val2
        return True
   
    def jumpIfFalse(self,op,params,paramModes): 
        if op != '06':
            return False
        val1 = float(self.getParamValue(params[0],paramModes[0]))
        val2 = int(self.getParamValue(params[1],paramModes[1]))
        #Assuming we wouldn't advance instruction pointer beyond the end of the program.
        if val1 == 0:
            self.opIndex = val2
        return True
    
    def output(self,op,params,paramModes):
        if op != '04':
            return False
        val = self.getParamValue(params[0], paramModes[0])
        self.opOutput = val
        return True

    def getInput(self,op,params,paramModes):
        if op != '03':
            return False
        loc = self.getOutputLoc(params[0], paramModes[0])
        self.instructions[loc] = float(self.opInputs.pop(0))
        return True

    def add(self,op,params,paramModes):
        if op != '01':
            return False      
        val1 = float(self.getParamValue(params[0],paramModes[0]))
        val2 = float(self.getParamValue(params[1],paramModes[1]))
        loc = self.getOutputLoc(params[2], paramModes[2])
        self.storeResult(val1 + val2, loc)
        return True
    
    def multiply(self,op,params,paramModes):
        if op != '02':
            return False
        val1 = float(self.getParamValue(params[0],paramModes[0]))
        val2 = float(self.getParamValue(params[1],paramModes[1]))
        loc = self.getOutputLoc(params[2], paramModes[2])
        self.storeResult(val1 * val2, loc)
        return True
    
    def setRelativeBase(self,op,params,paramModes):
        if op != '09':
            return False
        self.relativeBase += int(self.getParamValue(params[0],paramModes[0]))
        return True
    
      
    '''
    Seperates OpCode from ParamModes. Will also prefix '0' in front
    of opCodes with no paramModes ('1' will become '01')
    
    '''
    def getOpCode(self):
        codelen = OpCodesMeta.OPCODELEN.value
        op = str(self.instructions[self.opIndex])
        if (len(op)) < codelen:
            return "0" + op
        return op[len(op)-codelen:len(op)]

    '''
    Returns the paramemter modes (in same order as params). Will 
    add in default param mode of 0 when they are missing.
    
    Param modes will be aligned with parameters so param at index 1 will be able to find its mode at index 1.
    '''
    def getParamModes(self):
        codelen = OpCodesMeta.OPCODELEN.value
        op = str(self.instructions[self.opIndex])
        paramModes = list(op[0:len(op)-codelen])
        paramCount = self.getOpLength(self.getOpCode()) - 1
        paramModes.reverse()
        modeCount = len(paramModes)
        if (len(paramModes) < paramCount):
            for i in range(modeCount,paramCount):
                paramModes.append(0)
        return paramModes
    
    '''
    Returns the list of paramemters that is aligned with param modes list. 
    
    Essentially strips off the opCode from the instruction.
    '''
    def getParams(self):
        op = self.getOpCode()
        oplen = self.getOpLength(op)
        params = []
        for i in range(1,oplen):
            params.append(self.instructions[self.opIndex + i])
        return params

    def getParamValue(self,paramLoc,paramMode):
        index = int(paramLoc)
        mode = int(paramMode)
        if mode == ParamModes.POSITION.value or mode == ParamModes.RELATIVE.value:
            #check length and grow if necessary
            if index >= len(self.instructions):
                newmem = [0] * (index + 1 - len(self.instructions))
                self.instructions.extend(newmem)
        if mode == ParamModes.POSITION.value:
            val = self.instructions[index]
        elif mode == ParamModes.RELATIVE.value:
            val = self.instructions[self.relativeBase + index]
        else:
            val = paramLoc
        return val
        
    
    '''
    Fetch operation length from OpCodesMeta structure. This is used to 
    figure out where the instruction pointer should be set to after processing
    the instruction.
    '''    
    def getOpLength(self, opcode):
        return self.opCodeMeta[opcode][OpCodesMeta.OPLENGTH.value]
    
  
    '''
    Sets the instruction pointer to the next operation in the program.
    Takes as input the two-digit string opCode (e.g., '01') to figure out
    how far to advance. 
    Returns the opCode of the instruction after it has been advanced.
    WARNING: DO NOT CALL THIS FOR JUMP COMMANDS THAT MAY HAVE ALREAD ADVANCED
    THE INSTRUCTION POINTER!
    '''
    def advanceToNextOperation(self,currOpCode):
        oplen = self.getOpLength(currOpCode)
        self.opIndex += oplen
        return self.getOpCode()