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

while True:
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    #below are border rep spine
    draw.line((0,10,oled.width,10), fill = 'red', width = 5)
    draw.line((0,oled.height-10,oled.width,oled.height-10), fill = 'red', width = 5)
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)
