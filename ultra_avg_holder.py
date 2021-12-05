#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray

import time

import yaml


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
        print(filter_data.data)
        # call to the average function

        for i in zip(range(filter_data.data[0])):
            if filter_data.data[0][i]:


        filter_data.time = time.time()
    else:
        filter_data.data[0].append(data.data[0])
        filter_data.data[1].append(data.data[1])
filter_data.time = time.time()
filter_data.data = tuple()

def listener():

    rospy.init_node('listener', anonymous=True)

    read_from_yaml()

    rospy.Subscriber("ultra_sonic/out/raw", UInt16MultiArray , filter_data)

    rospy.spin()


if __name__ == '__main__':
    listener()