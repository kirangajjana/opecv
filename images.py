import cv2
print("package imported")
image=cv2.imread("images.jpg")
cv2.imshow("output",image)
cv2.waitKey(10000)