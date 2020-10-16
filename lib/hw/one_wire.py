"""
One Wire typing class

This class includes full support for Onewire devices using the ESP32 RMT peripheral to achieve very precise timing

1-Wire is a device communications bus system designed by Dallas Semiconductor Corp. that provides low-speed data, signaling, and power over a single conductor.
1-Wire is similar in concept to I²C, but with lower data rates and longer range. It is typically used to communicate with small inexpensive devices such as digital thermometers and weather instruments. A network of 1-Wire devices with an associated master device is called a MicroLAN.
One distinctive feature of the bus is the possibility of using only two wires: data and ground. To accomplish this, 1-Wire devices include an 800 pF capacitor to store charge, and to power the device during periods when the data line is active.

Connecting 1-wire device.
ESP32 	Device
any ouput capable port
External pull-up resistor (1K - 4.7K)
to +3.3V is needed 	D (data pin)
GND 	GND
+3.3V 	Vdd (optional)

The 1-wire devices can be connected in two power modes:

Normal power, +3.3V is connected to the device's Vdd pin
Normal Power
Parasite power, device's Vdd pin is connected to the GND pin, the needed power is supplied by the data pin
Parasite power
The used Power mode is detected automatically by the driver
All devices connected to the same 1-wire bus must operate in the same mode
"""

class OneWire:
    def deinit(self):
        """
        Deinitialize the 1-wire bus and free the used resources.

        """
        pass

    def scan(self, asnum):
        """
        Scan 1-wire bus for attached devices.

        Returns the tuple of detected devices ROM codes.

        Optional asnum argument defines the format of the rom code returned.
        If False (default), the rom code is returned as hex string.
        If True, the rom code is returned as tuple: (family_code, serial_number, crc)

        # >>> ow.scan()
        ('6e000000c86a8e28', '02000000c82a8928')
        # >>> ow.scan(True)
        ((40, 13134478, 110), (40, 13118089, 2))

        """
        pass

    def search(self, asnum):
        """
        Same as ow.scan.

        """
        pass

    def rom_code(self, dev):
        """
        Return the ROM code of the device dev as hex string.

        # >>> ow.rom_code(0)
        '6e000000c86a8e28'


        """
        pass

    def crc8(self, buf):
        """
        Returns the crc8 checksum byte for the buf argument

        # >>> ow.crc8('123456abcdef')
        12
        # >>> buf = bytearray([0x11,0x12,0x13,0x67,0xf7])
        # >>> ow.crc8(buf)
        227


            The following low-level methods can be used
            to implement Python drivers for various 1-wire devices.

        """
        pass

    def reset(self):
        """
        Reset the 1-wire bus.
        """
        pass

    def readbyte(self):
        """
        Read one byte from the 1-wire device.
        """
        pass

    def writebyte(self, val):
        """
        write one byte val to the 1-wire device.
        """
        pass

    def readbytes(self, len):
        """
        Read len bytes from the 1-wire device.
        Returns string of read bytes.
        """
        pass

