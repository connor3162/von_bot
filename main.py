# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keyboard
import time
from lib.TemplateMatch import TemplateMatcher
from lib.input import InputManager
from lib.buyLoop import BuyLoop
import ctypes
user32 = ctypes.windll.user32

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        input_manager = InputManager()
        template_matcher = TemplateMatcher()
        boy_loop = BuyLoop(input_manager, template_matcher)
        monitor_width = user32.GetSystemMetrics(0)
    
        while True:  # making a loop
            if keyboard.is_pressed('f4'):  # if the 'F4' key is pressed
                print("begining in 5 seconds...")
                time.sleep(5)
                while True:
                    try:
                        ret = boy_loop()
                    except Exception as ex:
                        print(ex)
                        input("test")