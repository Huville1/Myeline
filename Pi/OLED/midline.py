#methods for displaying

import time
import board
import busio
import digitalio
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageColor
import adafruit_ssd1306

#global vars
yVals = [23, 30, 37, 44, 51, 58 ]
# Define the Reset Pin
def layout(n:int, oled:adafruit_ssd1306) -> Image:
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
    draw.line((0,16,oled.width,16), fill = 255, width= 1)

    #setting up layout
    enum = n # limit is 8 electrodes
    xSpace = np.floor(128/(1+enum))
    i=0
    while i < enum:
        if (enum == 1):
            draw.text((xSpace-8,0), "E" + str(i+1), font = font, fill = 255)
            draw.rectangle((xSpace-8, 17, xSpace+8, oled.height-1), outline = 255, fill = 0)
            draw.rectangle ((xSpace-2,yVals[0]-2,xSpace+2,yVals[0]+2),outline = 255, fill = 0)
            draw.rectangle ((xSpace-2,yVals[1]-2,xSpace+2,yVals[1]+2),outline = 255, fill = 0)
            draw.rectangle ((xSpace-2,yVals[2]-2,xSpace+2,yVals[2]+2),outline = 255, fill = 0)
            draw.rectangle ((xSpace-2,yVals[3]-2,xSpace+2,yVals[3]+2),outline = 255, fill = 0)
            draw.rectangle ((xSpace-2,yVals[4]-2,xSpace+2,yVals[4]+2),outline = 255, fill = 0)
            draw.rectangle ((xSpace-2,yVals[5]-2,xSpace+2,yVals[5]+2),outline = 255, fill = 0)
        else:
            x = 0 + ((i+1)*xSpace)
            draw.text((x-8,0), "E" + str(i+1), font = font, fill = 255)
            draw.rectangle((x-8, 17, x+8, oled.height-1), outline = 255, fill = 0)
            draw.rectangle ((x-2,yVals[0]-2,x+2,yVals[0]+2),outline = 255, fill = 0)
            draw.rectangle ((x-2,yVals[1]-2,x+2,yVals[1]+2),outline = 255, fill = 0)
            draw.rectangle ((x-2,yVals[2]-2,x+2,yVals[2]+2),outline = 255, fill = 0)
            draw.rectangle ((x-2,yVals[3]-2,x+2,yVals[3]+2),outline = 255, fill = 0)
            draw.rectangle ((x-2,yVals[4]-2,x+2,yVals[4]+2),outline = 255, fill = 0)
            draw.rectangle ((x-2,yVals[5]-2,x+2,yVals[5]+2),outline = 255, fill = 0)
        i+=1
    return image

def coloring(ind:int):
    w
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)

# draw.text((0, 0), "E1", font=font, fill=255)
# draw.rectangle ((0,17,15,oled.height-1),outline = 255, fill =0);

# #mini electrode dots -> need to make this into a loop
# draw.rectangle ((6,21,10,25),outline = 255, fill = 0)
# draw.rectangle ((6,28,10,32),outline = 255, fill = 0)
# draw.rectangle ((6,35,10,39),outline = 255, fill = 0)
# draw.rectangle ((6,42,10,46),outline = 255, fill = 0)
# draw.rectangle ((6,49,10,53),outline = 255, fill = 0)
# draw.rectangle ((6,56,10,60),outline = 255, fill = 0)
#electrode name splitter
#

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

