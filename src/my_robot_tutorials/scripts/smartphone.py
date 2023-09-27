#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_recieve_radio_data(msg):
    rospy.loginfo("Message Received: ")
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node('smartphone')

    sub = rospy.Subscriber("/robot_news_radio", String, callback_recieve_radio_data)

    #This will keep the script right here until the rosnode smartphone is killed
    rospy.spin()

    
    