#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
import random
from std_msgs.msg import Float64,String

class Humidity_Node(Node):
    def __init__(self):
        super().__init__("Humidity_Node")
        self.Humidity_publisher_Data_=self.create_publisher(
            Float64,"Humidity_Data",10)
        self.Humidity_publisher_Status_=self.create_publisher(
            String,"Humidity_Status",10
        )
        self.timer=self.create_timer(0.5,self.callback)
    
    def callback(self):
        humidity_data_msg=Float64()
        humidity_data_msg.data=random.uniform(0.7,0.95)
        self.Humidity_publisher_Data_.publish(humidity_data_msg)

        humidity_stat_msg=String()
        humidity_stat_msg.data="correct"
        self.Humidity_publisher_Status_.publish(humidity_stat_msg)

        self.get_logger().info(f"From temp node the temp is:{humidity_data_msg.data} and the status is:{humidity_stat_msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node=Humidity_Node()
    rclpy.spin(node)
    rclpy.shutdown()

if (__name__=='__main__'):
    main()    
