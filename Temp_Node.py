#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
import random
from std_msgs.msg import Float64,String

class Temp_Node(Node):
    def __init__(self):
        super().__init__("Temp_Node")
        self.Temp_publisher_Data_=self.create_publisher(
            Float64,"Temp_Data",10)
        self.Temp_publisher_Status_=self.create_publisher(
            String,"Temp_Status",10
        )
        self.timer=self.create_timer(0.5,self.callback)
    
    def callback(self):
        temp_data_msg=Float64()
        temp_data_msg.data=random.uniform(10,100)
        self.Temp_publisher_Data_.publish(temp_data_msg)

        temp_stat_msg=String()
        temp_stat_msg.data="correct"
        self.Temp_publisher_Status_.publish(temp_stat_msg)

        self.get_logger().info(f"From temp node the temp is:{temp_data_msg.data} and the status is:{temp_stat_msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node=Temp_Node()
    rclpy.spin(node)
    rclpy.shutdown()

if (__name__=='__main__'):
    main()    
