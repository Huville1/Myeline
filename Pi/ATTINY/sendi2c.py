import sys
import smbus
import time

I2C_SLAVE_ADDRESS = 4
lights = [0x00,0x01,0x02,0x03,0x04,0x05]
# I2C_SLAVE2_ADDRESS = 12
# I2C_SLAVE3_ADDRESS = 13


def ConvertStringsToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted

def main(args):
    #create the I2C bus
    I2Cbus = smbus.SMBus(1)
    # with smbus.SMBUS(1) as I2Cbus:
    time.sleep(1)
    i = 0
    while True:
        if (i == 6):
            i= i-6
        message = lights[i]
        # .to_bytes(length=1, byteorder='little')
        #bytestoSend = ConvertStringsToBytes(message)
        print(message)
        I2Cbus.write_byte_data(I2C_SLAVE_ADDRESS, 0, message)
        time.sleep(5)
        i+=1
            
    return 0
if __name__ == '__main__':
    try:
       main(sys.argv)
    except KeyboardInterrupt:
       print("program was stopped manually")
    input()
