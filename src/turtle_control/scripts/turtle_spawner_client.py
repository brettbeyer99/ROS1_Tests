#!/usr/bin/env python3

import rospy
import random
from turtlesim.srv import Spawn

counter = 0

def rand_number():
    return random.uniform(0, 11) 

def new_name():
    global counter
    rospy.loginfo(counter)
    counter += 1
    return counter


if __name__ == '__main__':
    rospy.init_node('turtle_spwaner_client')

    rospy.wait_for_service("/spawn")

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            spawn_turtle = rospy.ServiceProxy("spawn", Spawn)
            response = spawn_turtle(rand_number(), rand_number(), 0, "Turtle_" + str(new_name()))
            rospy.loginfo("New Turtle = " + str(response.name))
        except rospy.ServiceException as e:
            rospy.logwarn("Service failed: " + str(e))

        rate.sleep()

    
    