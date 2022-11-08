import serial 

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            byte = ser.read()
            if byte != b'':
                ints = int.from_bytes(byte,byteorder = 'big')
                print(ints)
            print(byte)