import cv2
import numpy as np
from helper import stackImages

img = cv2.imread("Resources/lena.png")


# # stack image horizontally with itself
# imgHor = np.hstack((img, img))
# cv2.imshow("Horizontal", imgHor)
#
# # stack image vertically with itself
# imgVer = np.vstack((img, img))
# cv2.imshow("Vertical", imgVer)

# So there is some limitation with this method.
# We cannot resize the image
# If images are different channels one is RGB and the other is Gray then we cannot use this

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgStack = stackImages(0.5, ([[img, imgGray, img], [img, img, img]]))  # stack images with image scale 0.5.
print(imgStack.shape, imgGray.shape)
cv2.imshow("ImageStack", imgStack)

cv2.waitKey(0)
