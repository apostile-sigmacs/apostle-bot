#include "robot_base.h"

int main(int argc, char** argv )
{
    ros::init(argc, argv, "robot_base_node");
    RobotBase robot;
    ros::spin();
    return 0;
}