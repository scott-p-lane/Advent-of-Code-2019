'''
Created on Feb 10, 2020

@author: scott
'''
from aoc_helpers.Moon import Moon
from itertools import combinations
from datetime import datetime
from aoc_helpers.GeneralHelperFunctions import lcm
 
if __name__ == '__main__':     
    ##TEST 1 INPUT
    #moon1 = Moon("moon1", -1, 0, 2)
    #moon2 = Moon("moon2", 2, -10, -7)
    #moon3 = Moon("moon3", 4, -8, 8)
    #moon4 = Moon("moon4", 3, 5, -1)
    
    ##TEST 2 INPUT
    #origMoon1 = Moon("moon1",-8, -10, 0)
    #origMoon2 = Moon("moon2", 5, 5, 10)
    #origMoon3 = Moon("moon3", 2, -7, 3)
    #origMoon4 = Moon("moon4", 9, -8, -3)

   
    ##MAIN INPUT
    origMoon1 = Moon("moon1", 17, -9, 4)
    origMoon2 = Moon("moon2", 2, 2, -13)
    origMoon3 = Moon("moon3", -1, 5, -1)
    origMoon4 = Moon("moon4", 4, 7, -7)
    moon1 = Moon(origMoon1.moonId,
                 origMoon1.coordinates['x'], 
                 origMoon1.coordinates['y'], 
                 origMoon1.coordinates['z'])
    moon2 = Moon(origMoon2.moonId,
                 origMoon2.coordinates['x'], 
                 origMoon2.coordinates['y'], 
                 origMoon2.coordinates['z'])
    moon3 = Moon(origMoon3.moonId,
                 origMoon3.coordinates['x'], 
                 origMoon3.coordinates['y'], 
                 origMoon3.coordinates['z'])
    moon4 = Moon(origMoon4.moonId,
                 origMoon4.coordinates['x'], 
                 origMoon4.coordinates['y'], 
                 origMoon4.coordinates['z'])
    
    start = datetime.now()
    
    origMoons = [origMoon1, origMoon2, origMoon3, origMoon4]
    currMoons = [moon1, moon2, moon3, moon4]
    
    #Initialize pairs outside of loop (to speed things up)
    pairsList = []
    for pair in combinations(currMoons,2):
        pairsList.append(pair)
    pairCount = len(pairsList)
    
       
    steps = 0
    repeats = []

    for axis in ('x','y','z'):
        sameAsStart = 0
        steps = 0
        while (sameAsStart != len(currMoons)):
            steps += 1
            if steps % 100000 == 0:
                print("Up to step ",steps," on axis ",axis)
            for pair in pairsList:
                pair[0].calculateVelocity(pair[1],axis)
            sameAsStart = 0
            for moon in zip(currMoons,origMoons):
                moon[0].advancePosition(axis)
                if moon[0].coordinates[axis] == moon[1].coordinates[axis]:
                    if moon[0].velocity[axis] == 0:
                        sameAsStart += 1
        #WEND
        print("For",axis,"axis the system repeated after",steps,"steps!")
        repeats.append(steps)
    #FEND
    print("DONE! System will revert to original state in",lcm(repeats),"steps.")
    end = datetime.now()
    total_time = end - start
    print("Finished in",total_time)
