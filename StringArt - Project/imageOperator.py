import cv2
import numpy as np

def rescaleImage(image, scale = 0.75, x = 500, y = 500):
    #width = int(image.shape[1] * scale)
    #height = int(image.shape[0] * scale)
    
    width, height = x, y
    
    dimensions = (width, height)
    
    return cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)

def getAndMaskImage(filePath = "test.png"):
    
    myImage = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

    myImageResized = rescaleImage(myImage)
    blank = np.full(myImageResized.shape[:2],255, np.uint8)

    mask = cv2.circle(blank, (myImageResized.shape[1]//2, myImageResized.shape[0]//2), 250, 0, -1)


    maskedImage = cv2.bitwise_and(myImageResized, myImageResized, mask=cv2.bitwise_not(mask))
    #maskedImage = cv2.bitwise_and(myImageResized, mask)
    maskedImage = cv2.bitwise_or(maskedImage, blank)


    
    return maskedImage

def addBorder(image, pixels = 50, color = [0,0,0]):
    top, bottom, left, right = [pixels] * 4  # 50px z każdej strony

    return cv2.copyMakeBorder(
        image, 
        top, bottom, left, right, 
        cv2.BORDER_CONSTANT, 
        value=color
    )