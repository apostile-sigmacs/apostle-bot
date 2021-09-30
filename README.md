# apostle-bot
__Development computer:__<br>
__OS INSTALLATION__</br>
Download and Install Ubuntu on computer</br>
1. Download the proper **Ubuntu 18.04 LTS Desktop image** for your computer from the links below.</br>
https://releases.ubuntu.com/18.04/
3. Follow the instructions below to install Ubuntu on computer. </br>
https://ubuntu.com/tutorials/install-ubuntu-desktop#6-allocate-drive-space</br>
Install ROS 1 on development computer</br>
Open the terminal with **Ctrl+Alt+T** and enter below commands one at a time.</br>

keep the development computer updated by,</br>
$ sudo apt update</br>
$ sudo apt upgrade</br>
</br>__ROS INSTALLATION__<br>
Follow the instruction below to install ROS 1 Melodic on the computer.</br> 
	http://wiki.ros.org/melodic/Installation/Ubuntu</br>
else follow the instructions below.<br>
**step 1:** $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'<br>
**step 2:** $ sudo apt install curl<br>
**step 4:** $ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -<br>
**step 5:** $ sudo apt update<br>
**step 6:** $ sudo apt install ros-melodic-desktop-full<br>
**step 7:** $ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc<br>
**step 8:** $ source ~/.bashrc<br>
**step 9:** $ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential<br>
**step 10:** $ sudo apt install python-rosdep<br>
**step 11:** $ sudo rosdep init<br>
**step 12:** $ rosdep update<br>

**NOTE:**<br>
After successful ROS installation, here is the command to check whether ROS is working properly.<br>
$ roscore<br>

**Create a ROS Workspace**</br>
</br>
Once you have installed ROS on both computers, install Apostle packages and dependencies.</br>
On the development computer, install the packages required for configuration and visualization:</br>
$ mkdir -p ~/apostle_ws</br>
$ cd ~/apostle_ws</br>
$ git clone https://github.com/apostile-sigmacs/apostle-bot.git</br>
$ mv -f apostle-bot src
$ cd src
$./install.sh 4wd rplidar</br>

__Robot Computer:__</br>
For simple use raspberry pi with latest raspbian OS which can be found in the link below.</br>
		https://www.raspberrypi.org/software/</br>
   now its time to connect raspberry pi to WiFi network in headless mode in the following link<br>
    https://www.raspberrypi.org/documentation/computers/configuration.html<br>
	After setting up the raspberry pi with raspbian OS now, install Melodic which is described below link.</br>
	http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi</br></br>
  In the above link replace the following command in Setup ROS Repositories</br></br>
	$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654</br>
With </br>
	$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654</br>
  After completion of installation, now it's time to create a workspace for the robot on the terminal.
$mkdir -p ~/apostile_ws
$<git clone here>
$cd ~/catkin_ws
$./install.sh 4wd rplidar

Network Setup
Configure your ROS network so your development computer knows where the ROS Master(robot's computer) is within your local network. First, find out the ip-address of your robot's computer and development computer:
Connect the computer to a WiFi device and find the assigned IP address with the command below. 
$ ifconfig

Robot's computer:</br>
export ROS_MASTER_URI=http://<robot-ip>:11311</br>
export ROS_HOSTNAME=<robot-ip></br>
Development computer:</br>
export ROS_MASTER_URI=http://<robot-up>:11311</br>
export ROS_HOSTNAME=<devcom-ip></br>
You can automate this process so you don't have to re-do it every time you open a new terminal.</br>

Development computer:</br>
echo "export ROS_MASTER_URI=http://<robot-ip>:11311" >> ~/.bashrc</br>
echo "export ROS_HOSTNAME=<devcom-ip>" >> ~/.bashrc</br> 
Take note that once the ip-address of the machine has changed, you need to reconfigure your ROS_MASTER_URI and ROS_HOSTNAME again.</br>

Install the required joystick package on your machine (development computer), on the terminal.</br>
$sudo apt install ros-melodic-teleop-twist-keyboard.</br>

Now power up the controller with firmware to the raspberry pi. With the following command</br>
$roslaunch my_robot minimal.launch</br>

1. Launch teleop_twist_keyboard node from development computer for the teleoperation using a keyboard. </br>
       $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py</br>
       CTRL-C to quit</br>
          (or)</br>
$rosrun rqt_robot_steering rqt_robot_steering (on development computer)</br>
SLAM</br>
Slam approaches in ROS</br>
1) Gmapping :- ROS Wrapper</br>
2) Cartographer :- Real time simultaneous localization and mapping</br>
3) Hector-Slam :- Without odometry</br>
NOTE</br>
    • Please run the SLAM on a development computer. </br>
    • Make sure to launch the Bringup from apstronbot before executing any operation. </br>
The SLAM (Simultaneous Localization and Mapping) is a technique to draw a map by estimating current location in an arbitrary space. The SLAM is a well-known feature of apstronbot from its predecessors.
</br>
Run SLAM Node</br>
    1. If the Bringup is not running on the apstronbot SBC, launch the Bringup. Skip this step if you have launched bringup previously.</br>
       </br>
       Open a new terminal from the development computer with Ctrl + Alt + T and connect to Raspberry Pi with its IP address. The default password is ubuntu. </br>
       $ ssh pi@{IP_ADDRESS_OF_RASPBERRY_PI}</br>
       $ roslaunch apstronbot_ws bringup.launch</br>
       
    2. Open a new terminal from the development computer with Ctrl + Alt + T and launch the SLAM node. Gmapping is used as a default SLAM method. </br>
       
	$ roslaunch apstronbot slam.launch</br>

       Run Teleoperation Node</br>
