"""
Timer typing class



This class includes support for using ESP32 hardware timer peripheral

This class includes support for using ESP32 hardware timer peripheral

    The ESP32 chip contains two hardware timer groups. Each group has two general-purpose hardware timers. They are all 64-bit generic timers based on 16-bit prescalers and 64-bit auto-reload-capable up / down counters.

Features

    Several timer operational modes are available:

Mode 	Description
ONE_SHOT 	When timer is started, it runs for defined time and stops.
If given, the callback function is executed when the defined time elapses.
PERIODIC 	Timer runs repeatedly until explicitly stopped.
When defined time elapses the callback function is executed, if given
CHRONO 	Used for measuring the elapsed time with µs precision.
Can be started, paused, resumed and stopped
EXTBASE 	Base timer for extended timers. Only timer 0 can be used in this mode.

    Up to 4 hardware timers can be used.
    Up to 8 extended timers can be used if timer 0 is configured in EXTBASE mode.
    That way total of 11 timers can be used.
    Extended timers can operate only in ONE_SHOT or PERIODIC modes.
    In CHRONO mode timers uses 1 MHz clock as timer base frequency to achieve 1 µs resolution.
    In other modes timers uses 2 kHz clock as timer base frequency, resulution of 1 ms is available.
    Each timer keeps track of number of timer events and number of executed callbacks

Warnng:

    Due to MicroPython callback latency, some callbacks may not be executed if the timer period is less than 15 ms.
    The number of events and executed callbacks can be checked using tm.events() method.
"""

class TM:
    def deinit(self):
        """
        Deinitialize the timer, free the hardware timer resources.
        Timer 0, running in EXTBASE mode, canno't be freed if some EXTENDED timers are still running.

        """
        pass

    def value(self):
        """
        Returns the current timer counter value in µs if timer mode is CHRONO or in ms for other modes.
        Most useful for CHRONO mode timers, as it returns the actual elapsed time.

        """
        pass

    def pause(self):
        """
        Pause the timer.
        Timer 0, running in EXTBASE mode, canno't be paused if some EXTENDED timers are running.

        """
        pass

    def stop(self):
        """
        Stop the timer. Alias for tm.pause()
        Only use for timer in CHRONO mode.

        """
        pass

    def resume(self):
        """
        Resume the previously paused timer.


        """
        pass

    def start(self):
        """
        Resume the previously paused/stopped timer.
        Same function as tm.resume(), but resets the timer value to 0.
        Only use for timer in CHRONO mode.

        """
        pass

    def reshot(self):
        """
        Start the ONE_SHOT timer again.
        Only use for timer in ONE_SHOT mode.

        """
        pass

    def timernum(self):
        """
        Returns the hw timer number this timer uses.


        """
        pass

    def events(self):
        """
        Returns the number of timer events and number of executed callbacks.
        The tuple is returned: (num_events, num_cb).
        If no callbacks were missed, num_events = num_cb.

        """
        pass

    def isrunning(self):
        """
        Returns True if the timmer is currently running, False if not.

        """
        pass

    def period(self, period):
        """
        Get or set the timer period.
        Executed without argument, returns the current timer's period.
        Executed with period argument, changes the timer's period to the new value.

        """
        pass
