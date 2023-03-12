import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

# converting image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting RGB img to GRAY color
# Blur the gray image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # kernel size should be an odd number like (7,7) with sigma(variance) 0
# Edge Detector
imgCanny = cv2.Canny(img, 150, 200)  # 150, 200 representing the threshold to get the edge of specific intensity
# Image Dilation
kernel = np.ones((5, 5), np.uint8)  # Creating 5x5 kernel of 1's with unsigned integer 8 bit type (0 to 255 range)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)  # some edges are not detected as a proper lines due to the
# gaps in between them which can be avoided using image dilation A kernel(a matrix of odd size(3,5,7) is convolved
# with the image. A pixel element in the original image is ‘1’ (i.e. white color) if at least one pixel under the
# kernel is ‘1’. It increases the white region in the image or the size of the foreground object increases iterations
# is how many we look into the image for this purpose which results in the increase of the thickness of white objects
# Image Eroded
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
# A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel are 1,
# otherwise, it is eroded (made to zero). Thus, all the pixels near the boundary will be discarded depending upon the
# size of the kernel. So the thickness or size of the foreground object decreases or simply the white region
# decreases in the image.

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
