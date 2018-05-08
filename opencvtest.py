import numpy as np
import cv2
import math
import time
import sorting_contours

vid = cv2.VideoCapture("testvid.mp4")

#out = cv2.VideoWriter('baw.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 60, (19, 23))

width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

while vid.isOpened():
    ret, frame = vid.read()
    #print(frame[595, 1202])
    #frame[595,1202] = [0,0,0]
    lower = np.array([175, 175, 150])
    upper = np.array([255, 255, 255])

    if ret==True:
        frame = frame[int(math.ceil(.820083*height)):int(math.ceil(.85416*height)), int(math.ceil(.92812*width)):int(math.ceil(.94296*width))]
        mask = cv2.inRange(frame, lower, upper)
        kernel = np.ones((3, 3), np.uint8)
        #closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        #opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        dilation = cv2.dilate(mask, kernel, iterations = 1)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = np.float32(gray)

        #dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        #corners = cv2.goodFeaturesToTrack(gray,25,0.1,5)
        #corners = np.int0(corners)

        #dst = cv2.dilate(dst, None)

        #frame[dst > 0.01 * dst.max()] = [0, 0, 255]

        #for i in corners:
            #x,y = i.ravel()
            #cv2.circle(frame,(x,y),3,255,-1)
        image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(dilation, contours, -1, (255, 0, 255), 1)

        #for c in cnts:
            #(x, y, w, h) = cv2.boundingRect(c)

          #  if (w >= 11) and (h >= 20 and h <= 30):
#                digitcnts.append(c)
        #out.write(img)
        cv2.imshow("frame", img)
        #if len(contours) >= 1:
         #   for c in contours:
          #      if cv2.arcLength(c, True) > cv2.arcLength(contours[0], True):
           #         contours[0] = c
            #cnt = contours[0]
            #print(cv2.arcLength(cnt, True))
        #time.sleep(.15)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()
