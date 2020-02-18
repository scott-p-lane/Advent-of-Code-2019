'''
Created on Feb 10, 2020

@author: scott
'''
class Moon(object):
    
    def __init__(self, moonName:str, x: float, y: float, z: float):
        """
        Initialize with three dimensional coordinates (x, y, z) which will be treated as integers.
        Initialize velocity on each axis to 0
        """
        self.velocity = {'x':float(0),'y':float(0),'z':float(0)}
        self.coordinates = {'x':float(x),'y':float(y),'z':float(z)}
        self.moonId = moonName
    
    def calculateVelocity(self,otherMoon,axis):
        myPosition = self.coordinates[axis]
        theirPosition = otherMoon.coordinates[axis]
        if myPosition != theirPosition:
            if myPosition > theirPosition:
                self.velocity[axis] -= 1
                otherMoon.velocity[axis] += 1
            else:
                self.velocity[axis] += 1
                otherMoon.velocity[axis] -= 1
        #ENDIF
    #END FUNCTION:calculateVelocity

    
           
    def advancePosition(self,axis):
        self.coordinates[axis] += self.velocity[axis]


    def advanceAllPositions(self):
        for axis in self.coordinates.keys():
            self.coordinates[axis] += self.velocity[axis]
    
    def potentialEnergy(self):
        total = float(0)
        for pos in self.coordinates.values():
            total += abs(float(pos))
        return total
    
    def kineticEnergy(self):
        total = float(0)
        for velocity in self.velocity.values():
            total += abs(float(velocity))
        return total
    
    def totalEnergy(self):
        return self.potentialEnergy() * self.kineticEnergy()
        
            