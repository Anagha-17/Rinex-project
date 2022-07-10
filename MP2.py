# TO SCALE UP AN IMAGE AND RECOGNISE FACES


import cv2
import numpy as np
img=cv2.imread('mp.jpg')
cv2.imshow('original',img)
cv2.waitKey(2000)

#face recognision

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces=face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=1)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    #w,h -width ,height

#resizing

img =cv2.resize(img,None,fx=2,fy=2)
cv2.imshow('new',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
