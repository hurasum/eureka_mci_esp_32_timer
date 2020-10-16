"""
PIN typing class

This class includes support for using ESP32 gpios

The ESP32 chip features 40 physical GPIO pads.
Some GPIO pads cannot be used or do not have the corresponding pin on the chip package(refer to technical reference manual).
Each pad can be used as a general purpose I/O or can be connected to an internal peripheral signal.
Note that GPIO6-11 are usually used for SPI flash.
GPIO34-39 can only be set as input mode and do not have software pullup or pulldown functions.


"""

class PIN:
    def init(self, mode, pull, value, handler, trigger, debounce=0, acttime=0):
        """
        Change the pin configuration and options after the pin instance object was created.

        For arguments description see Create the Pin instance object

        """
        pass

    def value(self, val):
        """
        Get or set the pin value.
        If no argument is given, returns the current pin value (level), 0 or 1
        It the val argument is given, set the pin level. val can be 0, 1, False or True

        Note: If the pin is set to output-only mode (OUT or OUT_OD), the returned value will always be 0
        If you want to get the value of the output pin, it must be se to INOUT or INOUT_OD mode.

        """
        pass

    def irqvalue(self):
        """Returns the pin level at the time when the last interrupt occured.
        Can be used inside the interrupt handling function."""
        pass
