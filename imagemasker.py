import numpy as np
import cv2
from matplotlib import pyplot as plt

lower_red = np.array([150, 0, 0])
upper_red = np.array([255, 140, 200])

img = cv2.imread("14_26_38_20.jpg", cv2.IMREAD_UNCHANGED)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask = cv2.inRange(rgb, lower_red, upper_red)
plt.imshow(mask), plt.show()
plt.imshow(rgb), plt.show()
