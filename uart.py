"""
UART typing class



    An Universal Asynchronous Receiver/Transmitter (UART) is a component known to handle the timing requirements for a variety of widely-adapted protocols (RS232, RS485, RS422, …).
    An UART provides a widely adopted and cheap method to realize full-duplex data exchange among different devices.
    There are three UART controllers available on the ESP32 chip. They are compatible with UART-enabled devices from various manufacturers. All UART controllers integrated in the ESP32 feature an identical set of registers for ease of programming and flexibility. In this documentation, these controllers are referred to as UART0, UART1, and UART2.

UART0 is used for serial REPL and, at the moment, is not available in this class.

Note: When passing the buffer object to any method, if the argumnt contains characters > \x7f, the argument must be entered as bytearray (e.g., b'Has chars > 0x7F\xff\xfe\xa5')

"""

class UART:
    def init(self, **args):
        """
        All arguments are optional and must be entered as kw arguments (arg=value)
        Argument 	Description
        baudrate 	The baudrate to be used for this uart; default: 115200
        The actual baud rate may be slightly different than the set one due to ESP32 clock divider limitations.
        The actual baudrate is shown when printing the uart status.
        bits 	Number of bits transfered, 5 - 8; default: 8
        parity 	Parity generation:
        None no parity, 0 Odd, 1 Even; default: no parity
        stop 	Number of stop bits:
        1 one stop bit, 2 two stop bits, 3 1.5 stop bits; default: 1
        tx 	TX pin; no defaults
        rx 	RX pin; no defaults
        cts 	CTS pin; default: not used
        rts 	RTS pin; default: not used
        timeout 	Timeout for uart read operations in milliseconds; default: 0
        buffer_size 	Size of the receive buffer in bytes. Range: 512 - 8192; default 512
        Used only when creating the UART instance, ignored in init()
        lineend 	line end string for readln() method, 2 character max; default: '\r\n'
        Usually set to '\r\n', '\n\r', '\r' or '\n', but other values can be used for special purposes.
        If the lineend contains characters > \x7f, the argument must be entered as bytearray (e.g., b'\xff\xfe')
        inverted 	Set the inverted pins
        Tx, Rx, CTS and RTC can be inverted
        use constants INV_RX, INV_TX, INV_CTS, INV_RTS
        Several constants can be combined with or operator.
        """
        pass

    def write(self, buf, len, off):
        """
        Write bytes from buffer object ḃuf to UART
        If no other arguments are given, writes buffer length bytes.
        If len argument is given, writes ŀen bytes.
        If off argument is given, starts writting from off position in buf.
        """
        pass

    def write_break(self, buf, break_num, len):
        """
        Write bytes from buffer object ḃuf to UART.
        After the data are writthe emit the break signal for the duration of break_num bits
        If len argument is given, writes only ŀen bytes from buffer.
        """
        pass

    def any(self):
        """
        Returns number of bytes available in the receive buffer.
        """
        pass

    def read(self, len):
        """
        If no argument is given, reads all available bytes from the receive buffer.
        If len argument is given, reads len bytes from the receive buffer.
        If not enough bytes are available in the input buffer and uart timeout is set to a value greater than 0, waits until len bytes are received or timeout ms expires.
        Returns bytearray of the read bytes.
        """
        pass

    def readinto(self, buf, len):
        """
        If reads buffer buf length bytes from the receive buffer into buf.
        If len argument is given, reads maximum of len bytes from the receive buffer.
        If not enough bytes are available in the input buffer and uart timeout is set to a value greater than 0, waits until buffer length or len bytes are received or timeout ms expires.
        Returns bytearray of the read bytes.
        """
        pass

    def readline(self, max_len):
        """
        Reads all bytes from the receive buffer up to the line end character \n.
        If the line end character is not found in the input buffer and uart timeout is set to a value greater than 0, waits until line end character is received or timeout ms expires.
        If the timeout expires before \n is received, returns all available bytes from the receive buffer
        If the line end character is not found in the input buffer and uart timeout is 0, returns all available bytes from the receive buffer
        Returns bytearray of the read bytes.
        Line end character \n is incleded in the returned bytearray.
        """
        pass

    def readln(self, timeout):
        """
        Similar to uart.readline() but waits for lineend string defined on creating the uart instance or set in uart.init()
        If the timeout argument is not given, the global uart's timeout walue is used.
        If the timeout argument is given, waits for timeout ms.
        Returns a string of received characters.
        Line end characters are included in the returned string.
        If the lineend string is not found, returns None.
        This method is faster than uart.readline().
        """
        pass

    def flush(self):
        """
        Flush (empty) the uart's receive buffer.
        """
        pass

