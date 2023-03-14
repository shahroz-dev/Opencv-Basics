def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContour(mask)
        if x != 0 and y != 0:
            newPoints.append([x, y, 0])  # append all contour points in a single frame
    return newPoints


def getContour(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = (0, 0, 0, 0)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


if __name__ == "__main__":
    import cv2
    import numpy as np

    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 130)

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    videoWriter = cv2.VideoWriter('C:/Users/Muhammad Shahroz/Desktop/video.avi', fourcc, 30.0, (640, 480))

    # define colors threshold in HSV space
    myColors = [[100, 55, 0, 142, 201, 255]]
    # define color for drawing in BGR format
    myColorValues = [[102, 0, 0]]
    # x, y, colorId
    myPoints = []
    newPoints = []

    while True:
        success, img = cap.read()
        imgResult = img.copy()
        newPoints = findColor(img, myColors)
        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)  # append all the contour points in previously success frame
        if len(myPoints) != 0:
            drawOnCanvas(myPoints, myColorValues)  # draw all contour points
        cv2.imshow("Result", imgResult)
        videoWriter.write(imgResult)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    videoWriter.release()
    cv2.destroyAllWindows()
