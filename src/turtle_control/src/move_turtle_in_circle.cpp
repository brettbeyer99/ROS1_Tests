#include <ros/ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Twist.h>
#include <math.h>

int main(int argc, char **argv){
    
    ros::init(argc, argv, "move_turtle_in_circle");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

    ros::Rate rate(2);

    while (ros::ok()){
        geometry_msgs::Twist msg;
        msg.linear.x = 5;
        msg.angular.z = M_PI * 2;
        pub.publish(msg);
        rate.sleep();
    }
    
}