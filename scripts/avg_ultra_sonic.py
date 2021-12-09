#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray

import time

import statistics


BUNCH_TIME = 0     #in seconds
THRESHOLD = 0    #in cm


def filter_data(data):
    
    if time.time() - filter_data.time >= BUNCH_TIME:
        if filter_data.data[0] and filter_data.data[1]:
            filter_data.last = (int(statistics.mean(filter_data.data[0])), int(statistics.mean(filter_data.data[1])))

            avg.data = filter_data.last
            avg_publisher.publish(avg)

        filter_data.data = ([],[])
        filter_data.time = time.time()
    else:
        if not filter_data.last and abs(data.data[0] - data.data[1]) < THRESHOLD:
            filter_data.last = (data.data[0], data.data[1])

        if filter_data.last and abs(data.data[0] - filter_data.last[0]) < THRESHOLD and abs(data.data[1] - filter_data.last[1]) < THRESHOLD:
            filter_data.data[0].append(data.data[0])
            filter_data.data[1].append(data.data[1])
filter_data.time = time.time()
filter_data.data = ([],[])
filter_data.last = None
    
if __name__ == '__main__':
    rospy.init_node('avg_ultra_sonic', anonymous=True)

    BUNCH_TIME = rospy.get_param("~window_time", 3)     
    THRESHOLD = rospy.get_param("~threshold", 25)  
    
    avg_publisher = rospy.Publisher('avg_ultra_sonic/out/raw', UInt16MultiArray, queue_size=10)
    avg = UInt16MultiArray()

    rospy.Subscriber("ultra_sonic/out/raw", UInt16MultiArray , filter_data)

    rospy.spin()
