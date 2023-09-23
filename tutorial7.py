import numpy as np
import cv2

# ! base image and template should have the same scale
# ! if we are seeking a 5x5 ball in a base, template must be 5x5
# detection is done by convolution - sliding
img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/ball.PNG', 0)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    # use the method that gives the best match for the situation
    img2 = img.copy()
    res = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        # min is the best
        loc = min_loc
    else:
        # max is the best
        loc = max_loc
    bot_right = (loc[0] + w, loc[1] + h)
    cv2.rectangle(img2, loc, bot_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
