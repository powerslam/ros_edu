#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from geometry_msgs.msg import Twist

class TurtlePub():
    def __init__(self):
        rospy.init_node('turtle_pub_node')
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        self.rate = rospy.Rate(0.5)
        self.cmd_msg = Twist()

    def func(self) -> None:
        self.cmd_msg.linear.x = 1
        self.pub.publish(self.cmd_msg)

if __name__ == '__main__':
    try:
        obj = TurtlePub()
        while not rospy.is_shutdown():
            obj.func()
            obj.rate.sleep()
    
    except rospy.ROSInterruptException:
        pass
