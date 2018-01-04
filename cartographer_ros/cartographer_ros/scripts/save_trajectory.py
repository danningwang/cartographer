#!/usr/bin/env python

PACKAGE = 'cartographer_ros'

import rospy
import csv
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import PoseWithCovariance
from nav_msgs.msg import Path

def callback(data):
	
	file_save=open("trajectory.csv",'w')
	for each_pose in data.poses:
		pose_time = each_pose.header.stamp
		positions = each_pose.pose.position
		orientations = each_pose.pose.orientation
		file_save.write(str(pose_time)+' '+str(positions.x)+' '+str(positions.y)+' '+str(positions.z)+' '+str(orientations.x)+' '+str(orientations.y)+' '+str(orientations.z)+' '+str(orientations.w))
		file_save.write('\n')
	rospy.loginfo("I heard %s")


    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
	rospy.init_node('listener', anonymous=True)
	rospy.loginfo("ready to subscribe %s")
	rospy.Subscriber("trajectory", Path, callback)

    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()


