

from lib import display
import time
from lib import machine
## imports must be updated for uc

def ellipseDemo(dofill=False):
    while True:
        time.sleep(0.2)
        x = machine.random(50, 155)
        y = machine.random(50, 70)
        if x < y:
            rx = machine.random(2, x)
        else:
            rx = machine.random(2, y)
        if x < y:
            ry = machine.random(2, x)
        else:
            ry = machine.random(2, y)
        bg_color = machine.random(0xFFFFFF)
        if dofill:
            fill = machine.random(0xFFFFFF)
            tft.ellipse(x, y, rx, ry, 15, bg_color, fill)
        else:
            tft.ellipse(x, y, rx, ry, 15, bg_color)


# initialize the display
tft = display.TFT()
tft.init(tft.ST7789, rst_pin=23, backl_pin=4, miso=0, mosi=19, clk=18, cs=5, dc=16, width=235, height=340, backl_on=1)

# invert colors
tft.tft_writecmd(0x21)

# set orientation (optional)
tft.orient(tft.LANDSCAPE)

# set window size
tft.setwin(40, 52, 278, 186)

for i in range(0, 241):
    color = 0xFFFFFF-tft.hsb2rgb(i/241*360, 1, 1)
    tft.line(i, 0, i, 135, color)
tft.set_fg(0x000000)
text = "Powered by Daniel!"
tft.text(120-int(tft.textWidth(text)/2), 67-int(tft.fontSize()[1]/2), text, 0xFFFFFF)
time.sleep(2)
tft.clear()
ellipseDemo()

