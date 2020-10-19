"""
PWM typing class
This class includes PWM support using ESP32 LEDC peripheral


Features

    up to 8 pwm channels can be used
    4 pwm timers are available, multiple channels can use the same timer
    all pwm channels using the same timer have the same frequency, but can have different duty cycles
    maximum pwm frequency is 40 MHz
    pwm duty resolution can be 1-15 bits and is automatically set to maximum value for requested frequency.
    The frequency and the duty resolution are interdependent. The higher the PWM frequency, the lower duty resolution is available and vice versa.

"""

class PWM:
    def init(self, freq, duty, timer):
        """
        Reinitialize the pwm channel
        Arg 	Description
        freq 	optional, if not given, the frequency is not changed
        duty 	optional, if not given, the duty cycle is not changed
        timer 	optional, if not given, the pwm timer is not changed

        Changing the frequency or timer will affect all pwm channels using the same timer.

        """
        pass

    def deinit(self):
        """
        Deinitialize and free the pwm channel, stop pwm output.

        The echannel can be reinitializeded using pwm.init().

        """
        pass

    def freq(self, freq):
        """
        With no argument, return the current pwm channel frequency.
        Set the new pwm frequency to ḟreq Hz.
        All pwm channels using the same timer will be affected.

        """
        pass

    def duty(self, duty_perc):
        """
        With no argument, return the current pwm channel duty cycle.
        Set the new pwm duty cycle to duty_perc in %. The value can be given as float.

        """
        pass

    def pause(self):
        """
        Pause the pwm channel timer, no pwm output will be present on pwm pin.
        All pwm channels using the same timer will be affected.

        """
        pass
