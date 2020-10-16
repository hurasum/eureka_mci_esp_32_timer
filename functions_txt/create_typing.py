

def parseFunction(parse_function, filter_word, in_class):
    new_line = ""
    f_str = ""
    for line in parse_function:
        if line.startswith(f"{filter_word}."):
            line = line.replace("\n", "")
            line = line.replace(f"{filter_word}.", "")
            line = line.replace(", [", ",")
            line = line.replace("[,", ",")
            line = line.replace(" [", ",")
            line = line.replace("[", "")
            line = line.replace("]", "")
            if in_class:
                if "()" in line:
                    line = line.replace("(", "(self")
                else:
                    line = line.replace("(", "(self, ")
            f_str = "def {}:\n    \"\"\"place_holder    \"\"\"\n    pass\n\n".format(line)
        else:
            line = line.replace(">>>", "# >>>")
            new_line += "    {}".format(line)
    if f_str:
        return f_str.replace("place_holder", "{}".format(new_line))

def parseTextFile(path, filter_word, in_class):
    dtxt = open(path, "r")
    parse_function = []
    file_str = ""
    for idx, line in enumerate(dtxt.readlines()):
        if line.startswith(f"{filter_word}.") and idx != 0:
            file_str += parseFunction(parse_function, filter_word, in_class)
            parse_function = []
        parse_function.append(line)
    return file_str

def display():
    dpy = open("C:/repository/esptool-master/lol/display.py", "w")
    dpy.write("\"\"\"\nDisplay typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class TFT:\n")

    dtxt = "C:/repository/esptool-master/lol/display_functions.txt"
    file_str = parseTextFile(dtxt, "tft", True)
    dpy.write(file_str)
    dpy.close()

def machine():
    dpy = open("C:/repository/esptool-master/lol/machine.py", "w")
    dpy.write("\"\"\"\nMachine typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")

    dtxt = "C:/repository/esptool-master/lol/machine_functions.txt"
    file_str = parseTextFile(dtxt, "machine", False)
    dpy.write(file_str)
    dpy.close()

def neopixel():
    dpy = open("C:/repository/esptool-master/lol/neo_pixel.py", "w")
    dpy.write("\"\"\"\nNeo Pixel typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class NeoPixel:\n")

    dtxt = "C:/repository/esptool-master/lol/neopixel_functions.txt"
    file_str = parseTextFile(dtxt, "np", True)
    dpy.write(file_str)
    dpy.close()

def adc():
    dpy = open("C:/repository/esptool-master/lol/adc.py", "w")
    dpy.write("\"\"\"\nADC typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class ADC:\n")

    dtxt = "C:/repository/esptool-master/lol/adc_functions.txt"
    file_str = parseTextFile(dtxt, "adc", True)
    dpy.write(file_str)
    dpy.close()

def dac():
    dpy = open("C:/repository/esptool-master/lol/dac.py", "w")
    dpy.write("\"\"\"\nDAC typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class DAC:\n")

    dtxt = "C:/repository/esptool-master/lol/dac_functions.txt"
    file_str = parseTextFile(dtxt, "dac", True)
    dpy.write(file_str)
    dpy.close()

def pwm():
    dpy = open("C:/repository/esptool-master/lol/pwm.py", "w")
    dpy.write("\"\"\"\nPWM typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class PWM:\n")

    dtxt = "C:/repository/esptool-master/lol/pwm_functions.txt"
    file_str = parseTextFile(dtxt, "pwm", True)
    dpy.write(file_str)
    dpy.close()

def ow():
    dpy = open("C:/repository/esptool-master/lol/one_wire.py", "w")
    dpy.write("\"\"\"\nOne Wire typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class OW:\n")

    dtxt = "C:/repository/esptool-master/lol/ow_functions.txt"
    file_str = parseTextFile(dtxt, "ow", True)
    dpy.write(file_str)
    dpy.close()

def rtc():
    dpy = open("C:/repository/esptool-master/lol/rtc.py", "w")
    dpy.write("\"\"\"\nRTC typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class RTC:\n")

    dtxt = "C:/repository/esptool-master/lol/rtc_functions.txt"
    file_str = parseTextFile(dtxt, "rtc", True)
    dpy.write(file_str)
    dpy.close()

def timer_f():
    dpy = open("C:/repository/esptool-master/lol/timer.py", "w")
    dpy.write("\"\"\"\nTimer typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class TM:\n")

    dtxt = "C:/repository/esptool-master/lol/timer_functions.txt"
    file_str = parseTextFile(dtxt, "tm", True)
    dpy.write(file_str)
    dpy.close()

def uart():
    dpy = open("C:/repository/esptool-master/lol/uart.py", "w")
    dpy.write("\"\"\"\nUART typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class UART:\n")

    dtxt = "C:/repository/esptool-master/lol/uart_functions.txt"
    file_str = parseTextFile(dtxt, "uart", True)
    dpy.write(file_str)
    dpy.close()

def i2c():
    dpy = open("C:/repository/esptool-master/lol/i2c.py", "w")
    dpy.write("\"\"\"\nI2C typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class I2C:\n")

    dtxt = "C:/repository/esptool-master/lol/i2c_functions.txt"
    file_str = parseTextFile(dtxt, "i2c", True)
    dpy.write(file_str)
    dpy.close()

def spi():
    dpy = open("C:/repository/esptool-master/lol/spi.py", "w")
    dpy.write("\"\"\"\nSPI typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class SPI:\n")

    dtxt = "C:/repository/esptool-master/lol/spi_functions.txt"
    file_str = parseTextFile(dtxt, "spi", True)
    dpy.write(file_str)
    dpy.close()

def pin():
    dpy = open("C:/repository/esptool-master/lol/pin.py", "w")
    dpy.write("\"\"\"\nSPI typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class PIN:\n")

    dtxt = "C:/repository/esptool-master/lol/pin_functions.txt"
    file_str = parseTextFile(dtxt, "pin", True)
    dpy.write(file_str)
    dpy.close()

def ds():
    dpy = open("C:/repository/esptool-master/lol/ds_one_wire.py", "w")
    dpy.write("\"\"\"\nSPI typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class DS:\n")

    dtxt = "C:/repository/esptool-master/lol/ds_ow_functions.txt"
    file_str = parseTextFile(dtxt, "ds", True)
    dpy.write(file_str)
    dpy.close()

# ds()
# neopixel()
# adc()
# dac()
# pwm()
# ow()
# rtc()
# timer_f()
# uart()
# i2c()
# spi()
# pin()
# display()
# machine()
