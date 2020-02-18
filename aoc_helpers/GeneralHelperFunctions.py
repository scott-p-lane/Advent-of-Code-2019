'''
Created on Feb 18, 2020

@author: scott-p-lane

This is just a collection of useful helper functions. What makes this useful is it captures
some of the power of Python libraries without me having to remember how to invoke them (or Google
it again).

Also contains useful function not provided by Python or extends some of the functionality provided
by existing modules.
'''

from numpy import gcd

'''
Takes in a list of numbers 2 or more and calculates the LCM. 

The lcm of three or more integers can be found recursively. For three, the following formula turns calculating the lcm into two other lcm calculations.
lcm(a, b, c) = lcm(a, lcm(b, c)).

Takes in list and returns a float representing the LCM.
'''
def lcm(nums: []) -> float:
    if len(nums) < 2:
        return nums[0]
    mval = float(nums[0])
    for i in range(1,len(nums)):
        mval = mval * float(nums[i]) / gcd(nums[i-1],nums[i])
    return mval
        

