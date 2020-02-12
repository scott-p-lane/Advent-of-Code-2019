'''
Created on Feb 10, 2020

@author: scott
'''
from aoc_helpers.Moon import Moon
from itertools import combinations

##TEST 2 INPUT
#moon1 = Moon("moon1",-8, -10, 0)
#moon2 = Moon("moon2", 5, 5, 10)
#moon3 = Moon("moon3", 2, -7, 3)
#moon4 = Moon("moon4", 9, -8, -3)



##MAIN INPUT
moon1 = Moon("moon1", 17, -9, 4)
moon2 = Moon("moon2", 2, 2, -13)
moon3 = Moon("moon3", -1, 5, -1)
moon4 = Moon("moon4", 4, 7, -7)

moons = [moon1, moon2, moon3, moon4]
for step in range(1,1001):
    for pairs in combinations(moons,2):
        pairs[0].calculateVelocity(pairs[1])
        pairs[1].calculateVelocity(pairs[0])
    print("After Step ",step,":")
    for moon in moons:
        moon.advancePosition()
        
totalEnergy = 0
for moon in moons:
    totalEnergy += moon.totalEnergy()
print("DONE! Total Energy of Systems is ",totalEnergy)