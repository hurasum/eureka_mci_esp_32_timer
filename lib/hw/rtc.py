"""
RTC typing class

his class includes support for using ESP32 RTC peripherals and memory

The content of the RTC memory is preserved during the deep sleep.

Up to 64 32-bit integers can be saved in RTC memory.

One string of up to 2048 characters can be saved in RTC memory.
The string can be, for example, json string containing the parameters which has to be restored after deep sleep wake-up.

Integers and string saved in RTC memory are protected by 16-bit CRC.
"""

class RTC:
    def init(self, date):
        """
        Set the system time and date.

        date argument is the tuple containing the time and date information:
        (year, month, day [,hour [,minute [, second ]]])
        """
        pass

    def now(self):
        """
        Return the current time as tuple:
        (year, month, day, hour, minute, second)
        """
        pass

    def ntp_sync(self, server, update_period, tz):
        """
        server the NTP server domain name or IP, for example "pool.ntp.org"
        update_period optional, time update interval in seconds; default: 0
        tz optional, time zone string; default: the one set in menuconfig
        Note: for update_period < 300, the time will be synced only once

        rtc = machine.RTC()
        """
        pass

    def ntp_sync(self, server="hr.pool.ntp.org", tz="CET-1CEST"):
        """
        server the NTP server domain name or IP, for example "pool.ntp.org"
        update_period optional, time update interval in seconds; default: 0
        tz optional, time zone string; default: the one set in menuconfig
        Note: for update_period < 300, the time will be synced only once

        rtc = machine.RTC()
        rtc.ntp_sync(server="hr.pool.ntp.org", tz="CET-1CEST")
        rtc.synced()
        True
        utime.gmtime()
        (2018, 1, 29, 16, 3, 18, 2, 29)
        utime.localtime()
        (2018, 1, 29, 17, 3, 30, 2, 29)
        """
        pass

    def synced(self):
        """    True
        utime.gmtime()
        (2018, 1, 29, 16, 3, 18, 2, 29)
        utime.localtime()
        (2018, 1, 29, 17, 3, 30, 2, 29)

        """
        pass

    def synced(self):
        """
        Return True if the system time was synced from NTP server, False if not.
        """
        pass

    def wake_on_ext0(self, pin, level):
        """
        Enable external interrupt #0 on gpio level.

        pin a Pin object to be used for wake up level is the pin state on which the interrupt will be activated 0 | 1
        Valid pins are: 0, 2, 4, 12-15, 25-27, 32-39

        To disable external interrupt #0, execute rtc.wake_on_ext0(None)
        """
        pass

    def wake_on_ext1(self, pins, level):
        """
        Enable external interrupt #1 on multiple pins.

        pins tuple of Pin objects to be used as wakeup source: (Pin(x), Pin(y), ..., Pin(z))
        level is the pin state on which the interrupt wil be activated 0 | 1
        Valid pins are: 0, 2, 4, 12-15, 25-27, 32-39

        If level is set to 0, all pins must be at low level to wake up.
        If level is set to 1, any pin at high level will wake up.

        To disable external interrupt #1, execute rtc.wake_on_ext1(None)
        """
        pass

    def write(self, pos, value):
        """
        Write integer (32-bit) value to the position pos in RTC memory.
        Return True on success, False if failed.
        """
        pass

    def read(self, pos):
        """
        Read integer (32-bit) from the position pos in RTC memory.
        Returns None if no value has not been written to the RTC integer memory yet or the RTC memory was corrupted (bad CRC), otherwise returns the integer written to the position or 0 (default value).
        """
        pass

    def write_string(self, text):
        """
        Write the string text to RTC memory.
        Return True on success, False if failed.
        """
        pass

