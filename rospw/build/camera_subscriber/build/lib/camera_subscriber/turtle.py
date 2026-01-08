#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist,Point

class TWISTER(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, "/cmd_vel", 10)
        self.subscription = self.create_subscription(Point, "/point", self.p_call, 10)
        timer_period = 0.1  # seconds
        self.twist = Twist()
        self.timer = self.create_timer(timer_period, self.timer_callback)
    def p_call(self,msg):
        if msg.y <256:
            self.twist.linear.x = 0.5
        else:
            self.twist.linear.x = 0.0
    def timer_callback(self):      
        self.publisher_.publish(self.twist)
        self.get_logger().info("KRECI SIE")

def main(args=None):
    rclpy.init(args=args)
    T = TWISTER()
    rclpy.spin(T)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
