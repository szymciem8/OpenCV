import cv2 as cv
import os

#Converting to grayscale
print(os.getcwd())
# img = cv.imread(os.path.join(os.getcwd(), "Photos", "park.jpg"))
img = cv.imread(os.getcwd() + "\Photos\park.jpg")
cv.imshow('Boston', img)

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

#Blur
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur", blur)

#Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Cany', canny)

#Blurred cany
blurred_canny = cv.Canny(blur, 125, 175)
cv.imshow('Blurred Cany', blurred_canny)

#Dilated
dilated = cv.dilate(blurred_canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resized
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Cropping
cropped = img[0:200, 100:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)