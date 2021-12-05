#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray

import time

import yaml
import statistics



#TODO: AVG
#TODO: value_threshhold


#TODO: move those params in to a file. (yaml?)
WINDOW_TIME = 0     #in seconds
MAX_DISTANCE = 0    #in cm
MIN_DISTANCE = 0    #in cm

yaml_file_full_path = "params.yaml"

def read_from_yaml():
    global WINDOW_TIME, MAX_DISTANCE, MIN_DISTANCE
    with open(yaml_file_full_path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    WINDOW_TIME = data_loaded["Parameters"]["Window_Time"]
    MAX_DISTANCE = data_loaded["Parameters"]["Max_Distance"]
    MIN_DISTANCE = data_loaded["Parameters"]["Min_Distance"]

def filter_data(data):
    if time.time() - filter_data.time >= WINDOW_TIME:
        print("first: " + str(filter_data.data[0]))
        print("second: " + str(filter_data.data[1]))

        print("first: " + str(statistics.mean(filter_data.data[0])), " ,second: " + str(statistics.mean(filter_data.data[1])))

        filter_data.data = tuple([],[])
        filter_data.time = time.time()
    else:
        if filter_data.last == None:
            filter_data.last = (data.data[0], data.data[1])

        if abs(data.data[0] - filter_data.last[0]) < MAX_DISTANCE or abs(data.data[1] - filter_data.last[1]) < MAX_DISTANCE:
            filter_data.data[0].append(data.data[0])
            filter_data.data[1].append(data.data[1])

filter_data.time = time.time()
filter_data.data = tuple([],[])
filter_data.last = None


def listener():

    rospy.init_node('listener', anonymous=True)

    read_from_yaml()

    rospy.Subscriber("ultra_sonic/out/raw", UInt16MultiArray , filter_data)

    rospy.spin()


if __name__ == '__main__':
    listener()