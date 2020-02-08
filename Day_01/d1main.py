'''
Created on Dec 8, 2019

@author: slane
'''
inputFile = open("input.txt","r")
totalFuel = 0
for line in inputFile.readlines():
    fuel = int(line)
    fuel = int(fuel/3) - 2
    fuelPlus = int(fuel/3) - 2
    while (fuelPlus > 0):
        totalFuel += fuelPlus
        fuelPlus = int(fuelPlus/3) - 2
    totalFuel += fuel
inputFile.close()
print ("Total Fuel Needed: ",totalFuel)