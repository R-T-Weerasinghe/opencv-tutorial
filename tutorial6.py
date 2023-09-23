import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # goodFeaturesToTrack(img, maxCorners, minConfidence, minDistanceBetween2Corners)
    # minDistanceBetween2Corners = to remove duplicates
    corners = cv2.goodFeaturesToTrack(grey, 20, 0.2, 10)
    # floating point corners to int coords [[[x1 y1]] [[x2 y2]] ...]]
    corners = np.intp(corners)

    for corner in corners:
        x, y = corner.ravel() # ravel flattens ; [[x y]] => [x y]
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
            
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            # np.random returns 64bit np ints -> converting to 32bit python ints
            color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
            cv2.line(frame, corner1, corner2, color, 1)

    cv2.imshow('Frame', cv2.flip(frame, 1))
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()