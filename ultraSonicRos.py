#!/usr/bin/env python3
from os import name
from smbus import SMBus
import time
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import UInt16MultiArray
from diagnostic_msgs.msg import DiagnosticArray
from diagnostic_msgs.msg import DiagnosticStatus

import signal
import sys
import threading

###################################
#  run: sudo chmod 777 /dev/i2c-1
###################################

# sensor I2C address
address = [0x71, 0x72]

interval = 0.005

diagnostic_msg = DiagnosticArray()

def signal_handler(sig, frame):
    print('exiting the program!')
    sys.exit(1)

def change_diagnostic(index, msg = "ok", level = 0):
    diagnostic_msg.status[index].message = msg
    diagnostic_msg.status[index].level = level

def bit_publisher():
    threading.Timer(1.0, bit_publisher).start()
    bitUltraSonic.publish(diagnostic_msg)
    change_diagnostic(0)
    change_diagnostic(1)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print('Started ultra_sonic publisher\nPress Ctrl+C to stop')

    rospy.init_node('ultraSonic_pub', anonymous=False)

    rate = rospy.Rate(50) # 10hz

    ultraSonic = rospy.Publisher('ultra_sonic/out/raw', UInt16MultiArray, queue_size=10)
    bitUltraSonic = rospy.Publisher('bit/ultra_sonic', DiagnosticArray, queue_size=10)
    data = UInt16MultiArray()
    diagnostic_msg.status = [DiagnosticStatus(level=0, name='Permissions', message='ok'),
                             DiagnosticStatus(level=0, name='Connection', message='ok')]

    bit_publisher()

    while(True):
        for i in range (len(address)):
            try:
                i2cbus = SMBus(1)
                i2cbus.write_byte(address[i], 0x51)

                val = i2cbus.read_word_data(address[i], 0xe1)

                distance = (val >> 8) & 0xff | ((val & 0x3) << 8)

                data.data.append(distance)

                if i == 1:
                    ultraSonic.publish(data)
                    # print(data.data)
                    data.data.clear()
                # print((val >> 8) & 0xff | ((val & 0x3) << 8), "cm","   |     from address: ",address[i])
            
            # permission error
            except PermissionError:
                change_diagnostic(0, "run: sudo chmod 777 /dev/i2c-1", 2)

            # connection error
            except OSError:
                change_diagnostic(1, "Sensor is not connected", 2)


