import cv2
import numpy as np


img = cv2.imread('img/lena.png ')


height, width, _ = img.shape


output = np.zeros((height, width, 3), np.uint8)


for i in range(1, height-1):
    for j in range(1, width-1):
        neighbors = img[i-1:i+2, j-1:j+2] 
        mean = np.mean(neighbors, axis=(0,1))
        output[i,j] = mean

        
cv2.imshow('Input Image', img)
cv2.imshow('Output Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
