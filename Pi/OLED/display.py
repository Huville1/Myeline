from midline import layout, coloring
import time
import board
import busio
import digitalio
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageColor
import adafruit_ssd1306

#setup oled device
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
#BORDER = 5

# Display Refresh
LOOPTIME = 1.0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

#number of electrodes:
enum = 2
image = layout(enum, oled)
oled.image(image)
oled.show()
time.sleep(LOOPTIME)