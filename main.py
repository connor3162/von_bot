# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pykeyboard import PyKeyboard
import win32api,win32ui,win32con,win32gui
import keyboard
import time
from random import uniform

k=PyKeyboard()

class VonBot():

    vk = {
        '5': '5', 'c': 'c', 'n': 'n', 'z': 'z', '3': '3', '1': '1', 'd': 'd', '0': '0', 'l': 'l', '8': 208,
        'w': 'w', 'u': 'u', '4': '4', 'e': 'e', '[': '[', 'f': 'f', 'y': 'y', 'x': 'x', 'g': 'g', 'v': 'v',
        'r': 'r', 'i': 'i', 'a': 'a', 'm': 'm', 'h': 'h', '.': '.', ',': ',', ']': ']', '/': '/', '6': '6',
        '2': '2', 'b': 'b', 'k': 'k', '7': '7', 'q': 'q', "'": "'", '\\': 313, 'j': 'j', '`': '`', '9': '9',
        'p': 'p', 'o': 'o', 't': 't', '-': '-', '=': '=', 's': 's', ';': ';', 'tab': k.tab_key, 'enter': k.enter_key,
        'alt': k.alt_key,' ':' ',';':';','ctrl':k.control_key,'esc':k.escape_key,"f1": k.function_keys[1], "f2": k.function_keys[2],
        "f3": k.function_keys[3], "f4": k.function_keys[4], "f5": k.function_keys[5],"f8": k.function_keys[8], "num0" : k.numpad_keys[0],
        "num1": k.numpad_keys[1], "num2" : k.numpad_keys[2], "num3" : k.numpad_keys[3], "num4" : k.numpad_keys[4], "num5" : k.numpad_keys[5],
        "num6": k.numpad_keys[6], "num7" : k.numpad_keys[7], "num8" : k.numpad_keys[8], "num9" : k.numpad_keys[9]
    }

    def tap_key(self, key, t=0.2):
        print("pressed_key:" + key)
        random_wait = uniform(-0.15, 0.15)
        t = t + (t * random_wait)
        k.tap_key(self.vk[key])
        time.sleep(t)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from main import VonBot
    von_bot = VonBot()

    while True:  # making a loop
        if keyboard.is_pressed('f4'):  # if key 'q' is pressed
            print("begining in 5 seconds...")
            time.sleep(5)
            while True:
                random_wait = uniform(0, 0.2)
                random_wait = 1 + random_wait
                time.sleep(random_wait)
                print("starting new loop..")
                if keyboard.is_pressed('f5'):
                    exit()
                von_bot.tap_key("num0", 0.1)
                von_bot.tap_key("num0", 0.5)
                von_bot.tap_key("num0", 0.1)
                von_bot.tap_key("num0", 0.1)
                von_bot.tap_key("num0", 0.1)
                von_bot.tap_key("num4", 0.3)
                von_bot.tap_key("num0", 0.5)
                print("ending loop!")

0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/