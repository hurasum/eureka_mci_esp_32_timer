
import display
import time
import machine

class Cup:

    @staticmethod
    def oneCup(tft, x, y):
        tft.rect(x, y, 35, 35, 0xFFFFFF)
        tft.arc(x-2, y+15, 12, 2, 180, 360, 0xFFFFFF)

    @staticmethod
    def endLess(tft, x, y, r):
        tft.circle(x-20, y, r, 0xFFFFFF)
        tft.circle(x+20, y, r, 0xFFFFFF)

class CoffeeGrinder:
    """"""

    def __init__(self):
        """"""
        self.tft = self.initDisplay()
        self.tft.clear()
        self.__initText()
        self.pin_shot = machine.Pin(0, mode=machine.Pin.IN)
        self.pin_start = machine.Pin(2, mode=machine.Pin.IN)
        self.pin_out = machine.Pin(15, mode=machine.Pin.OUT)
        self.pin_sec = machine.Pin(35, mode=machine.Pin.IN)
        self.single_sec = machine.nvs_getint("single_sec")
        self.double_sec = machine.nvs_getint("double_sec")
        self.cup = Cup()

    @staticmethod
    def initDisplay():
        """initialize the display"""
        tft = display.TFT()
        tft.init(tft.ST7789, rst_pin=23, backl_pin=4, miso=0, mosi=19, clk=18, cs=5, dc=16, width=235, height=340,
                 backl_on=1)

        tft.font(tft.FONT_DejaVu18)

        # invert colors
        tft.tft_writecmd(0x21)

        # set orientation (optional)
        tft.orient(tft.PORTRAIT_FLIP)

        # set window size
        tft.setwin(52, 40, 188, 280)
        # x, y -> x2, y2
        tft.rect(0, 0, 135, 240, 0xFFFFFF)
        return tft

    def __textWrapper(self, x, y, text):
        """Function to warp text"""
        self.tft.text(x - self.__textCenterOffset(text), y - self.__textFontSizeOffset(), text, 0xFFFFFF)

    def __initText(self):
        text = "Initialize"
        self.__textWrapper(67, 110, text)
        text = "Coffegrinder"
        self.__textWrapper(67, 130, text)

    def __textCenterOffset(self, text):
        """Center offset"""
        return int(self.tft.textWidth(text) / 2)

    def __textFontSizeOffset(self):
        """Fontsize offset"""
        return int(self.tft.fontSize()[1] / 2)

    def runProgram(self):
        """"""
        if not self.single_sec:
            self.single_sec = 1
        self.single_sec /= 10

        if not self.double_sec:
            self.double_sec = 1
        self.double_sec /= 10

        print_s = 0
        state = 0
        run = True
        while True:
            time.sleep(0.1)
            button_shot = self.pin_shot.value()
            button_sec = self.pin_sec.value()
            self.tft.set_fg(0x000000)
            if not button_shot:
                run = True
                state += 1
                if state >= 3:
                    state = 0

            if state == 0 and run:
                self.tft.clear()
                self.cup.oneCup(self.tft, 57, 90)
                text = "Single Shot!"
                self.__textWrapper(67, 30, text)
                run = False
                print_s = self.single_sec
            elif state == 1 and run:
                self.tft.clear()
                self.cup.oneCup(self.tft, 27, 90)
                self.cup.oneCup(self.tft, 87, 90)
                text = "Double Shot!"
                self.__textWrapper(67, 30, text)
                run = False
                print_s = self.double_sec
            elif state == 2 and run:
                self.tft.clear()
                self.cup.endLess(self.tft, 68, 110, 20)
                text = "Endless!"
                self.__textWrapper(67, 30, text)
                run = False
                print_s = self.double_sec

            if not button_sec and state == 0:
                self.single_sec += 0.1
                if self.single_sec >= 9.9:
                    self.single_sec = 0.1
                time.sleep(0.1)
                machine.nvs_setint("single_sec", int(self.single_sec * 10))
                print_s = self.single_sec
            elif not button_sec and state == 1:
                self.double_sec += 0.1
                if self.double_sec >= 9.9:
                    self.double_sec = 0.1
                time.sleep(0.1)
                machine.nvs_setint("double_sec", int(self.double_sec * 10))
                print_s = self.double_sec

            text = "Seconds: {}".format(round(print_s, 2))
            if state == 2:
                self.tft.textClear(67, 200, text)
            else:
                self.__textWrapper(67, 200, text)

            if not self.pin_start.value():
                self.pin_out.value(True)
                if state != 2:
                    sleep = print_s
                    while sleep > 0:
                        text = "Seconds: {}".format(round(sleep, 2))
                        self.__textWrapper(67, 200, text)
                        sleep -= 0.1
                        time.sleep(0.1)
                else:
                    text = "Grind!"
                    self.__textWrapper(67, 200, text)
                    while not self.pin_start.value():
                        time.sleep(0.01)
                    self.tft.textClear(67, 200, text)
                self.pin_out.value(False)


if __name__ == '__main__':
    s = CoffeeGrinder()
    time.sleep(2)
    s.runProgram()





