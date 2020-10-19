"""
DAC typing class

ESP32 has two 8-bit DAC (digital to analog converter) channels, connected to GPIO25 (Channel 1) and GPIO26 (Channel 2).
The DAC driver allows these channels to be set to arbitrary voltages.<br The DAC channels can also be driven with DMA-style written sample data, via the I2S driver when using the “built-in DAC mode”.


This class includes full support for using ESP32 DAC peripheral.

ESP32 DAC output voltage range is 0-Vdd (3.3 V), the resolution is 8-bits
"""

class DAC:
    def deinit(self):
        """
        Deinitialize the dac object, free the pin used.

        """
        pass

    def write(self, value):
        """
        Set the DAC value. Valid range is: 0 - 255
        The value of 255 sets the voltage on dac pin to 3.3 V

        """
        pass

    def waveform(self, freq, type ,duration=0 ,scale=0 ,offset=0 ,invert=2):
        """
        Generate the waveform on the dac output
        Arg 	Description
        freq 	the waveform frequency; valid range:
        16-32000 Hz for sine wave
        500-32000 Hz for noise
        170 - 3600 Hz for triangle
        170 - 7200 Hz for ramp and sawtooth
        type 	the waveform type, use one of the defined constants:
        SINE, TRIANGLE, RAMP, SAWTOOTH and NOISE
        duration 	optional, is given, waits for duration ms and stops the waveform
        scale 	optional, only valid for sine wave; range: 0-3; scale the output voltage by 2^scale
        offset 	optional, only valid for sine wave; range: 0-255; ofset the output voltage by offset value
        invert 	optional, only valid for sine wave; range: 0-3; invert the half-cycle of the sine wave

        """
        pass

    def beep(self, freq, duration ,scale=0):
        """
        Generate the sine wave beep on the dac output
        Arg 	Description
        freq 	fequency; valid range:
        16-32000 Hz
        duration 	the duration of the beep in ms
        scale 	optional; range: 0-3; scale the output voltage by 2^scale

        """
        pass

    def write_timed(self, data, samplerate ,mode ,wait=False):
        """
        Output the values on dac pin from array or file using ESP32 I2S peripheral
        The data in array or file must be 8-bit DAC values
        The data from array or file obtained with machine.ADC.read_timed() can be used.
        Arg 	Description
        data 	array object or filename
        If an array object is given, write data from array object
        The array object can be array of type 'B', or bytearray
        If the filename is given, the datafrom the file will be output
        samplerate 	the sample rate at which the data will be output
        valid range: 5000 - 500000 Hz
        mode 	optional, default: machine.DAC.NORMAL; if set to machine.DAC.CIRCULAR the data from array or file will be repeated indefinitely (or until stopped)
        wait 	optional, default: False; if set to True waits for data output to finish

        """
        pass

    def write_buffer(self, data, freq ,mode ,wait=False):
        """
        Output the values on dac pin from an array using timer
        The in the array must be 8-bit DAC values
        The data from an array obtained with machine.ADC.collect() can be used.
        Arg 	Description
        data 	array object of type 'B'
        freq 	float; the frequency at which the data will be output
        valid range: 0.001 - 18000 Hz
        mode 	optional, default: machine.DAC.NORMAL; if set to machine.DAC.CIRCULAR the data from array will be repeated indefinitely (or until stopped).
        Some 'cliks' can be expected when playing continuously if the first value differs from the last one.
        wait 	optional, default: False; if set to True waits for data output to finish

        """
        pass

    def wavplay(self, wavfile, correct):
        """
        Plays the WAV file on dac pin
        Only PCM, 8-bit mono WAV files with sample rate >= 22000 can be played

        If the optional argument correct is given, the sample rate is corrected by correct factor.
        The allowed range is: -8.0 - +8.0 (float values can be entered).

        """
        pass

    def stopwave(self):
        """
        Stops the background proces started by dac.waveform(), dac.write_timed() or dac.wavplay() function.

        """
        pass