Once SLAM node is successfully up and running, apstronbot will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the apstronbot, it is a good practice to scan every corner of the map.
    </br>1. Open a new terminal and run the teleoperation node from the development computer.</br>
       $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py</br>
If the node is successfully launched, the following instruction will be appeared to the terminal window. </br>
       
       Control Your Apostle robot
       Moving around
            i
        j   k   l
            ,
       i/, : increase/decrease linear velocity
       j/l : increase/decrease angular velocity
       space key, k : force stop
       CTRL-C to quit
(or)
$rosrun rqt_robot_steerig rqt_robot_steering</br>
    2. Start exploring and drawing the map.</br>
      
Visualizing the map on rviz:</br>
	$roscd my_robot/rviz</br>
	$rviz -d slam.rviz</br>

Save Map</br>
The map is drawn based on the robot’s odometry, tf and scan information. This map data is drawn in the RViz window as the apostille robot was traveling. After creating a complete map of the desired area, save the map data to the local drive for later use.
    </br>1. Launch the map_saver node in the map_server package to create map files.</br>
The map file is saved in the directory where the map_saver node is launched at.</br>
Unless a specific file name is provided, map will be used as a default file name and create map.pgm and map.yaml. </br>
       $ cd ~/apostile_ws/src/my_robot/maps</br>
       $ rosrun map_server map_saver -f <map_name></br>
The -f option specifies a folder location and a file name where files to be saved.</br>
With the above command, map.pgm and map.yaml will be saved in the home folder ~/(/home/${username}).</br>

Map</br>
The map uses a two-dimensional Occupancy Grid Map (OGM), which is commonly used in ROS. The saved map will look like the figure below, where white area is the collision free area while black area is occupied and inaccessible area, and gray area represents the unknown area. This map is used for Navigation.
</br>

Navigation</br>
WARNING: In this instruction, Apstronbot may move and rotate. Please place the robot on a safe ground.</br>
NOTE</br>
    • Please run the Navigation on the development computer. </br>
    • Make sure to launch the Bringup from Apstronbot before executing any operation. </br>
    • The Navigation uses a map created by the SLAM. Please prepare a map before running the Navigation. </br>
Navigation is to move the robot from one location to the specified destination in a given environment. For this purpose, a map that contains geometry information of furniture, objects, and walls of the given environment is required. As described in the previous SLAM section, the map was created with the distance information obtained by the sensor and the pose information of the robot itself.
The Navigation enables a robot to move from the current pose to the designated goal pose on the map by using the map, robot’s encoder, IMU sensor, and distance sensor. The procedure for performing this task is as follows.
AMCL:- It is the ROS node that responsible for estimating the location of robot in the map
Move base :- It is the ROS node that implements both Global path planner & Local path planner. It is responsible for finding the static path between robot location and goal location via Global path planner.
Run Navigation Nodes</br>
    1. If the Bringup is not running on the apstronbot SBC, launch the Bringup. Skip this step if you have launched bring up previously. </br>
        ◦ Open a new terminal from development computer with Ctrl + Alt + T and connect to Raspberry Pi with its IP address. The default password is ubuntu.</br> 
          $ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}</br>
          $ roslaunch apstronbot bringup.launch</br>

    2. Launch the Navigation.</br>
       $ roslaunch apstronbot navigation.launch
</br>
Estimate Initial Pose</br>
Initial Pose Estimation must be performed before running the Navigation as this process initializes the AMCL parameters that are critical in Navigation. Apstronbot has to be correctly located on the map with the LDS sensor data that neatly overlaps the displayed map.</br>
    1. Click the 2D Pose Estimate button in the RViz menu.</br>
    2. Click on the map where the actual robot is located and drag the large green arrow toward the direction where the robot is facing. </br>
    3. Repeat step 1 and 2 until the LDS sensor data is overlayed on the saved map. </br>
    4. Launch keyboard teleoperation node to precisely locate the robot on the map. </br>
       $ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch</br>
    5. Move the robot back and forth a bit to collect the surrounding environment information and narrow down the estimated location of the TurtleBot3 on the map which is displayed with tiny green arrows.</br>
    6. Terminate the keyboard teleoperation node by entering Ctrl + C to the teleop node terminal in order to prevent different cmd_vel values from being published from multiple nodes during Navigation.</br>
    
    Set Navigation Goal</br>
    
    1. Click the 2D Nav Goal button in the RViz menu.</br>
    2. Click on the map to set the destination of the robot and drag the green arrow toward the direction where the robot will be facing.</br> 
        ◦ This green arrow is a marker that can specify the destination of the robot. </br>
        ◦ The root of the arrow is x, y coordinate of the destination, and the angle θ is determined by the orientation of the arrow.</br> 
        ◦ As soon as x, y, θ are set, TurtleBot3 will start moving to the destination immediately. </br>

