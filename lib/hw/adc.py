"""
ADC typing class



ESP32 integrates two 12-bit SAR (Successive Approximation Register) ADCs (Analog to Digital Converters) and supports measurements on 18 channels (analog enabled pins).
The ADC driver API supports:

ADC1 (8 channels, attached to GPIOs 32 - 39)
ADC2 (10 channels, attached to GPIOs 0, 2, 4, 12 - 15 and 25 - 27).

However, there’re some restrictions for the application to use ADC2:

The application can use ADC2 only when Wi-Fi driver is not started, since the ADC is also used by the Wi-Fi driver, which has higher priority.
Some of the ADC2 pins are used as strapping pins (GPIO 0, 2, 15), so they cannot be used freely.
For examples, for official Develop Kits:
ESP32 Core Board V2 / ESP32 DevKitC: GPIO 0 cannot be used due to external auto program circuits.
ESP-WROVER-KIT V3: GPIO 0, 2, 4 and 15 cannot be used due to external connections for different purposes.


This class includes full support for using ESP32 ADC peripheral.
Functions are added to set the attenuation and to calibrate the ADC.

ESP32 ADC input voltage range depends on attenuation setting:
Attenuation 	Voltage range
0 dB 	1.1 V
2.5 dB 	1.5 V
6 dB 	2.2 V
11 dB 	3.9 V

Due to ADC characteristics, most accurate results are obtained within the following approximate voltage ranges:

0 dB attenuaton (ATTN_0DB) between 100 and 950mV
2.5 dB attenuation (ATTN_2_5DB) between 100 and 1250mV
6 dB attenuation (ATTN_6DB) between 150 to 1750mV
11 dB attenuation (ATTN_11DB) between 150 to 2450mV


Note: Using ADC2 works, but as support for ADC2 in esp-idf is not fully functional, some error logs may br printed while using ADC2.
"""

