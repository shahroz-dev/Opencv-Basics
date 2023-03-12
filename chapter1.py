import cv2

print("Package Imported")

# Read an image

img = cv2.imread("Resources/lena.png")

cv2.imshow("Output", img)  # "Output" is label of image
cv2.waitKey(0)  # any integer value greater than 1 represent milliseconds i.e. 1000 = 1 sec and 0 means delay of in
# infinite time

# Creating Video Capture object
cap = cv2.VideoCapture(0)  # get video stream using webcam. Can be path of video as well.
# We can set width and height of images as well
cap.set(3, 640)  # width can be set with id 3
cap.set(4, 480)  # height can be set with id 4
cap.set(10, 100)  # we can change brightness from 0 to 100 as an intensity with id 10
# Video is a sequence of images

while True:
    success, img = cap.read()  # success is a boolean array against each image frame representing weather we are able to
    # capture the frame
    cv2.imshow("Video", img)
    key = cv2.waitKey(1) & 0xFF  # The 0xFF in this scenario is representing binary 11111111 an 8 bit binary, since we
    # only require 8 bits to represent a character we AND waitKey(1) to 0xFF with a time duration of 1 ms wait to
    # check if keyboard input occur . As a result, an integer is obtained below 255.
    if key == ord('q'):  # check if q is pressed to end the video stream. ord() is to get the unicode value of character
        break
