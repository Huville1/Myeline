import serial 
import numpy as np
import time
# from typing import Tuple
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
data = [] # all data collected from pins on module
i = 0 # pin number
temp = 0
def receive (secs:float) -> list: # takes in how long to read, output data  
    data = []
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
# ser.open()
    if ser.is_open == True:
        print("\nAll right, serial port now open. Configuration:\n")
        print(ser, "\n") #print serial parameters
    else:
       print("Opening Serial Connections")
       ser.open()
       a = ser.is_open
       print("Serial condition:" + str(a)) 
    timeout = time.time() + secs
    ser.flush()
    while time.time() < timeout:
        if ser.in_waiting >0:
            value = ser.readline()
            #print(message)
            #value = int(message)
            print(value)
            data.append(value)
    return data

#showing the data: http://www.mikeburdis.com/wp/notes/plotting-serial-port-data-using-python-and-matplotlib/
#creating figures
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# xs = [] #store x values
# ys = [] #store y values
# # i = 0

# def animate(i,xs, ys):
#     #aquire data
    
#     ser.reset_input_buffer()
#     if ser.in_waiting >0:
#         message = ser.readline() #ascii
#         lmessage = message.split(b',')
#         i = int(lmessage[0])
#         value = int(message[1])
#         xs.append(i)
#         ys.append(value)
#         # i+=1
#         ax.clear()
#         ax.plot(xs,ys,label = 'signal') 

#         # format plot
#         plt.subplots_adjust(bottom = 0.30)
#         plt.title("Data Graph")
#         plt.ylabel("signal numbers")
#         plt.legend()
        
# ani = animation.FuncAnimation(fig,animate, fargs = (xs,ys))
# plt.show()

        








    
#     while True:
#         if ser.in_waiting > 0:
#             message = ser.readline()
#             value = int(message)
#             print(value)

            # print( yte)
            # if byte != b'':
            #     ints = int.from_bytes(byte,byteorder = 'big')
            #     print(ints)