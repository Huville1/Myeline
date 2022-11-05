import sys
import smbus2 as SMBus
import time

I2C_SLAVE_ADDRESS = 11
lights = [0,1,2,3,4,5]
# I2C_SLAVE2_ADDRESS = 12
# I2C_SLAVE3_ADDRESS = 13
i = 0

def ConvertStringsToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted

def main(args):
    #create the I2C bus
    I2Cbus = SMBus(1)
    # with smbus.SMBUS(1) as I2Cbus:
    while True:
        if (i == 6):
            i= i-6
        message = lights[i]
        #bytestoSend = ConvertStringsToBytes(message)
        print(message)
        I2Cbus.write_byte_data(80, 0, message)
        time.sleep(1)
        i+=1
            
    return 0
if __name__ == '__main__':
    try:
       main(sys.argv)
    except KeyboardInterrupt:
       print("program was stopped manually")
    input()
