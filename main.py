"""
New Version :)
"""


import _thread
import display
import time
import machine
from rotary_irq_esp import RotaryIRQ
from rotary import Rotary


class RotaryEncoder:
    """Rotary Encoder config"""
    def __init__(self):
        self.encoder_state_machine = RotaryIRQ(25, 26, min_val=0, max_val=2, reverse=True, range_mode=Rotary.RANGE_WRAP)
        self.value = 1
        _thread.start_new_thread("getEncoderValue", self.__getEncoderValue, ())

    def setTime(self, value):
        """Set Encoder to time config"""
        self.encoder_state_machine.set(value=value, min_val=1, max_val=360, range_mode=Rotary.RANGE_WRAP)

    def setState(self, value):
        """Set Encoder to state config"""
        self.encoder_state_machine.set(value=value, min_val=0, max_val=2, range_mode=Rotary.RANGE_WRAP)

    def setCPS(self, value):
        """Set Encoder to CPS config"""
        self.encoder_state_machine.set(value=value, min_val=100, max_val=200, range_mode=Rotary.RANGE_WRAP)

    def __getEncoderValue(self):
        """Thread for fast polling encoder value"""
        while True:
            ntf = _thread.wait(0)
            if ntf == _thread.EXIT:
                # Terminate the thread
                return
            self.value = int(self.encoder_state_machine.value())
            time.sleep(0.001)


class SingleState:
    """Single State class"""
    def __init__(self):
        self.STATE = 0
        self.TEXT = "Single Shot!"
        self.VALUE = 1

    @property
    def SECONDS(self):
        return self.VALUE / 20


class DoubleState:
    """Double State class"""
    def __init__(self):
        self.STATE = 1
        self.TEXT = "Double Shot!"
        self.VALUE = 1

    @property
    def SECONDS(self):
        return self.VALUE / 20


class EndlessState:
    """Endless State class"""
    def __init__(self):
        self.STATE = 2
        self.TEXT = "Endless!"


class States:
    """States class"""
    def __init__(self, machine_main, display_main, pin_menu, encoder):
        self.single = SingleState()
        self.double = DoubleState()
        self.endless = EndlessState()
        #
        self.encoder_state_machine = encoder
        self.uc = machine_main
        self.display = display_main
        self.pin_menu = pin_menu
        self.state = self.double.STATE
        self.edit_state = False
        self.state_old = 0
        self.run = True
        self.edit_cps = False
        self.cps = 2

    def startCheckStatesThread(self):
        """Start thread"""
        _thread.start_new_thread("__checkStates", self.__checkStates, ())

    def __checkStates(self):
        """Thread for checking states"""
        self.state_old = self.encoder_state_machine.value
        while True:
            ntf = _thread.wait(50)
            if ntf == _thread.EXIT:
                # Terminate the thread
                return
            value = self.encoder_state_machine.value
            if self.edit_state:
                if self.state == self.single.STATE:
                    self.single.VALUE = value
                elif self.state == self.double.STATE:
                    self.double.VALUE = value
            else:
                self.state = value
                if self.state_old != self.state:
                    self.run = True
                    self.state_old = self.state

    def editCPS(self):
        """Edit CPS"""
        self.encoder_state_machine.setCPS(self.cps*100)
        self.display.lib.clear()
        self.display.textWrapper(67, 110, "Set CPS")
        time.sleep(1.0)
        while True:
            self.cps = self.encoder_state_machine.value / 100
            text = "CPS:   {:.2f}\r".format(round(self.cps, 3))
            self.display.textWrapper(67, 130, text, 0xec7d15)
            if not self.pin_menu.value():
                break
            time.sleep(0.1)
        self.encoder_state_machine.setState(value=self.double.STATE)
        self.edit_cps = False
        self.display.lib.clear()

    def runState(self, state, function_cup):
        """run state function"""
        self.display.update = True
        self.display.lib.clear()
        function_cup()
        self.display.textWrapper(67, 30, state.TEXT)
        self.run = False


