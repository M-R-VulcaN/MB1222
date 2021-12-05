#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray

import time

import yaml


#TODO: AVG
#TODO: value_threshhold


#TODO: move those params in to a file. (yaml?)
WINDOW_TIME = 3     #in seconds
MAX_DISTANCE = 210  #in cm
MIN_DISTANCE = 20   #in cm


yaml_file_full_path = "/home/makeruser/MB1222/params.yaml"

def read_from_yaml():
    global WINDOW_TIME, MAX_DISTANCE, MIN_DISTANCE
    with open(yaml_file_full_path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    WINDOW_TIME = data_loaded["Parameters"]["Window_Time"]
    MAX_DISTANCE = data_loaded["Parameters"]["Max_Distance"]
    MIN_DISTANCE = data_loaded["Parameters"]["Min_Distance"]

def filter_data(data):
    if time.time() - filter_data.time >= WINDOW_TIME:
        print (filter_data.data)
        filter_data.time = time.time()
    else:
        filter_data.append(data)
filter_data.time = time.time()
filter_data.data = list()

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("ultraSonic_pub", UInt16MultiArray , filter_data)
    
    read_from_yaml()

    rospy.spin()


if __name__ == '__main__':
    listener()