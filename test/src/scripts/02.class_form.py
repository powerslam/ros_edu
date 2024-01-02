#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

class ClassExample():
    def __init__(self):
        self.data = 0
    
    def func(self) -> None:
        pass

if __name__ == '__main__':
    try:
        obj = ClassExample()
        obj.func()
    
    except rospy.ROSInterruptException:
        pass