class DisplayFunctions:
    """Display  functions"""
    def __init__(self):
        self.lib = display.TFT()
        self.initDisplay()
        self.update = True

    def initDisplay(self):
        """initialize the display"""
        self.lib.init(
            self.lib.ST7789,
            rst_pin=23,
            backl_pin=4,
            miso=0,
            mosi=19,
            clk=18,
            cs=5,
            dc=16,
            width=235,
            height=340,
            backl_on=1
        )

        self.lib.font(self.lib.FONT_DejaVu18)

        # invert colors
        self.lib.tft_writecmd(0x21)

        # set orientation (optional)
        self.lib.orient(self.lib.PORTRAIT_FLIP)

        # set window size
        self.lib.setwin(52, 40, 188, 280)
        # x, y -> x2, y2
        self.lib.rect(0, 0, 135, 240, 0xFFFFFF)

    def doubleCup(self):
        """draw 2 cups"""
        self.__cup(27, 90)
        self.__cup(87, 90)

    def singleCup(self):
        """draw single cup"""
        self.__cup(57, 90)

    def endLess(self, x=68, y=110, r=20):
        """draw endles sign"""
        self.lib.circle(x-20, y, r, 0xFFFFFF)
        self.lib.circle(x+20, y, r, 0xFFFFFF)

    def __cup(self, x, y):
        """draw single cup"""
        self.lib.rect(x, y, 35, 35, 0xFFFFFF, fillcolor=0xFFFFFF)
        self.lib.arc(x-2, y+15, 12, 2, 180, 360, 0xFFFFFF)

    def textWrapper(self, x, y, text, color=0xFFFFFF):
        """Function to warp text"""
        self.lib.text(x - self.__textCenterOffset(text), y - self.__textFontSizeOffset(), text, color=color)

    def initText(self):
        """Init Text"""
        self.lib.set_fg(0x000000)  # background color
        text = "Initialize"
        self.textWrapper(67, 110, text)
        text = "Coffegrinder"
        self.textWrapper(67, 130, text)
        time.sleep(4)

    def __textCenterOffset(self, text):
        """Center offset"""
        return int(self.lib.textWidth(text) / 2)

    def __textFontSizeOffset(self):
        """Fontsize offset"""
        return int(self.lib.fontSize()[1] / 2)


