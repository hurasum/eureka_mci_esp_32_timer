
PATH = "C:/repository/esp32_python/functions_txt/{}"

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
            try:
                file_str += parseFunction(parse_function, filter_word, in_class)
            except TypeError:
                pass
            parse_function = []
        parse_function.append(line)
    return file_str

def display():
    dpy = open(PATH.format("display.py"), "w")
    dpy.write("\"\"\"\nDisplay typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class TFT:\n")

    dtxt = PATH.format("display_functions.txt")
    file_str = parseTextFile(dtxt, "tft", True)
    dpy.write(file_str)
    dpy.close()

def machine():
    dpy = open(PATH.format("machine.py"), "w")
    dpy.write("\"\"\"\nMachine typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")

    dtxt = PATH.format("machine_functions.txt")
    file_str = parseTextFile(dtxt, "machine", False)
    dpy.write(file_str)
    dpy.close()

def neopixel():
    dpy = open(PATH.format("neo_pixel.py"), "w")
    dpy.write("\"\"\"\nNeo Pixel typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class NeoPixel:\n")

    dtxt = PATH.format("neopixel_functions.txt")
    file_str = parseTextFile(dtxt, "np", True)
    dpy.write(file_str)
    dpy.close()

def adc():
    dpy = open(PATH.format("adc.py"), "w")
    dpy.write("\"\"\"\nADC typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class ADC:\n")

    dtxt = PATH.format("adc_functions.txt")
    file_str = parseTextFile(dtxt, "adc", True)
    dpy.write(file_str)
    dpy.close()

def dac():
    dpy = open(PATH.format("dac.py"), "w")
    dpy.write("\"\"\"\nDAC typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class DAC:\n")

    dtxt = PATH.format("dac_functions.txt")
    file_str = parseTextFile(dtxt, "dac", True)
    dpy.write(file_str)
    dpy.close()

def pwm():
    dpy = open(PATH.format("pwm.py"), "w")
    dpy.write("\"\"\"\nPWM typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class PWM:\n")

    dtxt = PATH.format("pwm_functions.txt")
    file_str = parseTextFile(dtxt, "pwm", True)
    dpy.write(file_str)
    dpy.close()

def ow():
    dpy = open(PATH.format("one_wire.py"), "w")
    dpy.write("\"\"\"\nOne Wire typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class OW:\n")

    dtxt = PATH.format("ow_functions.txt")
    file_str = parseTextFile(dtxt, "ow", True)
    dpy.write(file_str)
    dpy.close()

def rtc():
    dpy = open(PATH.format("rtc.py"), "w")
    dpy.write("\"\"\"\nRTC typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class RTC:\n")

    dtxt = PATH.format("rtc_functions.txt")
    file_str = parseTextFile(dtxt, "rtc", True)
    dpy.write(file_str)
    dpy.close()

def timer_f():
    dpy = open(PATH.format("timer.py"), "w")
    dpy.write("\"\"\"\nTimer typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class TM:\n")

    dtxt = PATH.format("timer_functions.txt")
    file_str = parseTextFile(dtxt, "tm", True)
    dpy.write(file_str)
    dpy.close()

def uart():
    dpy = open(PATH.format("uart.py"), "w")
    dpy.write("\"\"\"\nUART typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class UART:\n")

    dtxt = PATH.format("uart_functions.txt")
    file_str = parseTextFile(dtxt, "uart", True)
    dpy.write(file_str)
    dpy.close()

def i2c():
    dpy = open(PATH.format("i2c.py"), "w")
    dpy.write("\"\"\"\nI2C typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class I2C:\n")

    dtxt = PATH.format("i2c_functions.txt")
    file_str = parseTextFile(dtxt, "i2c", True)
    dpy.write(file_str)
    dpy.close()

def spi():
    dpy = open(PATH.format("spi.py"), "w")
    dpy.write("\"\"\"\nSPI typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class SPI:\n")

    dtxt = PATH.format("spi_functions.txt")
    file_str = parseTextFile(dtxt, "spi", True)
    dpy.write(file_str)
    dpy.close()

def pin():
    dpy = open(PATH.format("pin.py"), "w")
    dpy.write("\"\"\"\nSPI typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class PIN:\n")

    dtxt = PATH.format("pin_functions.txt")
    file_str = parseTextFile(dtxt, "pin", True)
    dpy.write(file_str)
    dpy.close()

def ds():
    dpy = open(PATH.format("ds_one_wire.py"), "w")
    dpy.write("\"\"\"\nSPI typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class DS:\n")

    dtxt = PATH.format("ds_ow_functions.txt")
    file_str = parseTextFile(dtxt, "ds", True)
    dpy.write(file_str)
    dpy.close()

def th():
    dpy = open(PATH.format("thread.py"), "w")
    dpy.write("\"\"\"\nThread typing class\n\"\"\"\n")
    dpy.write("\n")
    dpy.write("\n")
    dpy.write("class Thread:\n")

    dtxt = PATH.format("thread.txt")
    file_str = parseTextFile(dtxt, "_thread", True)
    dpy.write(file_str)
    dpy.close()

# th()
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
