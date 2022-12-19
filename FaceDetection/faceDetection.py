import cv2 as cv
import numpy as np

img = cv.imread("group.png")
cv.imshow("Person",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Picture of Person',gray)

haar_cascade = cv.CascadeClassifier("haarface.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('Detected Faces',img)

cv.waitKey()