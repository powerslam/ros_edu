#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2
import rospy
from cv_bridge import CvBridge
from std_msgs.msg import Float64
from sensor_msgs.msg import CompressedImage

class Turtle_sub():
    def __init__(self):
        rospy.init_node('sim_cmd_node') # 1. node 의 이름 설정(겹치면 한 쪽이 꺼짐)
        rospy.Subscriber('/image_jpeg/compressed', CompressedImage, self.cam_CB)
        self.image_msg = CompressedImage()
        self.bridge = CvBridge()
        
    def cam_CB(self, msg: CompressedImage) -> None:
        self.image_msg = msg
        cv_img = self.bridge.compressed_imgmsg_to_cv2(self.image_msg)
        cv2.imshow('cv_img', cv_img)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        pub = Turtle_sub()
        rospy.spin()
    
    except rospy.ROSInterruptException:
        pass
