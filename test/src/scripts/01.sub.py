#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

def callback(msg: Int32):
    print(msg.data * 2)

rospy.init_node('wego_sub_node') # 1. node 의 이름 설정(겹치면 한 쪽이 꺼짐)
rospy.Subscriber('counter', Int32, callback=callback)
rospy.spin() # 2. 대기모드 설정
