import nailOperator as nailOp
import imageOperator as imOP
import lineOperator as liOp
import cv2
path = "Maja.png"
board, lookUpTable = nailOp.setUpNailsAndBoard(path, 280)

image = imOP.getAndMaskImage(path)

cv2.imshow("before", image)

endId = 0

nailPath = [0]

for i in range(3000):
    if i % 100 == 0:
        print(f"Przeliczam linię numer {i}...")
        
    line, endId = nailOp.findMostDarkLine(image, endId, lookUpTable)

    for (x,y) in line:
        board[y,x] = max(0, int(board[y,x]) - 20)
    
    image = liOp.lightenLine(image, line)
    
    nailPath.append(endId)
    

for nail in nailPath:
    print(nail)

cv2.imshow("Nails", board)
cv2.imshow("after", image)
cv2.waitKey(0)
