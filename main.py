# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keyboard
import time
from lib.TemplateMatch import TemplateMatcher
from lib.input import InputManager


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_manager = InputManager()
    template_matcher = TemplateMatcher()

    while True:  # making a loop
        if keyboard.is_pressed('f4'):  # if key 'q' is pressed
            print("begining in 5 seconds...")
            time.sleep(5)
            while True:
                print("starting new loop..")
                while not template_matcher.ifTemplateExists("target", "target_mask"):
                    input_manager.tap_key("num0", 0.05)
                if keyboard.is_pressed('f5'):
                    exit()
                input_manager.tap_key("num0", 0.1)
                input_manager.tap_key("num0", 0.5)
                input_manager.tap_key("num0", 0.1)
                input_manager.tap_key("num0", 0.1)
                input_manager.tap_key("num0", 0.1)
                input_manager.tap_key("num4", 0.3)
                input_manager.tap_key("num0", 0.5)
                print("ending loop!")

0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/