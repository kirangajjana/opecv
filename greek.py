import cv2

img=cv2.imread("demo.png",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("newimg.png",img)
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()