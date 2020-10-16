"""
Machine typing class

machine module contains various methods and classes related to ESP32 hardware.
"""

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .hw.adc import ADC
    from .hw.dac import DAC
    from .hw.ds_one_wire import DS18x20
    from .hw.neo_pixel import NeoPixel
    from .hw.one_wire import OneWire
    from .hw.pin import PIN
    from .hw.pwm import PWM
    from .hw.rtc import RTC
    from .hw.spi import SPI
    from .hw.timer import TM
    from .hw.uart import UART
    from .hw.i2c import I2C

LOG_NONE = "LOG_NONE"
LOG_ERROR = "LOG_ERROR"
LOG_WARN = "LOG_WARN"
LOG_INFO = "LOG_INFO"
LOG_DEBUG = "LOG_DEBUG"
LOG_VERBOSE = "LOG_VERBOSE"

def UART(uart_num, tx, rx, **args) -> "UART":
    """Creates the UART instance.
    uart_num is mandatory, the ESP32 UART, 1 or 2
    tx, rx pins used for TX & RX
    Other arguments are optional and have the same meaning as in uart.init() method."""
    pass

def Timer(timer_no) -> "TM":
    """timer_no argument is the timer number to be used for the timer.
    It can be 0 - 3 for 4 hardware timers or 4 - 11 for extended timers.
    If extended timer is selected, timer 0 must already be configured in EXTBASE mode. """
    pass

def spi(spihost, baudrate, polarity, phase, firstbit, sck, mosi, miso, cs, duplex, bits) -> "SPI":
    """Argument 	Description
    spihost 	The hardware SPI host
    machine-SPI.HSPI (1) or machine.SPI.VSPI (2) can be used
    Default: 1
    baudrate 	SPI clock speed in Hz; Default: 1000000
    polarity 	SPI polarity; 0 or 1; Default: 0
    phase 	SPI phase; 0 or 1; Default: 0
    polarity & phase defines the SPI operating mode (0-3):
    mode = (polarity<<1) + phase
    firstbit 	Send MSB or LSB bit first; default: MSB
    use constants machine.spi.MSB or machine.spi.LSB
    sck 	SPI SCK pin; Can be entered as integer pin number or machine.Pin object
    moosi 	SPI MISI pin; Can be entered as integer pin number or machine.Pin object
    miso 	SPI MISO pin; Can be entered as integer pin number or machine.Pin object
    cs 	Optional; SPI CS pin; Can be entered as integer pin number or machine.Pin object.
    If set, CS activation and deactivation is handled by the driver, if not set, SPI select and deselect must be handled by user
    duplex 	Select wether SPI operates in fullduplex or halfduplex mode
    In fullduplex mode SPI writes and reads data at the same time
    In halfduplex mode SPI writes data first, then reads data
    Default: True
    bits 	Not used, ignored if given

    Only sck, mosi and miso are required, all the other arguments are optional and will be set to the default values if not given.
    All arguments, except for spihost are KW arguments and must be entered as arg=value."""
    pass

def RTC() -> "RTC":
    """Real time Clock"""
    pass

def PWM(pin, freq, duty, timer) -> "PWM":
    """Arg 	Description
    pin 	esp32 GPIO number to be used as pwm output
    can be given as integer value or machine.Pin object
    freq 	optional, default 5 kHz; pwm frequeny in Hz (1 - 40000000)
    duty 	optional, default 50% kHz; pwm duty cycle in % (0 - 100)
    timer 	optional, default 0; pwm timer (0 - 3)

    PWM channel is selected automatically from 8 available pwm channels. """
    pass

def Pin(gpio, mode, pull, value, handler, trigger, debounce, acttime) -> "PIN":
    """Argument 	Description
    gpio 	gpio number, if invalid gpio number is entered, an exception will be raised
    mode 	optional; pin operating mode
    use one of the constants: IN, OUT, OUT_OD, INOUT, INOUT_OD
    default: IN
    Modes with _OD suffix are configure as open drain outputs.
    Warning: pins 34-39 are input-only pins and cannot be used as output.
    pull 	optional; activate internal pull resistor if pin is configured as input
    use one of the constants: PULL_UP, PULL_DOWN, PULL_UPDOWN, PULL_FLOAT
    default: PULL_FLOAT
    Warning: pins 34~39 do not have pull-up or pull-down circuitry
    value 	optional; set the initial value for an output pin; default: do not set
    handler 	optional; Pin irq callback function
    If set, the pin interrupt will be enabled and the given function will be called on interrupt
    default: no irq enabled
    trigger 	optional; the pin interrupt mode
    use on of the constants: IRQ_DISABLE, IRQ_RISING, IRQ_FALLING, IRQ_ANYEDGE, IRQ_LOLEVEL, IRQ_HILEVEL
    default: IRQ_DISABLE
    Warning: if the level interrupt is selected, the interrupt will be disabled before the interrupt function is executed and must be explicitly enabled in interrupt function if needed
    debounce 	optional; debounce time on pin interrupt in micro seconds, 0 for debounce disable
    valid range: 100 - 500000 µs
    default: 0
    acttime 	optional; the minimal time the pin must be in active state after interrupt for interrupt function to be executed, in micro seconds
    valid range: 100 - 500000 µs, must be <= debounce
    default: 0

    Only gpio argument is required, all the other are optional and will be set to the default values if not given.
    Arguments value, handler, trigger, debounce, acttime must be given as kw arguments (arg=value)"""
    pass