class CoffeeGrinder:
    """Main Program"""
    SINGLE_SEC = "single_sec"
    DOUBLE_SEC = "double_sec"
    CPS = "cps"
    STATE = "state"

    def __init__(self):
        self.__setPins()
        self.encoder = RotaryEncoder()
        self.display = DisplayFunctions()
        self.states = States(machine, self.display, self.pin_menu, self.encoder)
        self.states.startCheckStatesThread()
        # self.__getShotTimes()

    def __getShotTimes(self):
        """Get shot times from memory"""
        single_sec = machine.nvs_getint(self.SINGLE_SEC)
        double_sec = machine.nvs_getint(self.DOUBLE_SEC)
        cps = machine.nvs_getint(self.CPS)
        state = machine.nvs_getint(self.STATE)
        if state:
            self.states.state = state
        if single_sec:
            self.states.single.VALUE = single_sec
        if double_sec:
            self.states.double.VALUE = double_sec
        if cps:
            self.states.cps = cps / 100

    def setCoffeGrindTime(self):
        """Update Grind Time"""
        self.display.update = True
        if self.states.state == self.states.single.STATE:
            single_sec = self.states.single.VALUE
            machine.nvs_setint(self.SINGLE_SEC, int(single_sec))
        elif self.states.state == self.states.double.STATE:
            double_sec = self.states.double.VALUE
            machine.nvs_setint(self.DOUBLE_SEC, int(double_sec))
        machine.nvs_setint(self.STATE, int(self.states.state))

    def __setPins(self):
        """Set uc pins"""
        self.pin_start = machine.Pin(
            33,
            mode=machine.Pin.IN,
            pull=machine.Pin.PULL_DOWN,
            handler=self.startGrinding,
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

    def setCPS(self, pin):
        """Interrupt CPS"""
        self.pin_menu.init(trigger=machine.Pin.IRQ_DISABLE)
        self.states.edit_cps = True

    def setEdit(self, pin):
        """Interrupt Edit"""
        self.pin_menu.init(trigger=machine.Pin.IRQ_DISABLE)
        time.sleep(0.1)
        self.display.update = True
        if self.states.state == self.states.endless.STATE:
            self.edit_state = False
        if self.states.edit_state:
            self.states.edit_state = False
            self.encoder.setState(self.states.state_old)
        else:
            self.states.edit_state = True
            if self.states.state == self.states.single.STATE:
                self.encoder.setTime(self.states.single.VALUE)
            elif self.states.state == self.states.double.STATE:
                self.encoder.setTime(self.states.double.VALUE)
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)

    def showCoffeData(self):
        """Show Display Data"""
        color = 0xFFFFFF
        if self.states.edit_state:
            color = 0xFF0000
        seconds = 0.1
        if self.states.state == self.states.single.STATE:
            seconds = self.states.single.SECONDS
        elif self.states.state == self.states.double.STATE:
            seconds = self.states.double.SECONDS
        text = "Timer: {:.2f} \r".format(round(seconds, 3))
        # if seconds < 10:
        #     text = "Timer:   {} \r".format(round(seconds, 3))
        qty = round(seconds * self.states.cps, 1)
        text_g = "QTY: {:.2f} g\r".format(qty)
        # if qty < 10:
        #     text_g = "QTY:   {} g\r".format(qty)
        self.display.lib.textClear(67, 200, text, color)
        if self.states.state != self.states.endless.STATE:
            self.display.textWrapper(67, 200, text, color)
            self.display.textWrapper(67, 225, text_g, color)

    def startGrinding(self, pin):
        """Interrupt routine for grinder start"""
        if self.states.edit_state:
            return
        self.pin_start.init(trigger=machine.Pin.IRQ_DISABLE)
        self.pin_menu.init(trigger=machine.Pin.IRQ_DISABLE)
        time.sleep(0.1)
        if not self.pin_start.value():
            self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)
            self.pin_start.init(trigger=machine.Pin.IRQ_HILEVEL)
            return
        self.pin_out.value(True)
        if self.states.state == self.states.single.STATE:
            self.__sleepTime(self.states.single.SECONDS)
        elif self.states.state == self.states.double.STATE:
            self.__sleepTime(self.states.double.SECONDS)
        else:
            self.display.textWrapper(67, 200, "Grind!")
            count = 0.2
            time.sleep(0.2)
            while self.pin_start.value():
                qty = round(count * self.states.cps, 3)
                text_g = "QTY: {:.2f} g".format(qty)
                # if qty < 10:
                #     text_g = "QTY:   {} g\r".format(qty)
                self.display.textWrapper(67, 225, text_g)
                count += 0.01
                time.sleep(0.01)
            self.display.textWrapper(67, 200, "\r             ")
        self.pin_out.value(False)
        self.display.update = True
        time.sleep(1)
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING)
        self.pin_start.init(trigger=machine.Pin.IRQ_HILEVEL)

    def __sleepTime(self, sleep):
        """sleep counter"""
        # start_time = time.time()
        end_time = 0
        while end_time < sleep:
            text = "Seconds: {:.2f}".format(round(sleep, 3))
            self.display.textWrapper(67, 200, text, 0xec7d15)
            sleep -= 0.01
            time.sleep(0.01)
            # end_time = time.time() - start_time

    def runProgram(self):
        """Run Main Program"""
        self.display.initText()
        if self.states.edit_cps:
            self.states.editCPS()
            machine.nvs_setint(self.CPS, int(self.states.cps * 100))
        self.pin_menu.init(trigger=machine.Pin.IRQ_FALLING, handler=self.setEdit)
        self.states.state = self.states.double.STATE
        self.states.run = True
        self.states.edit_state = False
        while True:
            if (self.states.state == self.states.single.STATE) and self.states.run:
                self.states.runState(self.states.single, self.display.singleCup)
            elif (self.states.state == self.states.double.STATE) and self.states.run:
                self.states.runState(self.states.double, self.display.doubleCup)
            elif (self.states.state == self.states.endless.STATE) and self.states.run:
                self.states.runState(self.states.endless, self.display.endLess)
            if self.states.edit_state:
                self.setCoffeGrindTime()
            if self.display.update:
                self.showCoffeData()
                self.display.update = False
            time.sleep(0.1)
            print(self.states.state)
            print(self.encoder.value)
            print(self.states.single.SECONDS)
            print(self.states.double.SECONDS)
            print(self.states.single.VALUE)
            print(self.states.double.VALUE)
            print(self.states.edit_state)


if __name__ == '__main__':
    s = CoffeeGrinder()
    s.runProgram()
