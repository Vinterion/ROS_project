#!/bin/bash
set -e
source /opt/ros/humble/setup.sh
mkdir -p /ros2_ws/src
cd /ros2_ws
colcon build
source /ros2_ws/install/setup.sh
cd /ros2_ws/src
ros2 pkg create ros_project --build-type ament_python --dependencies cv_bridge python3-opencv sensor_msgs geometry_msgs
cd /ros2_ws
colcon build
exec "$@"