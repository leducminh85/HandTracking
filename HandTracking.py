import cv2
import mediapipe as mp
import time
import Module as htm
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
