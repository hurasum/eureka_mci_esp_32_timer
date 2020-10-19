"""
Neo Pixel typing class

This class includes full support for various types of Neopixel, individually-addressable RGB(W) LEDs.
ESP32 RMT peripheral is used for very precise timing ( +/- 50 ns ).
Up to 8 Neopixel strips can be used, 1~1024 pixels each.
Connecting the Neopixel strip
ESP32 pin 	Neopixel 	Notes
Any output pin 	DIN 	Neopixel data input pin
GND 	GND 	Neopixel ground
4 - 7V 	5VDC 	Neopixel Power

Make shure the Neopixel Power can supply enough power to drive all connected LEDs.
Do not use ESP32 3.3V
"""

class NeoPixel:
    def set(self, pos, color , white, num, update ):
        """
        Set the color of the pixe at position pos
        Argument 	Description
        pos 	required, pixel position; 1 ~ pix_num
        color 	required, pixel color; use numeric value or predifined color constant
        white 	optional; default: 0; white level; only for RGBW Neopixels
        num 	optional; default: 1; number of pixels to set to the same color, starting from pos
        update 	optional, default: True; update the Neopixel strip. If False np.show() has to be used to update the strip
        """
        pass

    def get(self, pos):
        """
        Get the color of the pixe at position pos For 24-bit RGB Neopixels returns the integer representing the RGB color value. For 32-bit RGBW Neopixels returns the tuple of 24-bit RGB color value and 8-bit while level.
        """
        pass

    def setHSB(self, pos, hue, saturation, brightness, white, num, update):
        """
        Set the color of the pixe at position pos using hue/saturation/brightness color model
        Argument 	Description
        pos 	required, pixel position; 1 ~ pix_num
        hue 	float: any number, the floor of this number is subtracted from it to create a fraction between 0 and 1. This fractional number is then multiplied by 360 to produce the hue angle in the HSB color model.
        saturation 	float; 0 ~ 1.0
        brightness 	float; 0 ~ 1.0
        num 	optional; default: 1; number of pixels to set to the same color, starting from pos
        update 	optional, default: True; update the Neopixel strip. If False np.show() has to be used to update the strip
        """
        pass

    def brightness(self, brightness, update):
        """
        Set or get the brightnes factor. Brightnes factor is used to reduce the color level for all the pixels in the strip. Alloved value is 1 to 255.

        If no argument is given, the current brightnes factor will be returned. If update=True (default), the Neopixel strip will be updated immediately.
        """
        pass

    def color_order(self, color_order):
        """
        The pixel color is represented as 24-bit RGB value where RED is most significant byte and BLUE the least significant value. Various Neopixels types requires the color bytes to be sent in specific order (for example WS2812 requires "GRB" color order).

        The color order can be set to any combination of 'R', 'G', 'B' and 'W' (for RGBW type Neopixels). Without arguments, returns the current color order.
        """
        pass

    def timings(self, timings):
        """
        Various Neopixels types may require different timings for encoding the 1 and 0 bits in comunication protocol. When Neopixel object is created, the default timings for WS2812 are used for RGB type and SK6812 timings for RGBW type.

        The timings argument must be tuple with the following structure: (T1H,T1L), (T0H, T0L), Treset). All times are given as ns (nano second) values.

        Without arguments, returns the current timings tuple.
        """
        pass

    def HSBtoRGB(self, hue, saturation, brightness):
        """
        Converts the components of a color, as specified by the HSB model, to an equivalent set of values for the default RGB model. Returns 24-bit integer value suitable to be used as color argiment

        Arguments
        Argument 	Description
        hue 	float: any number, the floor of this number is subtracted from it to create a fraction between 0 and 1. This fractional number is then multiplied by 360 to produce the hue angle in the HSB color model.
        saturation 	float; 0 ~ 1.0
        brightness 	float; 0 ~ 1.0
        """
        pass

    def HSBtoRGBint(self, hue, saturation, brightness):
        """
        Converts the components of a color, as specified by the HSB model, to an equivalent set of values for the default RGB model. Returns 24-bit integer value suitable to be used as color argiment

        Arguments
        Argument 	Description
        hue 	integer: 0 ~ 360
        saturation 	integer; 0 ~ 1000
        brightness 	integer; 0 ~ 1000
        """
        pass

    def RGBtoHSB(self, color):
        """
        Converts 24-bit integer value to the the components of a color, as specified by the HSB model. Returns tuple: (hue, saturation, brightness)
        """
        pass

    def show(self):
        """
        Update the Neopixel strip.
        """
        pass

    def clear(self):
        """
        clear the Neopixel strip.
        """
        pass

