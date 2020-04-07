import numpy as np
import cv2

def line_detection(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([18, 94, 140]);
    high_yellow = np.array([48, 255, 255]);
    cv2.imshow("hsv", hsv)
    cv2.waitKey(0)

    mask = cv2.inRange(hsv, low_yellow, high_yellow)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

    edge = cv2.Canny(mask, 50, 150, apertureSize=3);
    cv2.imshow("edge", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 50, 100, 10)
    if lines is None:
        return
    for line in lines:
        x1, y1, x2, y2 = line[0]
        img = cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2);
    cv2.imshow("lines", img);
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img1 = cv2.imread('frame_40_gas_0.4_dir_0.0.jpg')
img2 = cv2.imread('frame_122_gas_0.4_dir_-0.27542755839822025.jpg')
img3 = cv2.imread('frame_281_gas_0.4_dir_-0.1778642936596218.jpg')

line_detection(img1)
line_detection(img2)
line_detection(img3)
