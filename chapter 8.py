import cv2
import numpy as np
from helper import stackImages


# contour is an outline representing or bounding the shape

def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # return only extreme outer
    # contour
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # -1 is to draw all contours points, otherwise it
            # will draw individual contour with index, 3 is thickness
            peri = cv2.arcLength(cnt, True)  # Used to calculate the perimeter of the contour.
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # getting corner points of shape, 0.02*peri is
            # precision parameter which is tunable
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)  # get the rectangle parameters around each object

            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4:
                aspRatio = w / float(h)  # to check if it is square or rectangle
                if 0.95 < aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circle"
            else:
                objectType = "None"
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0))
            cv2.putText(imgContour, objectType, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX,
                        0.5, (0, 0, 0), 2)


path = "Resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()

# convert it into grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContour(imgCanny)
# imgBlank = np.zeros((img.shape[0], img.shape[1], img.shape[2]))
# OR
imgBlank = np.zeros_like(img)

imgStack = stackImages(0.6, ([[img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]]))

cv2.imshow("Stack Images", imgStack)

# cv2.imshow("Original Image", img)
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
