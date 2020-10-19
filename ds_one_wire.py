"""
DS One wire typing class

This class includes support for DS18xxx family of temperature sensors.

Supported devices: DS18B20, DS18S20, DS1822 and DS28EA00
"""

class DS18x20:
    def deinit(self):
        """
        Deinitialize the ds18x20 object, free the resources.

        Note: Onewire object can be deinitialized only if all ds18x20 object using it are deinitialized.

        """
        pass

    def read_temp(self):
        """
        Return the last measured temperature from DS18xxx device.
        The measurement cycle is not started.
        The temperature is returned as the float value in °C

        """
        pass

    def read_tempint(self):
        """
        Return the last measured value from DS18xxx device.
        The measurement cycle is not started.
        The temperature is returned as the raw integer value.

        """
        pass

    def convert_read(self):
        """
        Return the temperature from DS18xxx device.
        Start the measurement, wait until done.
        The temperature is returned as the float value in °C

        # >>> ds1.convert_read()
        24.75
        # >>>


        """
        pass

    def convert_readint(self):
        """
        Return the temperature value from DS18xxx device.
        Start the measurement, wait until done.
        The temperature is returned as the raw integer value.

        # >>> ds1.convert_readint()
        396


        """
        pass

    def convert(self, wait):
        """
        Start the temperature measurement on all attached devices.

        If the optional argument wait is True, the function will wait until the measurement is done.
        If wait argument is False (default), the function will exit immediately.
        The measurement progress can be checked using ds-conv_time() method.

        """
        pass

    def conv_time(self):
        """
        Returns the elapsed time since last ds.convert(False).
        If the returned value is negative, the conversion is still in progress.
        If positive, the conversion is finished and the temperature valu can be read.

        def wait_temp():
            ds1.convert(False)
            et = ds1.conv_time()
            while et < 50:
                print("waiting", et)
                time.sleep_ms(50)
                et = ds1.conv_time()
            print("finished, temp =",ds1.read_temp())

        # >>> wait_temp()
        waiting -189
        waiting -139
        waiting -89
        waiting -39
        waiting 11
        finished, temp = 24.75
        # >>>


        """
        pass

    def get_res(self):
        """
        Return the current sensor resolution.
        """
        pass

    def set_res(self, res):
        """
        Set the sensor's resolution res bits.
        Higher resolution will require longer conversion time.

        # >>> ds1.get_res()
        10
        # >>> ds1.set_res(12)
        True
        # >>> wait_temp()
        waiting -752
        waiting -702
        waiting -652
        waiting -602
        waiting -552
        waiting -502
        waiting -452
        waiting -402
        waiting -352
        waiting -302
        waiting -252
        waiting -202
        waiting -152
        waiting -102
        waiting -52
        waiting -2
        waiting 48
        finished, temp = 24.75
        # >>>


        """
        pass

    def rom_code(self):
        """
        Return the device's ROM code as hex string.

        # >>> ds1.rom_code()
        '6e000000c86a8e28'


        """
        pass

