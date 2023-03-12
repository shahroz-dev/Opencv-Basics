import cv2
import numpy as np

# In open cv x-axis is at east and y-axis is at south

img = cv2.imread("Resources/lambo.png")
print(img.shape)  # (height, width, channels)

imgResize = cv2.resize(img, (300, 200))  # width, height
# We can increase the image pixel as compared to the original image, but it cannot increase its quality
print(imgResize.shape)

imgCropped = img[0:200, 200:500] # height, width

cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
