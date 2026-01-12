#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from geometry_msgs.msg import Point
from cv_bridge import CvBridge 
import cv2
import numpy as np

class camera_subs(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.window_name = "camera"
        self.subscription = self.create_subscription(Image,'image_raw',self.listener_callback,10)
        self.subscription
        self.publisher_ = self.create_publisher(Point, '/point', 10)
        self.point = None

    def listener_callback(self, image_data):
        cv_image = np.zeros((512,700,3), np.uint8)
        if(self.point is not None):
            cv2.rectangle(cv_image,self.point,(self.point[0]+50,self.point[1]+50),(0,255,0),3)
        cv2.imshow(self.window_name, cv_image)
        cv2.waitKey(25)
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x,y)
            p = Point()
            p.x = x
            p.y = y
            self.publisher_.publish(p)
def main():
    rclpy.init()
    camera_node = camera_subs()
    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()