"""
SPI typing class

This class includes full support for using ESP32 SPI peripheral in master mode

Only SPI master mode is supported for now.

Python exception wil be raised if the requested spihost is used by SD Card driver (sdcard in spi mode).
If the requested spihost is VSPI and the psRAM is used at 80 MHz, the exception will be raised.
The exception will be raised if SPI cannot be configured for given configurations.

"""

class SPI:
    def deinit(self):
        """
        Deinitialize the SPI object, free all used resources.

        """
        pass

    def read(self, len, val):
        """
        Read len bytes from SPI device.
        Returns the string of read bytes.
        If the optional val argument is given, outputs val byte on mosi during read (if duplex mode is used).

        """
        pass

    def readinto(self, buf, val):
        """
        Read bytes from SPI device into buffer object buf. Length of buf bytes are read.
        If the optional val argument is given, outputs val byte on mosi during read (if duplex mode is used).

        """
        pass

    def readfrom_mem(self, address, length, addrlen):
        """
        Writes address to the spi device and reads length bytes.
        The number of the address bytes to write is determined from the address value (1 byte for 0-255, 2 bytes for 256-65535, ...).
        The number of address bytes to be written can also be set by the optional argument addrlen (1-4).
        Returns the string of read bytes.

        """
        pass

    def write(self, buf):
        """
        Write bytes from buffer object buf to the SPI device.
        Returns True on success, False ion error

        """
        pass

    def write_readinto(self, wr_buf, rd_buf):
        """
        Write bytes from buffer object wr_buf to the SPI device and reads from SPI device into buffer object rd_buf.
        The lenghts of wr_buf and rd_buf can be different.
        In fullduplex mode write and read are simultaneous. In halfduplex mode the data are first written to the device, then read from it.
        Returns True on success, False ion error

        """
        pass

    def select(self):
        """
        Activates the CS pin if it was configured when the spi object was created.

        """
        pass
