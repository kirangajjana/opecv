import cv2

video=cv2.VideoCapture("demo1.mp4")

while True:
   success,img=video.read()
   cv2.imshow("video",img)
   if cv2.waitKey(1) & 0xFF ==ord('q'):
        break