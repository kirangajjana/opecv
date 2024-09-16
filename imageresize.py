import cv2
import numpy as np

video=cv2.VideoCapture(0)

while True:
    success,img=video.read()

    resize=cv2.resize(img,(200,150))
    cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),5)
    cv2.circle(img,(img.shape[1]//2,img.shape[0]//2),10,(0,255,0),2)
    cv2.circle(img,(img.shape[1]//2,img.shape[0]//2),10,(0,255,0),2)

    cv2.imshow("OUTPUT",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


   