#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray

import time

import yaml
import statistics


#TODO: add roslaunch to params
BUNCH_TIME = 3     #in seconds
THRESHOLD = 25    #in cm


def filter_data(data):
    if time.time() - filter_data.time >= BUNCH_TIME:
        if filter_data.data[0] and filter_data.data[1]:
            print("first: " + str(filter_data.data[0]))
            print("second: " + str(filter_data.data[1]))

            filter_data.last = (statistics.mean(filter_data.data[0]), statistics.mean(filter_data.data[1]))
            print("first: " + str(filter_data.last[0]), " ,second: " + str(filter_data.last[1]))

        filter_data.data = ([],[])
        filter_data.time = time.time()
    else:
        if not filter_data.last:
            filter_data.last = (data.data[0], data.data[1])

        if abs(data.data[0] - filter_data.last[0]) < THRESHOLD and abs(data.data[1] - filter_data.last[1]) < THRESHOLD:
            filter_data.data[0].append(data.data[0])
            filter_data.data[1].append(data.data[1])

filter_data.time = time.time()
filter_data.data = ([],[])
filter_data.last = None


def listener():

    rospy.init_node('avg_ultra_sonic', anonymous=True)

    rospy.Subscriber("ultra_sonic/out/raw", UInt16MultiArray , filter_data)

    rospy.spin()


if __name__ == '__main__':
    listener()
