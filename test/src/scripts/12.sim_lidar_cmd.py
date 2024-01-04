#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from sensor_msgs.msg import LaserScan
from math import *

class Turtle_sub():
    def __init__(self):
        rospy.init_node('turtle_sub_node') # 1. node 의 이름 설정(겹치면 한 쪽이 꺼짐)
        rospy.Subscriber('/lidar2D', LaserScan, self.lidar_CB)
        self.scan_msg = LaserScan()
        
    def lidar_CB(self, msg: LaserScan) -> None:
        self.scan_msg = msg

        degree_min = self.scan_msg.angle_min * 180 / pi
        degree_max = self.scan_msg.angle_max * 180 / pi

        print(degree_min)
        print(degree_max)

if __name__ == '__main__':
    try:
        pub = Turtle_sub()
        rospy.spin()
    
    except rospy.ROSInterruptException:
        pass
