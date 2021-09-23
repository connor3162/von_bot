import cv2
import os
import numpy as np
import datetime
import pyautogui


class TemplateMatcher:
    def ifTemplateExists(self, template_path):
        # return false if it can't find the template. else return true
        print("test")
        date = str(datetime.date.today())
        time = str(datetime.datetime.now().strftime('%H-%M-%S'))
        print(time)
        dir = os.getcwd() + "/tmp/screenshots/" + date + "/checker"
        if not os.path.exists(dir):
            os.makedirs(dir)
        file = dir + '/' + time + ".jpg"
        pyautogui.screenshot(file)
        screenshot_color = cv2.imread(file)