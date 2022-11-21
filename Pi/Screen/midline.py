from array import array
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageColor

yVals = [184, 240, 296, 352, 408, 464]
def layout(n:int, w:int, h: int)->Image:
    image = Image.new('RGB', (w,h)) #RGB image that has black background
    draw = ImageDraw.Draw(image)
    print("setup new image")
    #reseting the background to have a completely black one
    # draw.rectangle((0, 0, w, h), outline=255, fill=(255)
    draw.rectangle((0, 0, w, h), outline=0, fill=0)
    font = ImageFont.truetype('arial.ttf', 80)
    #drawing line to separate the text from electrodes
    draw.line((0,124,w,124), fill = (255,255,0), width= 1)
    enum = n # limit is 7 electrodes
    xSpace = np.floor(864/(1+enum))
    i=0
    while i < enum:
        if (enum == 1):
            draw.text(((xSpace-48)+80,32), "E" + str(i+1), font = font, fill = (255,255,0))
            draw.rectangle(((xSpace-54)+80, 130, xSpace+54+80, h-8), outline = (0,0,255), fill = 0)
            draw.ellipse ((xSpace-15+80,yVals[0]-15,xSpace+15+80,yVals[0]+15),outline = (0,0,255), fill = 0)
            draw.ellipse ((xSpace-15+80,yVals[1]-15,xSpace+15+80,yVals[1]+15),outline = (0,0,255), fill = 0)
            draw.ellipse ((xSpace-15+80,yVals[2]-15,xSpace+15+80,yVals[2]+15),outline = (0,0,255), fill = 0)
            draw.ellipse((xSpace-15+80,yVals[3]-15,xSpace+15+80,yVals[3]+15),outline = (0,0,255), fill = 0)
            draw.ellipse ((xSpace-15+80,yVals[4]-15,xSpace+15+80,yVals[4]+15),outline = (0,0,255), fill = 0)
            draw.ellipse ((xSpace-15+80,yVals[5]-15,xSpace+15+80,yVals[5]+15),outline = (0,0,255), fill = 0)
            # draw.line((xSpace-54+80,124+187-16,xSpace-30+80, 124+187), fill= (0,0,255),width=1)
            # draw.line((xSpace-30+80,124+187,xSpace-54+80, 124+187+16), fill= (0,0,255),width=1)
            # draw.line((xSpace-54+80,124+187-16,xSpace-54+80,124+187+16), fill = 0, width = 1)
        else:
            x = 0 + ((i+1)*xSpace)
            draw.text((x-48+80,32), "E" + str(i+1), font = font, fill = (255,255,0))
            draw.rectangle((x-54+80, 130, x+54+80, h-8), outline = (0,0,255), fill = 0)
            draw.ellipse ((x-15+80,yVals[0]-15,x+15+80,yVals[0]+15),outline = (0,0,255), fill = 0)
            draw.ellipse ((x-15+80,yVals[1]-15,x+15+80,yVals[1]+15),outline = (0,0,255), fill = 0)
            draw.ellipse((x-15+80,yVals[2]-15,x+15+80,yVals[2]+15),outline = (0,0,255), fill = 0)
            draw.ellipse((x-15+80,yVals[3]-15,x+15+80,yVals[3]+15),outline = (0,0,255), fill = 0)
            draw.ellipse((x-15+80,yVals[4]-15,x+15+80,yVals[4]+15),outline = (0,0,255), fill = 0)
            draw.ellipse ((x-15+80,yVals[5]-15,x+15+80,yVals[5]+15),outline = (0,0,255), fill = 0)
            # draw.line((x-54+80,124+187-16,x-30+80, 124+187), fill= (0,0,255),width=1)
            # draw.line((x-30+80,124+187,x-54+80, 124+187+16), fill= (0,0,255),width=1)
            # draw.line((x-54+80,124+187-16,x-54+80,124+187+16), fill = 0, width = 1)
        i+=1
    print("image return")

    #head label
    draw.text((20,221-40),"C",font =font, fill =(255,255,0))
    draw.text((20,318-40),"R",font =font, fill =(255,255,0))
    draw.text((20,415-40),"A",font =font, fill =(255,255,0))
    #Toe label:
    draw.text((w-70,221-40),"C",font =font, fill =(255,255,0))
    draw.text((w-70,318-40),"A",font =font, fill =(255,255,0))
    draw.text((w-70,415-40),"U",font =font, fill =(255,255,0))
    #border lines:
    #left
    draw.line((80,124,80,h),fill = (255,255,0), width= 1)
    #right
    draw.line((w-80,124,w-80,h),fill = (255,255,0), width= 1)

    return image

def coloring(ind:list, enum: int, w:int, h:int)->Image:
    ########### ind should be size enum ######################
    image = layout(enum, w,h)
    draw = ImageDraw.Draw(image)
    xSpace = np.floor(864/(1+enum))
    if ind:
        i = 0
        while i < enum:
            if (enum == 1):
                draw.ellipse((xSpace-15+80,yVals[ind[i]]-15,xSpace+15+80,yVals[ind[i]]+15), outline = 0, fill =(255,255,255))
            else:
                x = 0 + ((i+1)*xSpace)
                draw.ellipse((x-15+80,yVals[ind[i]]-15,x+15+80,yVals[ind[i]]+15),outline = 0,fill = (255,255,255))
            i+=1
    print("image from coloring is returned")
    return image