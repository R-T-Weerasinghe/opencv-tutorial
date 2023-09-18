import cv2
from random import randint

img = cv2.imread('assets/img.jpg', 1)
img = cv2.resize(img, (500, 500))
winname = "Image"

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.namedWindow(winname)
cv2.moveWindow(winname, 40, 30)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
