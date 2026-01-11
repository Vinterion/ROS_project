#!/usr/bin/env python3
import rclpy 
from geometry_msgs.msg import Point
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Time

class robot_cont(Node):
    def __init__(self):
        super().__init__('robot_contloler')
        self.window_name = "robot_contloler"
        self.subscription = self.create_subscription(Point,'/point',self.listener_callback,10)
        self.subscription 
        self.publisher_ = self.create_publisher(JointTrajectory, "/scaled_joint_trajectory_controller/joint_trajectory", 10)
        self.timer = self.create_timer(0.1, self.move_robot)
        self.traj = JointTrajectory()
        self.traj.joint_names = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]
        self.go_up = False
    def listener_callback(self, msg):
        if msg.y < 256:
            self.go_up = True
        else:
            self.go_up = False
        

    def move_robot(self):
        point = JointTrajectoryPoint()
        point.time_from_start = Time(sec=2, nanosec=0)
        point.positions = [0.0, 0.5, 0.0, 0.0, 0.0, 0.0] if self.go_up else [0.0, -0.5, 0.0, 0.0, 0.0, 0.0]
        self.traj = [point]
        self.publisher_.publish(self.traj)


if __name__ == '__main__':
    rclpy.init()
    cont_node = robot_cont()
    rclpy.spin(cont_node)
    cont_node.destroy_node()
    rclpy.shutdown()