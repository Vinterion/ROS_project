FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-cv-bridge \
    ros-humble-usb-cam \
    ros-rolling-ur \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install opencv-contrib-python-headless

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

#CMD ["ros2", "launch", "robot_control_interface", "start_interface.launch.py"]