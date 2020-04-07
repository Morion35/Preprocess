import numpy as np
import cv2

def line_detection(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)
    cv2.waitKey(0)

    low_yellow = np.array([0, 0, 150]);
    high_yellow = np.array([255, 50, 255]);
    mask = cv2.inRange(hsv, low_yellow, high_yellow)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

    edge = cv2.Canny(mask, 50, 150, apertureSize=3);
    cv2.imshow("edge", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 100, 50)
    if lines is None:
        return
    for line in lines:
        x1, y1, x2, y2 = line[0]
        img = cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2);
    cv2.imshow("lines", img);
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img1 = cv2.imread('road1.png')
img2 = cv2.imread('road2.png')
img3 = cv2.imread('road3.png')

line_detection(img1)
line_detection(img2)
line_detection(img3)
