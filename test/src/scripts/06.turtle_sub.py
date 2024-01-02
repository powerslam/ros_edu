#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from turtlesim.msg import Pose
from turtlesim.msg import Color

class TurtleSub():
    def __init__(self):
        rospy.init_node('turtle_sub_node')
        rospy.Subscriber('/turtle1/pose', Pose, callback=self.pose_callback)
        rospy.Subscriber('/turtle1/color_sensor', Color, callback=self.color_callback)

    def pose_callback(self, msg: Pose) -> None:
        print(msg)

    def color_callback(self, msg: Color) -> None:
        print(msg)

if __name__ == '__main__':
    try:
        obj = TurtleSub()
        rospy.spin()
    
    except rospy.ROSInterruptException:
        pass