def ds18x20(ow, dev) -> "DS18x20":
    """ow is the Onewire instance
    dev is the device number on 1-wire bus.

    # >>> ds0 = machine.Onewire.ds18x20(ow, 0)
    # >>> ds0
    ds18x20(Pin=25, OW Device=0, Type: DS18B20, Resolution=10bits, ROM code=6e000000c86a8e28, Parasite power: True)
    # >>> ds1 = machine.Onewire.ds18x20(ow, 0)
    # >>> ds1
    ds18x20(Pin=25, OW Device=1, Type: DS18B20, Resolution=10bits, ROM code=02000000c82a8928, Parasite power: True)"""
    pass

def Onewire(pin) -> "OneWire":
    """The new 1-wire bus is created on ESP32 gpio pin.
    The bus is scanned for attached devices.

    # >>> import machine
    # >>>
    # >>> ow = machine.Onewire(25)
    # >>> ow
    Onewire(Pin=25, RMTChannels=7&6, Devices=2, Used=0)"""
    pass

def Neopixel(pin, pixels, type) -> "NeoPixel":
    """pin can be given as pin number or machine.Pin object.
    pixels is the number of the pixels, 1 ~ 1024
    type Neopixel type: 0 (machine.Neopixel.TYPE_RGB) for RGB LEDs, or 1 (machine.Neopixel.TYPE_RGBW) for RGBW LEDs

    import machine
    np = machine.Neopixel(22, 115, 0)
    npw = machine.Neopixel(machine.Pin(25), 24, machine.Neopixel.TYPE_RGBW)

    Colors

    color values are given as 24 bit integer numbers, 8-bit per R,G,B color.
    For example: 0xFF0000 represents the RED color.
    The following color constants are defined and can be used as color arguments:
    BLACK, WHITE, RED, LIME, BLUE, YELLOW, CYAN, MAGENTA, SILVER, GRAY, MAROON, OLIVE, GREEN, PURPLE, TEAL, NAVY

    For RGBW Neopixels, white argument can be given as integer 0 ~ 255."""
    pass

def I2C(id, mode, speed, sda, scl, slave_addr, slave_bufflen, slave_rolen, slave_busy) -> "I2C":
    """Argument 	Description
    id 	The hardware I2C peripheral ID; 0 or 1 can be used
    Default: 0
    mode 	I2C interface mode; master or slave
    Use the constants machine.I2C.MASTER or machine.I2C.SLAVE
    Default: master
    speed
    freq 	I2C clock frequency in Hz
    Default: 100000
    sda 	I2C sda pin; can be given as integer gpio number or Pin object
    scl 	I2C scl pin; can be given as integer gpio number or Pin object
    slave_address 	I2C slave address to be assigned to this i2c interface.
    Only used if SLAVE mode is selected
    7-bit address, do not use reserved adresses 0x00-0x07 & 0x78-0x7F
    Default: 32 (0x20)
    slave_bufflen 	Size of slave buffer used for master<->slave comunication in bytes;
    Range: 128 - 4096
    Default: 256
    For buffer sizes 128-256 bytes 8-bit addressing is used
    For buffer sizes >256 bytes 16-bit addressing is used
    Only used if SLAVE mode is selected
    slave_rolen 	Size of read-only area at the end of the slave buffer in bytes;
    Range: 1 - slave_bufflen/2
    Default: 0
    Master device can only read from that area
    Only used if SLAVE mode is selected
    slave_busy 	If set to True, the last byte of the slave buffer will be used as status register.
    Bit #8 of that register will be set to 1 by the driver after the write transaction is finished, as indication to the master that the slave is busy processing request.
    User program must reset this bit using i2c.resetbusy() function.
    Default: False
    Only used if SLAVE mode is selected

    Only sda and scl are required, all the others are optional and will be set to the default values if not given.

    i2c = machine.I2C(0, sda=21, scl=22)
    si2c = machine.I2C(1, mode=machine.I2C.SLAVE, sda=25, scl=26, slave_bufflen=512)"""
    pass

