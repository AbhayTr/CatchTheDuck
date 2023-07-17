import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import sys
from threading import Thread

lmx = "I"
lmy = "I"
hs = ""
fh = 0
fw = 0
win_name = "Hand Sensor"

def sensing():
    global lmx
    global lmy
    global hs
    global fh
    global fw
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands = 1, min_detection_confidence = 0.7)
    mpDraw = mp.solutions.drawing_utils

    model = load_model("mp_hand_gesture")

    f = open("gesture.names", "r")
    classNames = f.read().split("\n")
    f.close()

    cap = cv2.VideoCapture(0)
    cv2.namedWindow(win_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        _, frame = cap.read()
        fh, fw, c = frame.shape
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)
        className = ""
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    lmx = int(lm.x * fh)
                    lmy = int(lm.y * fw)
                    landmarks.append([lmx, lmy])
                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = classNames[classID]
        if className == "fist":
            hs = "C"
        else:
            hs = "O"
        cv2.putText(frame, "Go back to the CMD/Terminal/Game window to play the game.", (4, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2, cv2.LINE_AA)
        cv2.imshow(win_name, frame)
        if cv2.waitKey(1) == ord("x"):
            break
    lmx = "X"
    lmy = "X"
    cap.release()
    cv2.destroyAllWindows()

thread = Thread(target = sensing, args = ())
thread.daemon = True
thread.start()