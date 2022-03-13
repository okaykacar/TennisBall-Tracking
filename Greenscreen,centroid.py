import cv2
import imutils
import numpy as np

def callback_val(x):
    pass

#Tennis ball ((29,86,6), (64, 255, 255))
#Face ((7,67,0), (118, 255, 217))
cap= cv2.VideoCapture(0)
cv2.namedWindow("Term Project")
cv2.createTrackbar("LH", "Term Project", 28, 255, callback_val)
cv2.createTrackbar("UH", "Term Project", 95, 255, callback_val)
cv2.createTrackbar("LS", "Term Project", 65, 255, callback_val)
cv2.createTrackbar("US", "Term Project", 255, 255, callback_val)
cv2.createTrackbar("LV", "Term Project", 178, 255, callback_val)
cv2.createTrackbar("UV", "Term Project", 255, 255, callback_val)


video_file = ''  # proje"  # if given frames are read from file
WIDTH =600# width of the windows
ONLY_MAX = False  # if True only the max circle is drawn



if len(video_file) == 0:
    kamera = cv2.VideoCapture(0)  # default web camera=0
else:
    kamera = cv2.VideoCapture(video_file)  # read from file

cv2.namedWindow('proje')
cv2.moveWindow('proje', 120, 120)  # 'frame' window position

# Write some Text

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    (ok, frame) = kamera.read()

    l_h = cv2.getTrackbarPos("LH", "Term Project")
    l_s = cv2.getTrackbarPos("LS", "Term Project")
    l_v = cv2.getTrackbarPos("LV", "Term Project")

    u_h = cv2.getTrackbarPos("UH", "Term Project")
    u_s = cv2.getTrackbarPos("US", "Term Project")
    u_v = cv2.getTrackbarPos("UV", "Term Project")

    GREEN_RANGE = ((l_h, l_s, l_v), (u_h, u_s, u_v))

    colorLower, colorUpper = GREEN_RANGE  # select color range

    if len(video_file) > 0 and not ok:
        break
    frame = imutils.resize(frame, WIDTH)
    #blur = cv2.GaussianBlur(frame, (1, 1), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=3)
    mask = cv2.dilate(mask, None, iterations=3)

    #kernel = np.ones((5, 5), np.float32) / 25
    #mask = cv2.filter2D(mask, -1, kernel)
    #mask = cv2.blur(mask, (5, 5))
    #mask = cv2.GaussianBlur(mask, (5, 5), 0)
    #mask = cv2.medianBlur(mask, 5)
    #mask = cv2.bilateralFilter(mask, 9, 75, 75)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    mask_copy = mask.copy()
    contours = cv2.findContours(mask_copy, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(contours) > 1:
        for ctr in contours:
            if ONLY_MAX:
                cmax = max(contours, key=cv2.contourArea)
                (x, y), radius = cv2.minEnclosingCircle(cmax)
            else:
                (x, y), radius = cv2.minEnclosingCircle(ctr)
            if radius >= 10:  # draw circle if radius>50 px
                cv2.circle(frame, (int(x), int(y)),
                           int(radius), (0,255, 255), 5)
                # Using cv2.putText() method
                strXY = str(int(x)) + ', ' + str(int(y))
                cv2.putText(frame, strXY, (int(x), int(y)), font, 0.5, (255, 255, 0), 2)

    cv2.imshow("proje", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    key = cv2.waitKey(2
                      ) & 0xFF
    if key == ord('q') or key == 1:
        break
kamera.release()
cv2.destroyAllWindows()
'''
if callback_val(True):
    class greenfinder:
        img = cv2.VideoCapture(0)

        lower_green = np.array ([45, 100, 100])
        upper_green = np.array ([75, 255, 255])
        sensitivity = 15
        lower_green_0 = np.array ([0, 100, 100])
        upper_green_1 = np.array ([180, 255, 255])
        mask_0 = cv2.inRange (img, lower_green_0, lower_green);
        mask_1 = cv2.inRange (img, upper_green, upper_green_1);

        mask = cv2.bitwise_or (mask_0, mask_1)
        cv2.imshow ("Green Pixel", mask)
        cv2.waitKey (0)

if __name__ == "__main__":
    greenfinder()
'''