#!/usr/bin/env python
"""
Script to move Turtlesim in a circle
"""
import rospy
from geometry_msgs.msg import Twist

speed = 0.0
theta = 0.0
time_sammple = 0
def move_circle():

    rospy.init_node('robot_cleaner', anonymous=True)
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    global speed
    global theta
    global time_sammple
    move_cmd.linear.x = speed
    move_cmd.angular.z = theta
    #move_cmd.angular.z = 0.0
    
    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(10)
    
    # For the next 6 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(time_sammple):
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    while True:
        try:
            time_sammple=5
            speed = abs(0.2)
            theta = abs(0.0)
            move_circle()
            
            time_sammple=16
            speed = abs(0.0)
            theta = abs(0.4)
            move_circle()
            
            time_sammple=16
            speed = abs(0.0)
            theta = -abs(0.4)
            move_circle()
        
            time_sammple=5
            speed = -abs(0.2)
            theta = abs(0.0)
            move_circle()
        
            time_sammple=16
            speed = abs(0.0)
            theta = abs(0.4)
            move_circle()

            time_sammple=16
            speed = abs(0.0)
            theta = -abs(0.4)
            move_circle()
        except rospy.ROSInterruptException:
            exit()