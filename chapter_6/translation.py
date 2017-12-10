from __future__ import print_function
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#M = np.float32([[1, 0, 25], [0, 1, 50]])
#shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#cv2.imshow("Shifted Down and Right", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)