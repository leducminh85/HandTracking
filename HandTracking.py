import cv2
import numpy as np
import mediapipe as mp
import time
import Module as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)

    img2 = img
    img2[:,::-1]=img[:,:]
    
    cv2.imshow("Image", img2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
