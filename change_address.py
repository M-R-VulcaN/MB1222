import smbus
import time
import subprocess
import os
import sys

dev = smbus.SMBus(1)
os.system("clear")

print("---------------------------------------------------------\nSearching for i2c devices...")
time.sleep(0.5)
print("This are the devices which are available:\n---------------------------------------------------------")

output = subprocess.check_output("i2cdetect -y 1", shell=True)
print(output)

print("---------------------------------------------------------\nNow you could change the sensor I2C address.\n---------------------------------------------------------")
 
try:
  addressOld = input("The actual sensor address (e. g. 0x70):")
  addressNew = input("The new sensor address (0x70 to 0x77):")
except ValueError:
  sys.exit()
 
print("---------------------------------------------------------\nChecking if the new address could be used (0x70 to 0x77)")

addressOld = int(addressOld, 16)
addressNew = int(addressNew, 16)

if addressNew in range(111, 120):
 
  time.sleep(0.5)
  print ("Changing the sensor I2C address...\n---------------------------------------------------------")

  addressNew = addressNew << 1

  dev.write_block_data(addressOld, 0xe0, [0xAA, 0xA5, addressNew])
  time.sleep(1)
  os.system("clear")
 
  print("---------------------------------------------------------\nSearching for i2c devices...")
  time.sleep(0.5)
  print("This are the devices which are available:")
  dev.write_block_data(addressOld, 0xe0, [0xAA, 0xA5, addressNew])
  print("---------------------------------------------------------")

  output = subprocess.check_output("i2cdetect -y 1", shell=True)
  print(output)
else:
  os.system("clear")
  print("---------------------------------------------------------\nThe new address is not vailid.\n---------------------------------------------------------")
