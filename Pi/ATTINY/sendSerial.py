import serial 
import numpy as np
import matplotlib.pyplot as plt
data = [] # all data collected from pins on module
i = 0 # pin number
temp = 0
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    while 5000:
        if ser.in_waiting > 0:
            byte = ser.readline().decode('utf-8').rstrip()
            data.append(byte)
        i+=1
    plt.plot(data)
    plt.show()
            # print( yte)
            # if byte != b'':
            #     ints = int.from_bytes(byte,byteorder = 'big')
            #     print(ints)