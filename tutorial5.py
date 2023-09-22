import numpy as np
import cv2

def rgb_to_hsv(r: int, g: int, b: int):
    return cv2.cvtColor(np.array([b, g, r]), cv2.COLOR_BGR2HSV)[0]

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([70, 255, 180])

    # creates a mask that only keep the pixels in range, others are blacked out
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # bitwising using the mask b/w src1 & src2
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 
    res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame', res)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


