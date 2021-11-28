#!/usr/bin/env python3
from smbus import SMBus
import time

# sensor I2C address
# address = [0x70,0x71,0x72,0x73,0x74]
address = [0x71]

interval = 0.05

while(True):
   for i in range (len(address)):
       try:
           i2cbus = SMBus(1)
           i2cbus.write_byte(address[i], 0x51)
           time.sleep(0.1)
           val = i2cbus.read_word_data(address[i], 0xe1)
           print((val >> 8) & 0xff | ((val & 0x3) << 8), "cm","   |     from address: ",address[i])
           i+=1
       except IOError:
           print("error     |     sensor ",address[i]," not found")
  
   print("--------------------------------------")
   time.sleep(interval)
