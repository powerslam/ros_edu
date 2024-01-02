#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

class ClassExample():
    def __init__(self):
        rospy.init_node('wego_pub_node')
        self.pub = rospy.Publisher('/counter', Int32, queue_size=1)
        self.int_msg = Int32()
        self.rate = rospy.Rate(10)

    def func(self) -> None:
        self.int_msg.data += 1
        self.pub.publish(self.int_msg)
        self.rate.sleep()
            

if __name__ == '__main__':
    try:
        obj = ClassExample()
        while not rospy.is_shutdown():
            obj.func()
    
    except rospy.ROSInterruptException:
        pass
