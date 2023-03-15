import cv2
import numpy as np
from helper import stackImages

#########################
widthImg = 640
heightImg = 480
#########################

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=2)
    imgTh = cv2.erode(imgDilate, kernel, iterations=1)

    return imgTh


def getContour(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))  # reshape from (4,1,2) to (4,2)
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.array(biggest, np.float32)
    pts2 = np.array([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]], np.float32)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgCropped = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))
    return imgCropped


while True:
    success, img = cap.read()
# img = cv2.imread('Resources/1.jpg')
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContour(imgThres)
    if biggest.size != 0:
        imgWarped = getWarp(img, biggest)
        imgArray = ([[img, imgThres], [imgContour, imgWarped]])
        stackedImages = stackImages(0.6, imgArray)
        cv2.imshow("Workflow", stackedImages)
        cv2.imshow("ImageWarped", imgWarped)
    else:
        imgArray = ([[img, imgThres], [img, img]])
        stackedImages = stackImages(0.6, imgArray)
        cv2.imshow("Workflow", stackedImages)
# cv2.waitKey(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
