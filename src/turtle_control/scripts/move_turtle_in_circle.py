#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import math

if __name__ == '__main__':
    rospy.init_node('move_turtle_in_circle')

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    vals = range(1,6)
    counter = 0

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 5

        rospy.loginfo(vals[counter])

        msg.angular.z = math.pi *vals[counter]
        pub.publish(msg)
        rate.sleep()
        counter += 1

        if counter == 5:
            counter = 0

    rospy.loginfo("Node was stopped!")

    