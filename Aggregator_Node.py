#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
import random
from std_msgs.msg import Float64,String
from custom_interfaces.srv import MyData


class Aggregator_Node(Node):
    def __init__(self):
        super().__init__("Aggregator_Node")
        
        self.Temp_Sub_Data_=self.create_subscription(Float64,"Temp_Data",self.Temp_callback,10)
        self.Pressure_Sub_Data_=self.create_subscription(Float64,"Pressure_Data",self.Pressure_callback,10)
        self.Humidity_Sub_Data_=self.create_subscription(Float64,"Humidity_Data",self.Humidity_callback,10)
        # self.Temp_Sub_Status_=self.create_subscription(String,"Temp_Status",self.Temp_callback,10)
        # self.Pressure_Sub_Status_=self.create_subscription(String,"Pressure_Status",self.Pressure_callback,10)
        # self.Humidity_Sub_Status_=self.create_subscription(String,"Humidity_Status",self.Humidity_callback,10)
        self.client_=self.create_client(MyData,"Remote_Station_Service")
        self.temp=None
        self.humidity=None
        self.pressure=None
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("wait for service...")
        self.future = None    

    def Temp_callback(self,msg):
        self.temp=msg.data
        self.send_request()

    def Pressure_callback(self,msg):
        self.pressure=msg.data
        self.send_request()

    def Humidity_callback(self,msg):
        self.humidity=msg.data
        self.send_request()

    def send_request(self):
        if self.temp is None or self.humidity is None or self.pressure is None:
            return
        
        request = MyData.Request()
        request.temp = self.temp
        request.humidity = self.humidity
        request.pressure = self.pressure

        self.future=self.client_.call_async(request)


    



def main(args=None):
    rclpy.init(args=args)
    node=Aggregator_Node()
    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future and node.future.done():
            try:
                response=node.future.result()
            except Exception as e:
                node.get_logger().info(f"service call failed {e}")
            else:
                node.get_logger().info(f"result is:{response.response}")   

            node.future = None  
    node.destroy_node()
    rclpy.shutdown()

if (__name__=='__main__'):
    main()    