FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-cv-bridge \
    ros-humble-usb-cam \
    ros-humble-ur \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install "numpy<2" opencv-contrib-python-headless

SHELL ["/bin/bash", "-c"]

WORKDIR /ros2_ws
RUN source /opt/ros/humble/setup.sh
RUN colcon build
RUN source ./install/setup.sh

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]