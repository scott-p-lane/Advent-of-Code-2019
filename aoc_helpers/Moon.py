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
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.xVelocity = float(0)
        self.yVelocity = float(0)
        self.zVelocity = float(0)
        self.moonId = moonName
        
    def getCoordinate(self):
        return [self.x, self.y, self.z]

    def getVelocity(self):
        return [self.xVelocity,self.yVelocity,self.zVelocity]
    
    def calculateVelocity(self,moon):
        """
        Calculates the gravity and adds to velocity. Returns the new velocity.
        THIS DOES NOT ADJUST VELOCITY OF THE MOON PASSED IN!!
        """
        myCoordinate = self.getCoordinate()
        otherCoordinate = moon.getCoordinate()
        myVelocity = self.getVelocity()
        
        for i in range(len(myCoordinate)):
            #Velocity is unchanged if coordinates are equal
            if myCoordinate[i] > otherCoordinate[i]:
                myVelocity[i] -= 1
            elif myCoordinate[i] < otherCoordinate[i]:
                myVelocity[i] += 1
        self.xVelocity = myVelocity[0]
        self.yVelocity = myVelocity[1]
        self.zVelocity = myVelocity[2]
        return self.getVelocity()

    def advancePosition(self):
        """
        Using the velocity, calculates the next position (x, y, z) using the current velocity.
        Returns new coordinates when done.
        """
        self.x += self.xVelocity
        self.y += self.yVelocity
        self.z += self.zVelocity
        return self.getCoordinate()
    
    def potentialEnergy(self):
        total = float(0)
        for pos in self.getCoordinate():
            total += abs(float(pos))
        return total
    
    def kineticEnergy(self):
        total = float(0)
        for velocity in self.getVelocity():
            total += abs(float(velocity))
        return total
    
    def totalEnergy(self):
        return self.potentialEnergy() * self.kineticEnergy()
        
            