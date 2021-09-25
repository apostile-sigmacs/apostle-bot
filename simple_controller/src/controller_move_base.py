#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal

p_x = 0.0
p_y = 0.0
p_z = 0.0

o_x = 0.0
o_y = 0.0
o_z = 0.0
o_w = 0.0


def movebase_client():
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    global p_x
    global p_y
    global p_z

    global o_x
    global o_y
    global o_z
    global o_w

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = p_x
    goal.target_pose.pose.position.y = p_y
    goal.target_pose.pose.position.z = p_z

    goal.target_pose.pose.orientation.x = o_x
    goal.target_pose.pose.orientation.y = o_y
    goal.target_pose.pose.orientation.z = o_z
    goal.target_pose.pose.orientation.w = o_w

    client.send_goal(goal)

    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    
    count = 1
    while True:
        #loop for inf times       
        try:

            if count == 1:
                print("set to point1")
                p_x = 1.43215632439
                p_y = 0.285309791565
                p_z = 0.0

                o_x = 0.0
                o_y = 0.0
                o_z = 0.0673175824099
                o_w = 0.997731598727
                rospy.sleep(1)

            elif count == 2:
                print("set to point2")
                p_x = 3.49022698402
                p_y = 2.63572454453
                p_z = 0.0

                o_x = 0.0
                o_y = 0.0
                o_z = 0.71556871048
                o_w = 0.698542354179
                rospy.sleep(1)

            elif count == 3:
                print("set to point3")
                p_x = 3.53322553635
                p_y = 7.78741121292
                p_z = 0.0

                o_x = 0.0
                o_y = 0.0
                o_z = -0.728272148254
                o_w = 0.685288025634

                rospy.sleep(1)

            rospy.init_node("movebase_client_py")
            result = movebase_client()
            if result:
                rospy.loginfo("Goal execution done!")
                count = count+1
            if count > 3:
                count = 1
        except rospy.ROSInterruptException:
            rospy.loginfo("Navigation test finished")