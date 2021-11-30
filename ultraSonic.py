#!/usr/bin/env python3
from smbus import SMBus
import time
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import UInt16MultiArray

import signal
import sys

###################################
#  run: sudo chmod 777 /dev/i2c-1
###################################

# sensor I2C address
address = [0x71, 0x72]

interval = 0.05


def signal_handler(sig, frame):
    print('exiting the program!')
    sys.exit(1)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to stop')

    rospy.init_node('ultraSonic_pub', anonymous=False)

    rate = rospy.Rate(50) # 10hz

    ultraSonic = rospy.Publisher('ultraSonic', UInt16MultiArray, queue_size=10)
    data = UInt16MultiArray()

    while(True):
        for i in range (len(address)):
            try:
                i2cbus = SMBus(1)
                i2cbus.write_byte(address[i], 0x51)
                time.sleep(0.1)
                val = i2cbus.read_word_data(address[i], 0xe1)

                distance = (val >> 8) & 0xff | ((val & 0x3) << 8)
                # print(distance)

                data.data.append(distance)
                if i == 1:
                    ultraSonic.publish(data)
                    print(data.data)
                    data.data.clear()

                print((val >> 8) & 0xff | ((val & 0x3) << 8), "cm","   |     from address: ",address[i])

            except IOError:
                print("error     |     sensor ",address[i]," not found")
    
        print("--------------------------------------")
        time.sleep(interval)

    signal.pause()
    rospy.spin()

