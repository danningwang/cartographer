#!/usr/bin/env python

PACKAGE = 'slam_karto'

import rospy
import csv
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import LaserScan

def callback(data):
	rospy.loginfo("I heard %s")
	data_time=data.header.stamp
	laser=data.ranges
	file_save.write(str(data_time)+','+str(laser))
	file_save.write('\n')


    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
	rospy.init_node('listener', anonymous=True)
	rospy.loginfo("ready to subscribe %s")
	rospy.Subscriber("base_laser_front/scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	global file_save
	file_save=open("laser_data.csv",'w')
	listener()


