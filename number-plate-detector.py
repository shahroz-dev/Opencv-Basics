import os
import cv2

#######################################
widthImg = 640
heightImg = 480
numPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255, 0, 255)
path = r"Resources/car-number.jpg"
#######################################

cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)
count = 0

while True:
    img = cv2.imread(path)
    img = cv2.resize(img, (widthImg, heightImg))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = numPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgROI = img[y:y + h, x:x + w]  # region of number plate
            cv2.imshow("Number Plate", imgROI)

    cv2.imshow("Result", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        dest_path = "Resources/Scanned/"
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        cv2.imwrite(dest_path + "NoPlate_" + str(count)+".jpg", imgROI)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, color, 2)
        cv2.imshow("Result", img)
        count += 1
        cv2.waitKey(500)


cap.release()
cv2.destroyAllWindows()
