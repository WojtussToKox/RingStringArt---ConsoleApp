import math

def makePixelLine(startingNail, endingNail):
    x0, y0 = startingNail
    x1, y1 = endingNail
    
    linePixels = []
    
    diffX = abs(x0 - x1)
    diffY = abs(y0 - y1)
    
    stepX = 1 if x0 < x1 else -1
    stepY = 1 if y0 < y1 else -1
    
    err = diffX - diffY
    linePixels.append((x0, y0))
    while x0 != x1 or y0 != y1:
        
        doubleErr = 2 * err     
           
        if doubleErr > -diffY:
            err -= diffY
            x0 += stepX
            
        if doubleErr < diffX:
            err += diffX
            y0 += stepY
            
        linePixels.append((x0, y0))
    
    return linePixels

def getAverageLineDarkness(image, line):
    
    sumOfWhite = 0
    
    for (x,y) in line:
        sumOfWhite += int(image[y,x])
        
    return sumOfWhite / len(line)

def lightenLine(image, line):
    for (x,y) in line:
        image[y, x] = min(255, int(image[y, x]) + 20)
        
    return image    