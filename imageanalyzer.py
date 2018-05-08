from PIL import ImageGrab
import time
import win32api
import numpy as np
import cv2

img_num = 0
screenshots = {}

lower_red = np.array([30, 200, 50])
upper_red = np.array([255, 255, 180])

while len(screenshots) < 30:
    if win32api.GetAsyncKeyState(0x01) < 0:
        name = time.strftime("%H_%M_%S", time.localtime()) + "_" + img_num.__str__() + ".jpg"
        ImageGrab.grab().save(name, "JPEG")
        screenshots[img_num] = name
        img_num += 1
        time.sleep(.4)

img = cv2.imread(screenshots[20])

cv2.imshow("ss", screenshots)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow("mask", mask)