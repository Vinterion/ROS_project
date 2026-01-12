import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    usb_cam_cfg = os.path.join(
        get_package_share_directory("ros_project"),
        'config',
        'params.yaml'
    )
    return LaunchDescription([
        Node(
            package='image_publisher',
            executable='image_publisher_node',
            name='fake_camera',
            arguments=["/src/src/fake_came.png"], 
            parameters=[{'publish_frequency': 30.0}],
            remappings=[('image_raw', '/image_raw')]
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