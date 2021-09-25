#include "robot_pid/robot_pid_core.h"

RobotPID::RobotPID()
{
}

RobotPID::~RobotPID()
{
}

void RobotPID::publishMessage(ros::Publisher *pub_message)
{
  apstron_msgs::PID msg;
  msg.p = p_;
  msg.d = d_;
  msg.i = i_;
  pub_message->publish(msg);
}

void RobotPID::messageCallback(const apstron_msgs::PID::ConstPtr &msg)
{
  p_ = msg->p;
  d_ = msg->d;
  i_ = msg->i;

  //echo P,I,D
  ROS_INFO("P: %f", p_);
  ROS_INFO("D: %f", d_);
  ROS_INFO("I: %f", i_);
}

void RobotPID::configCallback(robot_pid::robotPIDConfig &config, double level)
{
  //for PID GUI
  p_ = config.p;
  d_ = config.d;
  i_ = config.i;

}