def DAC(pin) -> "DAC":
    """pin argument defines the gpio which will will be used as dac output.
    Only GPIOs 25 and 26 can be used as DAC outputs.
    The pin argument can be given as pin number (integer) or the machine.Pin object.

    # >>> import machine
    # >>> dac=machine.DAC(25)
    # >>> dac
    DAC(Pin(25), channel: 1)
    #>>> """
    pass

def ADC(pin, unit) -> "ADC":
    """pin argument defines the gpio which will will be used as adc input.
    It can be given as integer pin number, or machine.Pin(n) object.
    For ADC1 only GPIOs 32-39 can be used as ADC inputs.
    For ADC2 gpios 4, 0, 2, 15, 13, 12, 14, 27, 25, 26 can be used as ADC inputs.

    Be very carefull not to use the pins used by ESP32, especially the bootstrapping pins.

    Use machine.ADC.HALL constant to select ESP32 Hall sensor as input.
    If Hall sensor is used, gpio#36 and gpio#39 cannot be used as adc inputs at the same time.

    Optional unit argument select ESP32 ADC unit for this instance. Values 1 (ADC1, default) or 2 (ADC2) can be selected.

    Initially, the attenuation is set to 0 dB, and resolution to 12 bits."""
    pass

def freq(new_freq):
    """
    Get or set the current ESP32 CPU clock in Hz
    Executed without an argument returns the current CPU clock in Hz.

    When setting the frequency, new_freq argument can be entered in Hz or MHz.
    Only frequencies 2MHz, 80Mhz, 160MHz, 240MHz and crystal frequency are supported.
    If Power Management is enabled, the maximum frequency is set.
    """
    pass

def reset():
    """
    Reset the ESP32
    """
    pass

def wake_reason():
    """
    Returns 2-items tuple containing numeric representation of reset and wake-up reasons
    (reset_reason, wakeup_reason)

    Possible reset_reason values:
    0 - Power on reset
    1 - Hard reset
    2 - WDT reset
    3 - Deepsleep wake-up
    4 - Soft reset
    5 - Brownout reset
    6 - Soft reset
    7 - RTC WDT reset
    8 - Unknown reset reason

    Possible wakeup_reason values:
    0 - no wake-up reason
    1 - EXT_0 wake-up
    2 - EXT_1 wake-up
    3 - Touchpad wake-up
    4 - RTC wake-up
    5 - ULP wake-up
    """
    pass

def wake_description():
    """
    Returns 2-items tuple containing string description of reset and wake-up reasons
    """
    pass

def unique_id():
    """
    Returns bytearray (6 bytes) of unique ESP32 id.
    Base MAC address which is factory-programmed by Espressif is used as unique_id.
    """
    pass

def WDT(enable):
    """
    Get WDT (watchdog timer) status, optionally evable/disable WDT
    Set the optional argument enable to True to enable the watch dog, set it to False to disable the watch dog.
    The watchdog timeout period is set in menuconfig:
    → Component config → ESP32-specific → Task Watchdog timeout period (seconds)
    default value is is 15 seconds.
    """
    pass

def resetWDT():
    """
    Reset (feed) the watchdog timer.
    """
    pass

def stdin_disable(pattern):
    """
    Disable stdin, no characters will be processed from standard input until the pattern is matched.
    Maximum pattern length is 15 bytes.
    If the pattern contains characters > \x7f, the argument must be entered as bytearray (e.g., b'\xff\xfe\x03\x41').
    The pattern must be entered fast enough to arrive before the stdin timeout expires.

    # >>> import machine
    # >>> machine.stdin_disable("123abc")
    I (8855) [stdin]: Disabled, waiting for pattern [123abc]
    # no characters on stdin are accepted
    # >>> I (25508) [stdin]: Pattern matched, enabled

    # >>>

    """
    pass

def stdin_get(len, timeout):
    """
    Get string from stdin, wait maximum timeout ms
    None is returned on timeout.
    """
    pass

def stdout_put(buf):
    """
    Put the content of the buf object (string, bytearray, ...) to stdout.
    Returns number of bytes put.
    """
    pass

def SetStackSize(value):
    """
    Set the new MicroPython stack size.
    The stack size is stored in the NVM and will be used on the next (and all consecutive) reboot.
    """
    pass

