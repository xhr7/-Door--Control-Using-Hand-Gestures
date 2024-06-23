import cv2

import mediapipe as mp

from math import hypot

from pyfirmata2 import Arduino, util

import numpy as np



cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands

hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils



board = Arduino('/dev/cu.usbmodem2017_2_251')

servo_pin = 6

servo = board.get_pin(f'servo:{servo_pin}:s')



lmList = []



while True:

    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



    results = hands.process(imgRGB)



    lmList = []

    if results.multi_hand_landmarks:

        for handlandmark in results.multi_hand_landmarks:

            for id, lm in enumerate(handlandmark.landmark):

                h, w, _ = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)

                lmList.append([id, cx, cy])

            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)



    if lmList:

        x1, y1 = lmList[4][1], lmList[4][2]  # thumb

        x2, y2 = lmList[8][1], lmList[8][2]  # index finger



        length = hypot(x2 - x1, y2 - y1)



        angle = np.interp(length, [30, 350], [0, 180])

        print(angle, int(length))

        servo.write(angle)

        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 4)

        servo_bar = np.interp(angle, [0, 180], [400, 150])

        cv2.rectangle(img, (50, int(servo_bar)), (85, 400), (0, 0, 255), cv2.FILLED)

        cv2.putText(img, f"Servo Angle: {int(angle)}", (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)



    cv2.imshow('Image', img)



    if cv2.waitKey(1) == ord('q'):

        break



cap.release()

cv2.destroyAllWindows()

board.exit()

