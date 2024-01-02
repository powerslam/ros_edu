#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

class ClassExample():
    def __init__(self):
        rospy.init_node('wego_sub_node') # 1. node 의 이름 설정(겹치면 한 쪽이 꺼짐)
        rospy.Subscriber('counter', Int32, callback=self.func)
        rospy.spin() # 2. 대기모드 설정

    def func(self, msg: Int32) -> None:
        print(msg.data * 2)


if __name__ == '__main__':
    try:
        obj = ClassExample()
        obj.func()
    
    except rospy.ROSInterruptException:
        pass
