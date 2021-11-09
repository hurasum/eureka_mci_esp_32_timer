

import _thread
import display
import time
import machine
import timer
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
    CPS_DEFAULT = 167

    def __init__(self):
        """Init"""
        machine.WDT(True)
        self.tft = self.initDisplay()
        self.tft.clear()
        self.encoder_state_machine = RotaryIRQ(25, 26, min_val=0, max_val=2, reverse=True, range_mode=Rotary.RANGE_WRAP)
        self.encoder_grinder_time = None
        self.run = True
        self.update_display = True
        self.print_s = 0.0
        self.encoder_value = 0
        self.state = 0
        self.state_old = 0
        self.edit_state = False
        self.cup = Cup()
        self.single_sec = machine.nvs_getint("single_sec")
        self.double_sec = machine.nvs_getint("double_sec")
        self.cps = machine.nvs_getint("cps")
        self.seconds = 0.1
        self.edit_cps = False
        self.pin_start = machine.Pin(
            33,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.__startGrinding,
            trigger=machine.Pin.IRQ_HILEVEL,
            acttime=0,
            debounce=500000
        )
        self.pin_menu = machine.Pin(
            27,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.setCPS,
            trigger=machine.Pin.IRQ_FALLING,
            acttime=0,
            debounce=500000
        )
        self.pin_out = machine.Pin(32, mode=machine.Pin.INOUT)
        self.pin_out.value(False)

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
        time.sleep(4)

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
        text_s = "Timer: {} \r".format(round(self.print_s, 3))
        if self.print_s < 10:
            text_s = "Timer:   {} \r".format(round(self.print_s, 3))
        qty = round(self.print_s * self.cps, 2)
        text_g = "QTY: {} g\r".format(qty)
        if qty < 10:
            text_g = "QTY:   {} g\r".format(qty)
        self.tft.textClear(67, 200, text_s, color)
        if self.state != 2:
            self.__textWrapper(67, 200, text_s, color)
            self.__textWrapper(67, 225, text_g, color)

    def __stateSingeleShot(self):
        """Single shot"""
        self.pin_start = machine.Pin(
            33,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.__startGrinding,
            trigger=machine.Pin.IRQ_HILEVEL,
            acttime=0,
            debounce=500000
        )
        self.update_display = True
        self.tft.clear()
        self.cup.oneCup(self.tft, 57, 90)
        text = "Single Shot!"
        self.__textWrapper(67, 30, text)
        self.print_s = self.single_sec
        self.run = False

    def __stateDoubleShot(self):
        """Double Shot"""
        self.pin_start = machine.Pin(
            33,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.__startGrinding,
            trigger=machine.Pin.IRQ_HILEVEL,
            acttime=0,
            debounce=500000
        )
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
        self.pin_start = machine.Pin(
            33,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.__startGrinding,
            trigger=machine.Pin.IRQ_HILEVEL,
            acttime=0,
            debounce=500000
        )
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
        self.pin_menu.init(trigger=machine.Pin.IRQ_DISABLE)
        time.sleep(0.1)
        if not self.pin_start.value():
            self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)
            self.pin_start.init(trigger=machine.Pin.IRQ_HILEVEL)
            return
        period = self.print_s*1000
        hw_timer = timer.TM()
        self.pin_out.value(True)
        if self.state != 2:
            hw_timer.init(period=period, mode=timer.TM.ONE_SHOT)
            while hw_timer.isrunning():
                sleep_count = period - (hw_timer.value() / 1000)
                text = "Seconds: {}".format(round(sleep_count, 2))
                self.__textWrapper(67, 200, text, 0xec7d15)
                time.sleep(0.1)
            # start_time = time.time()
            # end_time = 0
            # count = 0
            # while True:
            #     sleep_count = period - end_time
            #     text = "Seconds: {}".format(round(sleep_count, 2))
            #     if count % 10 == 0:
            #         self.__textWrapper(67, 200, text, 0xec7d15)
            #     time.sleep(0.01)
            #     count += 1
            #     end_time = time.time() - start_time
            #     if end_time < period:
            #         break
        else:
            text = "Grind!"
            self.__textWrapper(67, 200, text)
            hw_timer.init(period=period, mode=timer.TM.CHRONO)
            time.sleep(0.1)
            while self.pin_start.value():
                count = hw_timer.value() * 100000
                qty = round(count * self.cps, 1)
                text_g = "QTY: {} g".format(qty)
                if qty < 10:
                    text_g = "QTY:   {} g\r".format(qty)
                self.__textWrapper(67, 225, text_g)
                time.sleep(0.1)
            self.__textWrapper(67, 200, "\r             ")
        self.pin_out.value(False)
        print(self.pin_out.value())
        self.update_display = True
        time.sleep(1)
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)
        self.pin_start.init(trigger=machine.Pin.IRQ_HILEVEL)

    def __setCoffeGrindTime(self, pin):
        """Interrupt routine for set timer"""
        self.update_display = True
        if self.state == 0:
            self.single_sec = self.seconds / 20
            self.print_s = self.single_sec
            machine.nvs_setint("single_sec", int(self.seconds))
        elif self.state == 1:
            self.double_sec = self.seconds / 20
            self.print_s = self.double_sec
            machine.nvs_setint("double_sec", int(self.seconds))

    def switchState(self, pin):
        """Switch state on button press"""
        self.pin_menu.init(trigger=machine.Pin.IRQ_DISABLE)
        self.update_display = True
        if self.state == 2:
            self.edit_state = False
            self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)
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
            value *= 20
            self.encoder_state_machine.set(value=value, min_val=1, max_val=360, range_mode=Rotary.RANGE_WRAP)
        else:
            self.encoder_state_machine.set(value=self.state_old, min_val=0, max_val=2, range_mode=Rotary.RANGE_WRAP)
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)

    def setCPS(self, pin):
        self.pin_menu.init(trigger=machine.Pin.IRQ_DISABLE)
        self.edit_cps = True

    def editCPS(self):
        self.encoder_state_machine.set(value=self.cps*100, min_val=100, max_val=200, range_mode=Rotary.RANGE_WRAP)
        self.tft.clear()
        text = "Set CPS"
        self.__textWrapper(67, 110, text)
        time.sleep(1.0)
        while True:
            self.cps = self.encoder_value / 100
            text = "CPS:   {}\r".format(round(self.cps, 2))
            self.__textWrapper(67, 130, text, 0xec7d15)
            if not self.pin_menu.value():
                print(self.pin_menu.value())
                break
            time.sleep(0.1)
        machine.nvs_setint("cps", int(self.cps * 100))
        self.encoder_state_machine.set(value=0, min_val=0, max_val=2, range_mode=Rotary.RANGE_WRAP)
        self.tft.clear()
        self.edit_cps = False
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING, handler=self.switchState)

    def __getEncoderValue(self):
        """Thread for fast polling encoder value"""
        while True:
            ntf = _thread.wait(0)
            if ntf == _thread.EXIT:
                # Terminate the thread
                return
            self.encoder_value = self.encoder_state_machine.value()
            time.sleep(0.001)

    def __shotState(self):
        """Thread for checking states"""
        self.state_old = self.encoder_value
        while True:
            ntf = _thread.wait(50)
            if ntf == _thread.EXIT:
                # Terminate the thread
                return
            if not self.edit_state:
                self.state = self.encoder_value
                if self.state_old != self.state:
                    self.run = True
                    self.state_old = self.state
            else:
                self.seconds = self.encoder_value

    def runProgram(self):
        """Run Main Program"""

        if not self.single_sec:
            self.single_sec = 1
        self.single_sec /= 20

        if not self.double_sec:
            self.double_sec = 1
        self.double_sec /= 20

        if not self.cps:
            self.cps = self.CPS_DEFAULT
        self.cps /= 100

        self.tft.set_fg(0x000000)

        self.shot_state_th = _thread.start_new_thread("Shot_state", self.__shotState, ())
        _thread.start_new_thread("t", self.__getEncoderValue, ())
        self.__initText()
        if self.edit_cps:
            self.editCPS()
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING, handler=self.switchState)
        # self.__stateSingeleShot()
        self.state = 0
        self.run = True
        while True:
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
            time.sleep(0.1)


if __name__ == '__main__':
    s = CoffeeGrinder()
    s.runProgram()