class ADC:
    def deinit(self):
        """
        Deinitialize the adc, free the pin used.

        """
        pass

    def atten(self, value):
        """
        Set the attenuation value.

        The following attenuation constants can be used for value:
        ATTN_0DB - attenuation 0 dB (range: 0 - 1.1 V)
        ATTN_2_5DB - attenuation 2.5 dB (range 0 - 1.5 V)
        ATTN_6DB - attenuation 6 dB (range: 0 - 2.5 V)
        ATTN_11DB - attenuation 11 dB (range: 0 - 3.9 V'

        # >>> adc.atten(adc.ATTN_11DB)
        # >>> adc
        ADC(Pin(34): unit=ADC1, chan=6, width=12 bits, atten=11dB (3.9V), Vref=1100 mV)
        # >>>


        """
        pass

    def vref(self, vref, vref_topin):
        """Get or set ADC refference voltage and/or reference output pin.

            The gain and offset factors of an ESP32 module's ADC are calculated using the reference voltage and the Gain and Offset curves provided in the lookup tables.
            Nominal voltage refernce is 1100 mV, and can be adjusted to compensate for ESP32 chip differences.
            The reference voltage can be set to any value in range 1000 ~ 1200 mV.
            The internal ESP32 reference can be routed to gpio to be measured and the value used to set the reference voltage for the specific ESP32 chip.

        To route the reference voltage to the gpio set the argument vref_topin to the gpio pin number to be used as output.
        Valid gpios are only 25, 26 and 27.

        Returns tuple containing the current refference voltage in mV and selected output pin.

        # Get the reference voltage
        # >>> machine.ADC.vref()
        (1100, 0)
        # Route the internal reference voltage to GPIO#25
        # >>> machine.ADC.vref(vref_topin=25)
        # You can now measure the voltage on GPIO#25 with the voltmeter

        # Set the reference voltage to measured value in mV
        # This value will be used to get more precise readings
        # >>> machine.ADC.vref(vref=1096)
        (1096, 0)
        """
        pass

    def width(self, value):
        """
        Configure ADC capture width..

        The following constants can be used for value:
        WIDTH_9BIT - capture width is 9Bit
        WIDTH_10BIT - capture width is 10Bit
        WIDTH_11BIT - capture width is 11Bit
        WIDTH_12BIT - capture width is 12Bit

        # >>> adc.width(adc.WIDTH_10BIT)
        # >>> adc
        ADC(Pin(34): unit=ADC1, chan=6, width=10 bits, atten=11dB (3.9V), Vref=1100 mV)
        # >>>


        machine.ADC.vref([vref=mv] [,] [vref_topin=pin])

        Get or set ADC refference voltage and/or reference output pin.

            The gain and offset factors of an ESP32 module's ADC are calculated using the reference voltage and the Gain and Offset curves provided in the lookup tables.
            Nominal voltage refernce is 1100 mV, and can be adjusted to compensate for ESP32 chip differences.
            The reference voltage can be set to any value in range 1000 ~ 1200 mV.
            The internal ESP32 reference can be routed to gpio to be measured and the value used to set the reference voltage for the specific ESP32 chip.

        To route the reference voltage to the gpio set the argument vref_topin to the gpio pin number to be used as output.
        Valid gpios are only 25, 26 and 27.

        Returns tuple containing the current refference voltage in mV and selected output pin.

        # Get the reference voltage
        # >>> machine.ADC.vref()
        (1100, 0)
        # Route the internal reference voltage to GPIO#25
        # >>> machine.ADC.vref(vref_topin=25)
        # You can now measure the voltage on GPIO#25 with the voltmeter

        # Set the reference voltage to measured value in mV
        # This value will be used to get more precise readings
        # >>> machine.ADC.vref(vref=1096)
        (1096, 0)


        """
        pass

    def read(self):
        """
        Read the ADC value as voltage (in mV)

        Calibrated read is used.
        For hall sensor readings, the raw value is returned.

        Data collection

        """
        pass

    def collect(self, freq, len=0, readmv=False, data=None, callback=None, wait=False):
        """
        Collect ADC data in background using the ESP32 timer interrupt.
        Arg 	Description
        freq 	the frequency at which the data is collected
        valid range: 0.001 - 18000 Hz
        readmv 	optional, default False; collect raw ADC value (False) or calibrated values in mV (True)
        len 	optional, default: 0; number of samples to collect
        If not collecting to an array, must be > 0
        If collecting to an array, can be omited, if set, only the len samples will be collected
        data 	optional, default: None; Collect data into a given array object
        If the array is of type 'H' or 'h', 16-bit values will be collected (the resolution depends on ADC width)
        If the array is of type 'B', 8-bit values will be collected (the ADC value will be converted to 8-bit value)
        callback 	optional, default: None; callback function to be executed after the collection is finished
        Function prototype: adc_cb_func(adc_obj)
        wait 	optional, default: False; wait until the collection is finished

        During the data collection some statistical data are collected: minimum, maximum, average and rms.
        If the data array is not given, only the statictical data are available after the collection.

        """
        pass

    def read_timed(self, data, freq, nsamples=-1, byte=True, wait=False, callback=None):
        """
        Read the ADC data in background using the ESP32 I2S peripheral.
        Mostly used to capture the audio data to an array of file.
        The ADC is configured to 12 bit and 11 dB attenuation by I2S, you may need an amplifier to get the required input range.
        Arg 	Description
        data 	array object or filename>br>If an array object is given, read data into array object
        If the array is of type 'H' or 'h', 16-bit values will be saved (the resolution depends on ADC width)
        If the array is of type 'B', 8-bit values will be saved (the ADC value will be converted to 8-bit value)
        If the filename is given, the ADC data will be saved to file
        freq 	the frequency at which the data is collected
        valid range: 5000 - 500000 Hz
        nsamples 	number of ADC samples to collect
        mandatory if saving to file
        optional if saving to an array, if set, only the nsamples samples will be saved
        byte 	optional, default: True; only used if saving to file.
        If True, save ADC values as 8-bit values, if False save as 16-bit values
        wait 	optional, default: False; wait until the collection is finished
        callback 	optional, default: None; callback function to be executed after the collection is finished
        Function prototype: adc_cb_func(adc_obj)

        Warning: Saving data to file on internal file system can be too slow and not all the data will be saved.
        Saving data to the file on SD Card usually works without issues.

        """
        pass

    def stopcollect(self):
        """
        Stop previously started collect or read_timed operation running in background.

        """
        pass

    def progress(self):
        """
        Get the status of the previously started collect or read_timed operation.
        Returns the 4-item tuple:
        (active, collected_len, total_len, elapsed_time)
        active True if operation is not yet finished, False if finished
        collected_len number of collected values, less than total_len if not yet finished
        total_len total number of values that will be collected
        elapsed_time elapsed collection time in micro seconds

        """
        pass

