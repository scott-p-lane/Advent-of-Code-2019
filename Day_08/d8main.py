'''
Created on Jan 19, 2020

@author: slane
'''
import numpy as np
from pip._vendor.pyparsing import col

inputFile = open("input_day8_part1.txt","r")
pixels = []
for line in inputFile.readlines():
    pixels.extend(list(line))
inputFile.close()
print("Processed ",len(pixels)," pixels!")

width = 25
height = 6
layerSize = width * height
endIndex = layerSize
startIndex = 0
layers = []
while startIndex < len(pixels):
    layer = pixels[startIndex:endIndex]
    layers.append(layer)
    startIndex += layerSize
    endIndex += layerSize
layerCount = len(layers)

print("Processed ",len(layers)," layers")
minZeroLayer = layers[0]
minCount = layerSize
count = 0
for layer in layers:
    count = layer.count('0')
    if count < minCount:
        minCount = count
        minZeroLayer = layer 
print("Found layer with least zeros (",minCount,")")
print(minZeroLayer)
print("Count of 1's * count of 2's is ",minZeroLayer.count('1')*minZeroLayer.count('2'))

'''
PART two: use Numpy reshape to convert layers into 25x6 arrays that can be layereed on top
of each other.
'''
shapedLayers = []
for layer in layers:
    reshapedLayer = np.reshape(layer,(6,25))
    shapedLayers.append(reshapedLayer)

image = [[0] * width for i in range(height)]
#Now process each pixel, given top pixel priority over lesser pixel
for row in range(0,height):
    for col in range(0,width):
        for layer in range(layerCount-1,-1,-1):
            pixel = shapedLayers[layer][row][col]
            if pixel < '2':
                image[row][col] = pixel

for row in image:
    rowOutput = ''
    for col in row:
        if col == '1':
            rowOutput += col
        else:
            rowOutput += ' '
    print (rowOutput)
