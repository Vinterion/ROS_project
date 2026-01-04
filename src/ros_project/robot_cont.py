#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2
import numpy as np

class robot_cont(Node):
    def __init__(self):
        super().__init__('robot_contloler')
        self.window_name = "robot_contloler"
        self.subscription = self.create_subscription(Image,'image_raw',self.listener_callback,10)
        self.subscription  
        self.point = None

    def listener_callback(self, image_data):
        pass
        

    def move_robot(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x,y)

if __name__ == '__main__':
    rclpy.init()
    cont_node = robot_cont()
    rclpy.spin(cont_node)
    cont_node.destroy_node()
    rclpy.shutdown()