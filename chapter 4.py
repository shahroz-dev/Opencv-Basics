import cv2
import numpy as np

cv2.destroyAllWindows()
# We will create a matrix of zeros(i.e. black)

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# img[100:200, 100:200, :] = (255, 0, 0)  # (255,0,0) is a RGB color value for blue assign to a block in a image
# cv2.imshow("Image1", img) img[:] = (255, 0, 0)  # converting the whole image in blue color cv2.imshow("Image2",
# img) img[:] = (0, 0, 0)  # converting back to black color cv2.imshow("Image3", img) Draw a line on original image
# from pt1 (0,0)(width, height) to pt2 (300,300)(width, height) with RGB color value of (0,255,0) and thickness 3
# img1 = np.copy(img)
# cv2.line(img1, (0, 0), (300, 300), (0, 255, 0), 3)
# cv2.imshow("Image4", img1)
# Draw a diagonal line on original image from 2 corner points
# img2 = np.copy(img)
cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (255, 255, 0), 3)
# cv2.imshow("Image5", img)
# Draw rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)  # from corner pt1 (0,0) to corner pt2 (250, 300) with RGB
# color value (0, 0, 255) and thickness 2
# cv2.imshow("Image6", img)
# draw filled rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# cv2.imshow("Image7", img)
# draw circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)  # center pt, radius, RGB color value, thickness
cv2.imshow("Image", img)
# Write text
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)  # text, origin pt of text(width,
# height), font style, scale, color, thickness
cv2.imshow("Image", img)
cv2.waitKey(0)
