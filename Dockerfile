FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-cv-bridge \
    ros-humble-usb-cam \
    ros-rolling-ur \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install opencv-contrib-python-headless

WORKDIR /ros2_ws/src
COPY . /ros2_ws/src/robot_control_interface

WORKDIR /ros2_ws
RUN . /opt/ros/humble/setup.sh && colcon build

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [".entrypoint.sh"]

#CMD ["ros2", "launch", "robot_control_interface", "start_interface.launch.py"]