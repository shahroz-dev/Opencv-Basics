import cv2
import numpy as np

# getting world perspective of an image to get its bird eye view

img = cv2.imread("Resources/cards.jpg")

width, height = 250, 350  # normal size of card is 2.5x3.5 inch so can set it dimension as 250x350 pixel according to
# their width height ratio

# Create arrays of 4 pts of cards. The pts need to be float32 type for perspective transformation
pts1 = np.array([[111, 219], [287, 188], [154, 482], [352, 440]], np.float32)  # four points of card in image
pts2 = np.array([[0, 0], [width, 0], [0, height], [width, height]], np.float32)  # destination size of card in world
# perspective
matrix = cv2.getPerspectiveTransform(pts1, pts2)  # getting transformation object of world perspective
imgOutput = cv2.warpPerspective(img, matrix, (width, height))  # converting image into world perspective

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
