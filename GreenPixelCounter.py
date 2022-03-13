'''
This program is not working completely I'm sorry about it because it's my fault.
This program have to worked for Count the greenPixels on webcam but it is not working very well.

Thank you

Sincerely,
Okay Kacar


'''



import cv2
import numpy as np
class greenfinder():
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