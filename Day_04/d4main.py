'''
Created on Jan 4, 2020

@author: slane
'''
matchesCount = 0
failCount = 0

'''
Input range is 234208 - 765869, however the end value in Python range is not inclusive, so I had to bump
it up by one.
'''
for val in range(234208,765870):
    valray = list(str(val))
    hasDecrease = 0
    hasValidDouble = 0
    repeatCount = 0
    for i in range(1,len(valray)):
        prior = int(valray[i-1])
        curr = int(valray[i])
        if (curr < prior):
            hasDecrease = 1
            break
        if (curr == prior):
            repeatCount += 1
        if (curr != prior):
            if (repeatCount == 1):
                hasValidDouble += 1
            repeatCount = 0

    #Covers the case where the last two digits are a repeated.
    if (repeatCount == 1):
        hasValidDouble += 1        
    if (hasValidDouble >= 1 and hasDecrease == 0):
        matchesCount += 1
    else:
        failCount += 1

print("Done! Found",matchesCount,"matches and ",failCount,"failures.")
    

    