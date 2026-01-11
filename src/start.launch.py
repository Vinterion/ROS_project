import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
         Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[{'framerate': 30.0}] # Możesz dodać więcej parametrów
        ),
       Node(
            package='ros_project',
            executable='camera_subs',
            name='camera_subs'
        ),
        Node(
            package='ros_project',
            executable='robot_cont',
            name='robot_cont',
            output='screen'
        )
    ])