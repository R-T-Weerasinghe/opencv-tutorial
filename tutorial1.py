import cv2
from random import randint

img = cv2.imread('assets/dog.jpg', 1)
img = cv2.resize(img, (600, 400))
winName = "Image"

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.namedWindow(winName)
cv2.moveWindow(winName, 40, 30)
cv2.imshow(winName, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
