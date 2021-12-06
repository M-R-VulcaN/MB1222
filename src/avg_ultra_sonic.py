#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray

import time

import yaml
import statistics



#TODO: AVG
#TODO: value_threshhold


#TODO: move those params in to a file. (yaml?)
BUNCH_TIME = 0     #in seconds
MAX_JUMP = 0    #in cm

yaml_file_full_path = "params.yaml"

def filter_data(data):
    if time.time() - filter_data.time >= BUNCH_TIME:
        print("first: " + str(filter_data.data[0]))
        print("second: " + str(filter_data.data[1]))

        print("first: " + str(statistics.mean(filter_data.data[0])), " ,second: " + str(statistics.mean(filter_data.data[1])))

        filter_data.data = ([],[])
        filter_data.time = time.time()
    else:
        if filter_data.last == None:
            filter_data.last = (data.data[0], data.data[1])

        if abs(data.data[0] - filter_data.last[0]) < MAX_JUMP and abs(data.data[1] - filter_data.last[1]) < MAX_JUMP:
            filter_data.data[0].append(data.data[0])
            filter_data.data[1].append(data.data[1])

filter_data.time = time.time()
filter_data.data = ([],[])
filter_data.last = None


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("ultra_sonic/out/raw", UInt16MultiArray , filter_data)

    rospy.spin()


if __name__ == '__main__':
    listener()
