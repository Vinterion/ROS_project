FROM osrf/ros:rolling-desktop

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-rolling-cv-bridge \
   # ros-humble-usb-cam \
    ros-rolling-ur \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install "numpy<2" opencv-contrib-python-headless --break-system-packages

WORKDIR /ros2_ws
RUN source /opt/ros/rolling/setup.sh
RUN colcon build
RUN source ./install/setup.sh

WORKDIR /ros2_ws/src
RUN ros2 pkg create ros_project --build-type ament_python --dependencies cv_bridge python3-opencv sensor_msgs geometry_msgs trajectory_msgs
COPY /src/ros_project/robot_cont.py /ros2_ws/src/ros_project/ros_project/robot_cont.py
COPY /src/ros_project/camera_subs.py /ros2_ws/src/ros_project/ros_project/camera_subs.py
COPY /src/ros_project/launch/start.launch.py /ros2_ws/ros_project/launch/start.launch.py

WORKDIR /ros2_ws
RUN colcon build

#RUN ros2  launch ros_project /src/launch.py