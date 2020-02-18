'''
Created on Feb 12, 2020

@author: slane
'''
import time
import datetime

from aoc_helpers.Moon import Moon
from itertools import combinations


def concurrentVelocity(pairs):
    for axis in ('x','y','z'):
        pairs[0].calculateVelocity(pairs[1],axis)

def concurrentPositioning(moon):
    moon.advanceAllPositions()
    
if __name__ == '__main__':  
    start = datetime.datetime.now()
    
    ##TEST 1 INPUT
    #moon1 = Moon("moon1", -1, 0, 2)
    #moon2 = Moon("moon2", 2, -10, -7)
    #moon3 = Moon("moon3", 4, -8, 8)
    #moon4 = Moon("moon4", 3, 5, -1)
    
    ##TEST 2 INPUT
    moon1 = Moon("moon1",-8, -10, 0)
    moon2 = Moon("moon2", 5, 5, 10)
    moon3 = Moon("moon3", 2, -7, 3)
    moon4 = Moon("moon4", 9, -8, -3)
    
    
    
    ##MAIN INPUT
    #moon1 = Moon("moon1", 17, -9, 4)
    #moon2 = Moon("moon2", 2, 2, -13)
    #moon3 = Moon("moon3", -1, 5, -1)
    #moon4 = Moon("moon4", 4, 7, -7)
    
    moons = [moon1, moon2, moon3, moon4]
    pairsList = []
    for pair in combinations(moons,2):
        pairsList.append(pair)
    pairCount = len(pairsList)
    
    for step in range(1,2029):
        for pair in pairsList:
            concurrentVelocity(pair)
        for moon in moons:
            concurrentPositioning(moon)

            
    totalEnergy = 0
    for moon in moons:
        totalEnergy += moon.totalEnergy()
    print("DONE! Total Energy of Systems is ",totalEnergy)
    for moon in moons:
        print (moon.moonId,moon.coordinates.items())
    end = datetime.datetime.now()
    total_time = end - start
    print(total_time)