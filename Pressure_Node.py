#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
import random
from std_msgs.msg import Float64,String

class Pressure_Node(Node):
    def __init__(self):
        super().__init__("Pressure_Node")
        self.Pressure_publisher_Data_=self.create_publisher(
            Float64,"Pressure_Data",10)
        self.Pressure_publisher_Status_=self.create_publisher(
            String,"Pressure_Status",10
        )
        self.timer=self.create_timer(0.5,self.callback)
    
    def callback(self):
        pressure_data_msg=Float64()
        pressure_data_msg.data=random.uniform(0.95,1.2)
        self.Pressure_publisher_Data_.publish(pressure_data_msg)

        pressure_stat_msg=String()
        pressure_stat_msg.data="correct"
        self.Pressure_publisher_Status_.publish(pressure_stat_msg)

        self.get_logger().info(f"From temp node the temp is:{pressure_data_msg.data} and the status is:{pressure_stat_msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node=Pressure_Node()
    rclpy.spin(node)
    rclpy.shutdown()

if (__name__=='__main__'):
    main()    
