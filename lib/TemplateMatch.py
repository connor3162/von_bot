import cv2
import os
import numpy as np
import datetime
import pyautogui
from matplotlib import pyplot as plt


class TemplateMatcher:
    def ifTemplateExists(self, template_name, mask_name="", threshold=0.99, max_x=0):
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
            template = cv2.imread(os.getcwd() + "/templates/" + template_name + ".png")
            res1 = cv2.matchTemplate(screenshot_color, template, cv2.TM_CCORR_NORMED)

        plt.imshow(res1, cmap='gray')
        loc1 = np.where(res1 >= threshold)
        os.remove(file)

        if len(loc1[0] > 0):
            if max_x == 0:
                return True
            else:
                for pt in zip(*loc1[::-1]):
                    if pt[0] < max_x:
                        return True
                    else:
                        return False
        else:
            return False
