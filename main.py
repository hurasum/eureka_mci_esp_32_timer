

import _thread
import display
import time
import machine
from rotary_irq_esp import RotaryIRQ
from rotary import Rotary


class Cup:
    """Class for Displayinig cups"""
    @staticmethod
    def oneCup(tft, x, y):
        """draw single cup"""
        tft.rect(x, y, 35, 35, 0xFFFFFF, fillcolor=0xFFFFFF)
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
        self.encoder_state_machine = RotaryIRQ(13, 12, min_val=0, max_val=2, range_mode=Rotary.RANGE_WRAP)
        self.encoder_grinder_time = None
        self.run = True
        self.update_display = True
        self.print_s = 0.0
        self.state = 0
        self.state_old = 0
        self.edit_state = False
        self.cup = Cup()
        self.single_sec = machine.nvs_getint("single_sec")
        self.double_sec = machine.nvs_getint("double_sec")
        self.seconds = 0.1

        self.pin_start = machine.Pin(
            36,
            mode=machine.Pin.IN,
            handler=self.__startGrinding,
            trigger=machine.Pin.IRQ_RISING,
            acttime=0,
            debounce=500000
        )
        self.pin_sec = machine.Pin(
            2,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.switchState,
            trigger=machine.Pin.IRQ_RISING,
            acttime=0,
            debounce=500000
        )
        self.pin_out = machine.Pin(32, mode=machine.Pin.OUT)

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

    def __textWrapper(self, x, y, text, color=0xFFFFFF):
        """Function to warp text"""
        self.tft.text(x - self.__textCenterOffset(text), y - self.__textFontSizeOffset(), text, color=color)

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
        self.update_display = True
        color = 0xFFFFFF
        if self.edit_state:
            color = 0xFF0000
        text_s = "Seconds: {}\r".format(round(self.print_s, 2))
        qty = round(self.print_s * self.COFFEE_PER_SECOND, 1)
        # x, y = math.modf(qty)
        text_g = "QTY: {} g\r".format(qty)
        if qty < 10:
            # qty = "0{}".format(qty)
            text_g = "QTY:   {} g\r".format(qty)
        if self.state == 2:
            self.tft.textClear(67, 200, text_s)
        else:
            self.__textWrapper(67, 200, text_s, color)
            self.__textWrapper(67, 225, text_g, color)

    def __stateSingeleShot(self):
        """Single shot"""
        self.update_display = True
        self.tft.clear()
        self.cup.oneCup(self.tft, 57, 90)
        text = "Single Shot!"
        self.__textWrapper(67, 30, text)
        self.print_s = self.single_sec
        self.run = False

    def __stateDoubleShot(self):
        """Double Shot"""
        self.update_display = True
        self.tft.clear()
        self.cup.oneCup(self.tft, 27, 90)
        self.cup.oneCup(self.tft, 87, 90)
        text = "Double Shot!"
        self.__textWrapper(67, 30, text)
        self.print_s = self.double_sec
        self.run = False

    def __stateEndlessShot(self):
        """Endless"""
        self.update_display = True
        self.tft.clear()
        self.cup.endLess(self.tft, 68, 110, 20)
        text = "Endless!"
        self.__textWrapper(67, 30, text)
        self.run = False

    def __startGrinding(self, pin):
        """Interrupt routine for grinder start"""
        if self.edit_state:
            return
        self.pin_start.init(trigger=machine.Pin.IRQ_DISABLE)
        self.pin_out.value(True)
        if self.state != 2:
            sleep = self.print_s
            while sleep > 0:
                text = "Seconds: {}".format(round(sleep, 2))
                self.__textWrapper(67, 200, text,  0xec7d15)
                sleep -= 0.1
                time.sleep(0.1)
        else:
            text = "Grind!"
            self.__textWrapper(67, 200, text)
            test = 0
            while not self.pin_start.value():
                time.sleep(0.1)
                test += 0.1
                text_g = "QTY: {} g".format(round(test * self.COFFEE_PER_SECOND, 1))
                self.__textWrapper(67, 225, text_g)
            self.tft.textClear(67, 200, text)
        self.pin_out.value(False)
        self.update_display = True
        self.pin_start.init(trigger=machine.Pin.IRQ_RISING)

    def __setCoffeGrindTime(self, pin):
        """Interrupt routine for set timer"""
        self.update_display = True
        if self.state == 0:
            self.single_sec = self.seconds / 10
            self.print_s = self.single_sec
            machine.nvs_setint("single_sec", int(self.seconds))
        elif self.state == 1:
            self.double_sec = self.seconds / 10
            self.print_s = self.double_sec
            machine.nvs_setint("double_sec", int(self.seconds))

    def switchState(self, pin):
        self.update_display = True
        if self.state == 2:
            self.edit_state = False
            return
        if self.edit_state:
            self.edit_state = False
        elif not self.edit_state:
            self.edit_state = True

        if self.edit_state:
            value = 0.1
            if self.state_old == 0:
                value = self.single_sec
            elif self.state_old == 1:
                value = self.double_sec
            value *= 10
            self.encoder_state_machine.set(value=value, min_val=1, max_val=99, range_mode=Rotary.RANGE_WRAP)
        else:
            self.encoder_state_machine.set(value=self.state_old, min_val=0, max_val=2, range_mode=Rotary.RANGE_WRAP)

    def __shotState(self):
        """Interrupt routine for States"""
        self.state_old = self.encoder_state_machine.value()
        while True:
            ntf = _thread.wait(10)
            if ntf == _thread.EXIT:
                # Terminate the thread
                return
            if not self.edit_state:
                self.state = self.encoder_state_machine.value()
                if self.state_old != self.state:
                    self.run = True
                    self.state_old = self.state
            else:
                self.seconds = self.encoder_state_machine.value()
            if ntf == 1:
                print('s =', self.seconds)
                print('st =', self.state)
                print('so =', self.state_old)

    def runProgram(self):
        """Run Main Program"""

        if not self.single_sec:
            self.single_sec = 1
        self.single_sec /= 10

        if not self.double_sec:
            self.double_sec = 1
        self.double_sec /= 10

        self.tft.set_fg(0x000000)

        shot_state_th = _thread.start_new_thread("Shot_state", self.__shotState, ())
        while True:
            _thread.notify(shot_state_th, 1)
            if self.state == 0 and self.run:
                self.__stateSingeleShot()
            elif self.state == 1 and self.run:
                self.__stateDoubleShot()
            elif self.state == 2 and self.run:
                self.__stateEndlessShot()
            if self.edit_state:
                self.__setCoffeGrindTime(1)
            if self.update_display:
                self.__showCoffeData()
                self.update_display = False
            time.sleep(0.05)



if __name__ == '__main__':
    s = CoffeeGrinder()
    time.sleep(1)
    s.runProgram()