def SetHeapSize(value):
    """
    Set the new MicroPython heap size.
    The heap size is stored in the NVM and will be used on the next (and all consecutive) reboot.
    """
    pass

def heap_info():
    """
    Prints the detailed information about the ESP32 heap space outside the MicroPython heap.
    If psRAM is used, the information about psRAM heap is also printed.

    # >>> machine.heap_info()
    Heap outside of MicroPython heap:
    #--------------------------------
                  Free: 237632
             Allocated: 20196
          Minimum free: 236212
          Total blocks: 87
    Largest free block: 113804
      Allocated blocks: 82
           Free blocks: 5

    SPIRAM info:
    #-----------
                  Free: 1048532
             Allocated: 3145728
          Minimum free: 1048532
          Total blocks: 2
    Largest free block: 1048532
      Allocated blocks: 1
           Free blocks: 1
    # >>>


    """
    pass

def deepsleep(timeout):
    """
    Put the ESP32 into deep sleep mode.
    You may want to configure some wake-up sorces using RTC module. timeout sets the sleep time in ms. If set to 0, the timer is not used as wake-up source.

    # >>> machine.deepsleep(10000)
    ESP32: DEEP SLEEP
    ets Jun  8 2016 00:22:57

    rst:0x5 (DEEPSLEEP_RESET),boot:0x3f (SPI_FAST_FLASH_BOOT)
    configsip: 0, SPIWP:0xee
    clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
    mode:DIO, clock div:1
    load:0x3fff0018,len:4
    load:0x3fff001c,len:4852
    load:0x40078000,len:0
    load:0x40078000,len:14728
    entry 0x40078d64

    Internal FS (SPIFFS): Mounted on partition 'internalfs' [size: 1048576; Flash address: 0x1F0000]
    ----------------
    Filesystem size: 956416 B
               Used: 512 B
               Free: 955904 B
    ----------------

    FreeRTOS running on BOTH CORES, MicroPython task running on both cores.
    Running from Factory partition starting at 0x10000, [MicroPython].

     Reset reason: Deepsleep wake-up
    Wakeup source: RTC wake-up
        uPY stack: 19456 bytes
         uPY heap: 3073664/5520/3068144 bytes (in SPIRAM using heap_caps_malloc)

    MicroPython ESP32_LoBo_v3.1.16 - 2017-02-04 on ESP32 board with ESP32
    Type "help()" for more information.
    # >>> import machine
    # >>> machine.wake_description()
    ('Deepsleep wake-up', 'RTC wake-up')
    # >>>

    """
    pass

def random(limit, upper_limit: Optional = None):
    """
    Returns random number between 0 and limit
    If the optional upper_limit argument is given, returns random number between limit and upper_limit

    """
    pass

def internal_temp():
    """
    Read the internal ESP32 temperature sensor
    Returns tuple of raw value and the temperature in °C
    Returned temperature has in internal offset which may be different on each ESP32 chip.
    Use this function only to measure the relative temperatures.

    # >>> import machine
    # >>> machine.internal_temp()
    (134, 56.66666793823243)



    Non-volatile storage support

        Non-volatile storage (NVS) is designed to store key-value pairs in flash.
        Currently NVS uses a portion of main flash memory through spi_flash_{read|write|erase} APIs.

    Integer and string values can be saved into NVS.
    Key - Value pairs are used as arguments for NVS methods.

    Variables saved in NVS are preserved on power off.
    """
    pass

def nvs_setint(key, value):
    """
    Save the integer value with name key in NVS
    """
    pass

def nvs_getint(key):
    """
    Return the saved integer key from NVS

    # >>> machine.nvs_setint('myvar', 12345678)
    # >>> machine.nvs_getint('myvar')
    12345678
    # >>>

    """
    pass

def nvs_setstr(key, value):
    """
    Save the string value with name key in NVS
    """
    pass

def nvs_getstr(key):
    """
    Return the saved string key from NVS

    # >>> machine.nvs_setstr('mystr', "String saved in NVS")
    # >>> machine.nvs_getstr('mystr')
    'String saved in NVS'
    # >>>

    """
    pass

def nvs_erase(key):
    """
    Erase the variable key from NVS
    """
    pass

def nvs_erase_all():
    """
    Erase all variables from NVS

    ESP32 loging handling

    ESP32 log messages can be disabled or enabled with the desired log level.
    Logging for the individual components or all components can be set.
    The following constants can be used for setting the log level:
    """
    pass

def loglevel(component, log_level):
    """
    Set the log level of the component to level log_level
    component is the name of the component as it apears in log messages.
    '*' can be used to set the global log level.

    """
    pass

