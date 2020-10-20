
import display
import time
import machine


class Cup:
    """Class for Displayinig cups"""
    @staticmethod
    def oneCup(tft, x, y):
        """draw single cup"""
        tft.rect(x, y, 35, 35, 0xFFFFFF)
        tft.arc(x-2, y+15, 12, 2, 180, 360, 0xFFFFFF)

    @staticmethod
    def endLess(tft, x, y, r):
        """draw endles sign"""
        tft.circle(x-20, y, r, 0xFFFFFF)
        tft.circle(x+20, y, r, 0xFFFFFF)

class CoffeeGrinder:
    """CoffeeGrinder Class"""
    COFFEE_PER_SECOND = 2.0

    def __init__(self):
        """Init"""
        self.tft = self.initDisplay()
        self.tft.clear()
        self.__initText()
        self.run = True
        self.update_display = True
        self.print_s = 0.0
        self.state = 0
        self.cup = Cup()
        self.single_sec = machine.nvs_getint("single_sec")
        self.double_sec = machine.nvs_getint("double_sec")
        self.pin_shot_state = machine.Pin(
            0,
            mode=machine.Pin.IN,
            handler=self.__shotState,
            trigger=machine.Pin.IRQ_RISING,
            debounce=500000
        )
        self.pin_shot_rotation = machine.Pin(12, mode=machine.Pin.IN)
        self.pin_start = machine.Pin(
            2,
            mode=machine.Pin.IN,
            handler=self.__startGrinding,
            trigger=machine.Pin.IRQ_RISING
        )
        self.pin_sec = machine.Pin(
            35,
            mode=machine.Pin.IN,
            handler=self.__setCoffeGrindTime,
            trigger=machine.Pin.IRQ_RISING
        )
        self.pin_out = machine.Pin(15, mode=machine.Pin.OUT)

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
        """Init Text"""
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

    def __showCoffeData(self):
        """Show Display Data"""
        self.update_display = False
        text_s = "Seconds: {}".format(round(self.print_s, 2))
        if self.state == 2:
            self.tft.textClear(67, 200, text_s)
        else:
            self.__textWrapper(67, 200, text_s)
            text_g = "QTY: {} g".format(round(self.print_s * self.COFFEE_PER_SECOND, 1))
            self.__textWrapper(67, 225, text_g)

    def __stateSingeleShot(self):
        """Single shot"""
        self.tft.clear()
        self.cup.oneCup(self.tft, 57, 90)
        text = "Single Shot!"
        self.__textWrapper(67, 30, text)
        self.print_s = self.single_sec
        self.run = False

    def __stateDoubleShot(self):
        """Double Shot"""
        self.tft.clear()
        self.cup.oneCup(self.tft, 27, 90)
        self.cup.oneCup(self.tft, 87, 90)
        text = "Double Shot!"
        self.__textWrapper(67, 30, text)
        self.print_s = self.double_sec
        self.run = False

    def __stateEndlessShot(self):
        """Endless"""
        self.tft.clear()
        self.cup.endLess(self.tft, 68, 110, 20)
        text = "Endless!"
        self.__textWrapper(67, 30, text)
        self.run = False

    def __startGrinding(self, pin):
        """Interrupt routine for grinder start"""
        self.pin_out.value(True)
        if self.state != 2:
            sleep = self.print_s
            while sleep > 0:
                text = "Seconds: {}".format(round(sleep, 2))
                self.__textWrapper(67, 200, text)
                sleep -= 0.1
                time.sleep(0.1)
        else:
            text = "Grind!"
            self.__textWrapper(67, 200, text)
            # test = 0
            while not self.pin_start.value():
                time.sleep(0.01)
                # test += 0.01
                # text_g = "QTY: {} g".format(round(test * self.COFFEE_PER_SECOND, 1))
                # self.__textWrapper(67, 225, text_g)
            self.tft.textClear(67, 200, text)
        self.pin_out.value(False)

    def __setCoffeGrindTime(self, pin):
        """Interrupt routine for set timer"""
        self.update_display = True
        if self.state == 0:
            self.single_sec = self.__countGrindSeconds(self.single_sec)
            self.print_s = self.single_sec
            machine.nvs_setint("single_sec", int(self.single_sec * 10))
        elif self.state == 1:
            self.double_sec = self.__countGrindSeconds(self.double_sec)
            self.print_s = self.double_sec
            machine.nvs_setint("double_sec", int(self.double_sec * 10))

    @staticmethod
    def __countGrindSeconds(seconds):
        """Sum time"""
        seconds += 0.1
        if seconds >= 9.9:
            seconds = 0.1
        return seconds

    def __shotState(self, pin):
        """Interrupt routine for States"""
        self.run = True
        self.update_display = True
        self.state += 1
        if self.pin_shot_rotation.value():
            pass
        # else:
        #     self.state -= 1
        if self.state >= 3:
            self.state = 0
        elif self.state <= -1:
            self.state = 2

    def runProgram(self):
        """Run Main Program"""
        if not self.single_sec:
            self.single_sec = 1
        self.single_sec /= 10

        if not self.double_sec:
            self.double_sec = 1
        self.double_sec /= 10

        self.tft.set_fg(0x000000)

        while True:
            time.sleep(0.1)
            if self.state == 0 and self.run:
                self.__stateSingeleShot()
            elif self.state == 1 and self.run:
                self.__stateDoubleShot()
            elif self.state == 2 and self.run:
                self.__stateEndlessShot()
            # if self.update_display:
            self.__showCoffeData()


if __name__ == '__main__':
    s = CoffeeGrinder()
    time.sleep(1)
    s.runProgram()



