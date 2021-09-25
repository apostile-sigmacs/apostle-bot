#ifndef SR_ROBOT_PID_CORE_H
#define SR_ROBOT_PID_CORE_H

#include "ros/ros.h"
#include "ros/time.h"

// Custom message includes. Auto-generated from msg/ directory.
#include <apstron_msgs/PID.h>

// Dynamic reconfigure includes.
#include <dynamic_reconfigure/server.h>
// Auto-generated from cfg/ directory.
#include <robot_pid/robotPIDConfig.h>

class RobotPID
{
public:
  RobotPID();
  ~RobotPID();
  void configCallback(robot_pid::robotPIDConfig &config, double level);
  void publishMessage(ros::Publisher *pub_message);
  void messageCallback(const apstron_msgs::PID::ConstPtr &msg);

  double p_;
  double d_;
  double i_;

};
#endif
