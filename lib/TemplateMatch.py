import cv2
import os
import numpy as np
import datetime
import pyautogui
from matplotlib import pyplot as plt


class TemplateMatcher:
    def ifTemplateExists(self, template_name, mask_name: ""):
        # return false if it can't find the template. else return true
        date = str(datetime.date.today())
        time = str(datetime.datetime.now().strftime('%H-%M-%S'))
        dir = os.getcwd() + "/tmp/screenshots/" + date + "/checker"
        if not os.path.exists(dir):
            os.makedirs(dir)
        file = dir + '/' + time + ".jpg"
        pyautogui.screenshot(file)
        screenshot_color = cv2.imread(file)
        res1 = ""
        if not mask_name == "":
            mask = cv2.imread(os.getcwd() + "/templates/" + mask_name + ".png")
            template = cv2.imread(os.getcwd() + "/templates/" + template_name + ".png")
            res1 = cv2.matchTemplate(screenshot_color, template, cv2.TM_CCORR_NORMED, mask=mask)
        else:
            template = cv2.imread(os.getcwd() + "/templates" + template_name + ".png")
            res1 = cv2.matchTemplate(screenshot_color, template, cv2.TM_CCORR_NORMED)

        threshold = 0.99

        plt.imshow(res1, cmap='gray')
        loc1 = np.where(res1 >= threshold)
        os.remove(file)
        if len(loc1[0]) > 0 :
            return True
        else:
            return False
