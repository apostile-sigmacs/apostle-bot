cmake_minimum_required(VERSION 2.8.3)
project(my_robot)

##################
## Dependencies ##
##################

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries 
find_package(catkin REQUIRED COMPONENTS
    roscpp 
    rospy 
    tf2
		tf2_ros
    nav_msgs 
    apstron_msgs 
    geometry_msgs 
    sensor_msgs 
    std_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES my_robot
  CATKIN_DEPENDS roscpp rospy tf2 tf2_ros nav_msgs apstron_msgs geometry_msgs sensor_msgs std_msgs 
  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_library(robot_base src/robot_base.cpp)
add_executable(robot_base_node src/robot_base_node.cpp)
target_link_libraries(robot_base_node robot_base ${catkin_LIBRARIES})
add_dependencies(robot_base apstron_msgs_generate_messages_cpp)


#############
## Install ##
#############

# Future work

#############
## Testing ##
#############

# Future work
