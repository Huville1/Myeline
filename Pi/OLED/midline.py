import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont, ImageColor
import adafruit_ssd1306


# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 15)

draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

draw.text((0, 0), "E1", font=font, fill=255)
draw.line((0,16,oled.width,16), fill = 255, width= 1)
#electrode shell
draw.rectangle ((0,17,15,oled.height-1),outline = 255, fill =0);
draw.rectangle ((7,19,9,21),outline = 255, fill = 0)
draw.rectangle ((7,26,9,29),outline = 255, fill = 0)
draw.rectangle ((7,33,9,36),outline = 255, fill = 0)
draw.rectangle ((7,40,9,43),outline = 255, fill = 0)
draw.rectangle ((7,47,9,50),outline = 255, fill = 0)
draw.rectangle ((7,54,9,57),outline = 255, fill = 0)
# lnTh = 10
# # electrode design
# enum = 1
# eWidth = int(WIDTH/enum)
# eHeight = (oled.height - lnTh)-lnTh

# #black background
# draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
# draw.rectangle((0,0,10,17), outline= 0,fill=255)

# #below are border rep spine
# draw.line((0,lnTh,oled.width,lnTh), fill = 125, width = 5)
# draw.line((0,oled.height-lnTh,oled.width,oled.height-lnTh), fill = 125, width = 5)


#showing the image
oled.image(image)
oled.show()
time.sleep(LOOPTIME)
