'''
Created on Feb 10, 2020

@author: scott
'''
from aoc_helpers.Moon import Moon
from itertools import combinations

moon1 = Moon("moon1", -1, 0, 2)
moon2 = Moon("moon2", 2, -10, -7)
moon3 = Moon("moon3", 4, -8, 8)
moon4 = Moon("moon4", 3, 5, -1)

moons = [moon1, moon2, moon3, moon4]
for pairs in combinations(moons,2):
    print("[",pairs[0].moonId,", ",pairs[1].moonId,"]")
print("DONE!")