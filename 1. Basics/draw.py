import cv2 as cv
import numpy as np 

blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('Blank', blank)

#Color given pixesl
#blank[100:200, 0:200] = 0,255,0
#cv.imshow('Green', blank)

#Draw rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=2)
cv.imshow('Rectangle', blank)

#Draw circle
cv.circle(blank, (100, 100), 50, (0, 0, 255), thickness=2)
cv.imshow('Circle', blank)

cv.waitKey(0)