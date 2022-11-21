from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageShow
import matplotlib.pyplot as plt
# from OLED.midline import layout, coloring
from Screen.midline import layout, coloring
import time
import numpy as np

def display(index:list, enums:int):
    Width = 1024
    Height = 512 #scale up by 8
    image = coloring(index, enums, Width,Height)
    # image.show()
    a = ImageShow.show(image)
# print(a)
# def main():
#     display([],1)
