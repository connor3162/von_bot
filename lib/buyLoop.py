import time
import ctypes

from lib.TemplateMatch import TemplateMatcher
from lib.input import InputManager

user32 = ctypes.windll.user32

class BuyLoop:
    def __init__(self, input_manager: InputManager, template_matcher: TemplateMatcher):
        self.input_manager = input_manager
        self. template_matcher = template_matcher


    def buy_loop(self, time_to_wait=2):
        monitor_width = user32.GetSystemMetrics(0)
        try:
            start = time.time()
            print("starting new loop..")
            while not self.template_matcher.ifTemplateExists("target", mask_name="target_mask"):
                if start + time_to_wait > time.time():
                    self.input_manager.tap_key("esc")
                self.input_manager.tap_key("num0", 0.001)
                print("looking for reticle")
            print("found target reticle")
            self.input_manager.tap_key("num0", 0.001)
            while not self.template_matcher.ifTemplateExists("hand", mask_name="hand_mask"):
                print("looking for hand")
                self.input_manager.tap_key("num0", 0.001)
            self.input_manager.tap_key("num0", 0.001)
            self.input_manager.tap_key("num0", 0.001)
            self.input_manager.tap_key("num4", 0.2)
            while not self.template_matcher.ifTemplateExists("hand", mask_name="hand_mask", max_x=monitor_width \
                                                                                             * .4427, threshold=0.95):
                print('looking for hand and the yes')
            print("found hand and yes")
            self.input_manager.tap_key("num0", 0.00)
            print("ending loop!")
        except Exception as ex:
            print(ex)
            input("test")