#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Float64

class Turtle_sub():
    def __init__(self):
        rospy.init_node('sim_cmd_node') # 1. node 의 이름 설정(겹치면 한 쪽이 꺼짐)
        self.pub = rospy.Publisher('/commands/motor/speed', Float64, queue_size=1)
        self.cmd_msg = Float64()
        self.rate = rospy.Rate(2)
        self.speed = 1000
        
    def func(self) -> None:
        self.speed = min(2400, self.speed + 10)
        self.cmd_msg.data = self.speed
        self.pub.publish(self.cmd_msg)
        print(f'speed: {self.cmd_msg.data}')
        self.rate.sleep()

if __name__ == '__main__':
    try:
        pub = Turtle_sub()
        while not rospy.is_shutdown():
            pub.func()
    
    except rospy.ROSInterruptException:
        pass
