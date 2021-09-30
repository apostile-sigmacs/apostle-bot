#!/usr/bin/env bash

set -e

source /opt/ros/$(dir /opt/ros)/setup.bash


ROSDISTRO="$(rosversion -d)"
BASE=$1
SENSOR=$2
ARCH="$(uname -m)"
echo $ARCH

if [ "$3" != "test" ]
    then
        if [ "$*" == "" ]
            then
                echo "No arguments provided"
                echo
                echo "Example: $ ./install.sh 2wd xv11"
                echo
                exit 1
                
        elif [[ "$1" != "2wd" && "$1" != "4wd" && "$1" != "mecanum" && "$1" != "ackermann" ]]
            then
                echo "Invalid robot base: $1"
                echo
                echo "Valid Options:"
                echo "2wd"
                echo "4wd"
                echo "ackermann"
                echo "mecanum"
                echo
                exit 1

        elif [[ "$2" != "xv11" && "$2" != "rplidar" && "$2" != "ydlidar" && "$2" != "hokuyo" && "$2" != "kinect" && "$2" != "realsense" ]]
            then
                echo "Invalid robot sensor: $2"
                echo
                echo "Valid Options:"
                echo "hokuyo"
                echo "kinect"
                echo "lms1xx"
                echo "realsense"
                echo "rplidar"
                echo "xv11"
                echo "ydlidar"
                echo
                exit 1
        
        elif [[ "$ARCH" != "x86_64" && "$2" == "realsense" ]]
            then
                echo "Intel Realsense R200 is not supported in $ARCH architecture."
                exit 1

        fi

        echo
        echo -n "You are installing ROS-$ROSDISTRO Linorobot for $BASE base with a $SENSOR sensor. Enter [y] to continue. " 
        read reply
        if [[ "$reply" != "y" && "$reply" != "Y" ]]
            then
                echo "Wrong input. Exiting now"
                exit 1
        fi
fi

echo
echo "INSTALLING NOW...."
echo

sudo apt-get update
sudo apt-get install -y \
avahi-daemon \
openssh-server \
python-setuptools \
python-dev \
build-essential

sudo apt-get install python-pip

source /opt/ros/$ROSDISTRO/setup.bash


sudo apt-get install -y \
ros-$ROSDISTRO-roslint \
ros-$ROSDISTRO-rosserial \
ros-$ROSDISTRO-rosserial-arduino \
ros-$ROSDISTRO-imu-filter-madgwick \
ros-$ROSDISTRO-navigation \
ros-$ROSDISTRO-robot-localization \
ros-$ROSDISTRO-tf2 \
ros-$ROSDISTRO-tf2-ros \
ros-$ROSDISTRO-usb-cam \
ros-$ROSDISTRO-slam-gmapping \
ros-$ROSDISTRO-rosbridge-suite \
ros-$ROSDISTRO-rosbridge-server \
ros-$ROSDISTRO-map-server \
ros-$ROSDISTRO-compressed-image-transport \
ros-$ROSDISTRO-camera-info-manager

sudo apt-get install -y ros-$ROSDISTRO-rplidar-ros

sudo apt install python-gobject
sudo apt install libtool-bin
sudo apt install python-gobject-2-dev
sudo apt install autoconf
sudo apt-get install libgudev-1.0-dev

cd $HOME/apostle_ws
catkin_make

echo "source $HOME/apostle_ws/devel/setup.bash" >> $HOME/.bashrc
echo "export ROBOTLIDAR=$SENSOR" >> $HOME/.bashrc
echo "export ROBOTBASE=$BASE" >> $HOME/.bashrc
source $HOME/.bashrc



echo
echo "INSTALLATION DONE!"
echo
