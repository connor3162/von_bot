# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keyboard
import time
from lib.TemplateMatch import TemplateMatcher
from lib.input import InputManager
import ctypes
user32 = ctypes.windll.user32


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_manager = InputManager()
    template_matcher = TemplateMatcher()
    monitor_width = user32.GetSystemMetrics(0)

    while True:  # making a loop
        if keyboard.is_pressed('f4'):  # if key 'q' is pressed
            print("begining in 5 seconds...")
            time.sleep(5)
            while True:
                print("starting new loop..")
                while not template_matcher.ifTemplateExists("target", mask_name="target_mask"):
                    input_manager.tap_key("num0", 0.025)
                print("found target reticle")
                while not template_matcher.ifTemplateExists("purchase_this_plot_for"):
                    input_manager.tap_key("num0", 0.075)
                print("found no button")
                while not template_matcher.ifTemplateExists("hand", mask_name="hand_mask"):
                    input_manager.tap_key("num0", 0.025)
                print("found hand")
                while not template_matcher.ifTemplateExists("hand", mask_name="hand_mask", max_x=monitor_width * .4427
                        , threshold=0.95):
                    input_manager.tap_key("num4", 0.04)
                print("found hand and yes")
                input_manager.tap_key("num0", 0.05)
                if keyboard.is_pressed('f5'):
                    exit()
                print("ending loop!")

0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/