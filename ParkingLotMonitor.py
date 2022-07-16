from ast import While
import os
from pickle import TRUE
from signal import signal
from cv2 import threshold
import pyautogui,time
import cv2 as cv
from PIL import Image, ImageGrab
import numpy as np
import pytesseract
from pytesseract import image_to_string 
from threading import Thread, Timer
import threading
import os

def Main():
    cap = cv.VideoCapture(0)
    while(True):
        ret, frame = cap.read()

        cv.imshow('frame',frame)

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

Main()



