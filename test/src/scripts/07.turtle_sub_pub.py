#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy

from turtlesim.msg import Pose
from turtlesim.msg import Color

from geometry_msgs.msg import Twist

class TurtleSub():
    def __init__(self):
        rospy.init_node('turtle_sub_node')
        rospy.Subscriber('/turtle1/pose', Pose, callback=self.pose_callback)
        rospy.Subscriber('/turtle1/color_sensor', Color, callback=self.color_callback)

        self.pose_msg = Pose()
        self.color_msg = Color()
        self.cmd_msg = Twist()
        self.rate = rospy.Rate(10)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

    def func(self) -> None:
        if self.color_msg.r < 100:
            print('new path')
            if 1 < self.pose_msg.x < 10:
                self.cmd_msg.linear.x = 4
                self.cmd_msg.angular.z = 0
            
            else:
                self.cmd_msg.linear.x = 0.5
                self.cmd_msg.angular.z = 0.5
        
        else:
            
            print("already passed")

        self.pub.publish(self.cmd_msg)
        sub.rate.sleep()

    def pose_callback(self, msg: Pose) -> None:
        #print('----- pose -----')
        self.pose_msg = msg
        #print(self.pose_msg)

    def color_callback(self, msg: Color) -> None:
        #print('----- color -----')
        self.color_msg = msg
        #print(self.color_msg)

if __name__ == '__main__':
    try:
        sub = TurtleSub()
        while not rospy.is_shutdown():
            sub.func()

        rospy.spin()
    
    except rospy.ROSInterruptException:
        pass
