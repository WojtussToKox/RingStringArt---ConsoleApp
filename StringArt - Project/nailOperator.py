import cv2
import numpy as np
import imageOperator as imOp
import lineOperator as liOp
import math 
from collections import namedtuple

PI = math.pi

Nail = namedtuple("Nail", ["x", "y"])

nails = []

def setUpNailsAndBoard(filePath = "test.png", NUMBER_OF_NAILS = 100):
    image = imOp.getAndMaskImage(filePath)
    
    
    CIRCLE_STEP = (2*PI)/NUMBER_OF_NAILS
    RADIUS = image.shape[0]//2 - 1
    CENTER_OF_IMAGE = image.shape[0]//2
    
    for i in range(NUMBER_OF_NAILS):
        x = int(CENTER_OF_IMAGE + RADIUS * math.cos(CIRCLE_STEP*i))
        y = int(CENTER_OF_IMAGE + RADIUS * math.sin(CIRCLE_STEP*i))
        nails.append(Nail(x,y))


    board = np.full((image.shape[1], image.shape[0]), 255, np.uint8)

    for nail in nails:
        cv2.circle(board, (nail.x, nail.y), 1, 0, -1)


    allLines = {}
    
    for i in range(NUMBER_OF_NAILS):
        for j in range(i+1, NUMBER_OF_NAILS):
            allLines[i,j] = liOp.makePixelLine(nails[i], nails[j])
    
    return board, allLines
    
    
def findMostDarkLine(image, startingNailId, lookUpTable):
    
    darkestLine = []
    darkness = 255
    endId = 0
    
    for i in range(len(nails)):
        idDiff = abs(startingNailId - i)
        realDistance = min(idDiff, len(nails) - idDiff)
        if(realDistance > 25):
            key = (min(startingNailId, i), max(startingNailId, i))
            averageDarnkess = liOp.getAverageLineDarkness(image, lookUpTable[key])
            if (averageDarnkess < darkness):
                darkness = averageDarnkess
                darkestLine = lookUpTable[key]
                endId = i
    
    return darkestLine, endId
    