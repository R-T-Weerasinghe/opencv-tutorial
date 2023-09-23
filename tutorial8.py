import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        # region_of_interest for detecting eye
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w] # this is linked to frame
        eyes = eye_cascade.detectMultiScale(roi_grey, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            ctr_point = ((ex+(ex+ew))//2, (ey+(ey+eh))//2)
            cv2.circle(roi_color, ctr_point, ew//10, (0, 255, 0), -1)

        mouths = mouth_cascade.detectMultiScale(roi_grey, 1.3, 20)
        for (mx, my, mw, mh) in mouths:
            cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 3)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
