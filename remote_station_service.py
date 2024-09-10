import rclpy
from rclpy.node import Node
from custom_interfaces.srv import MyData


class RemoteStationService(Node):
    def __init__(self):
        super().__init__("Remote_Station_Service")
        self.servive_=self.create_service(
            MyData,"Remote_Station_Service",self.callback
        )
    
    def callback(self,request,response):
        if not (10.0<=request.temp<=100.0):
            self.get_logger().info(f"The Temp:{request.temp} is out of range")
        if not (0.7<=request.humidity<=0.95):
            self.get_logger().info(f"The humidity:{request.humidity} is out of range")
        if not (0.95<=request.pressure<=1.2):
            self.get_logger().info(f"The pressure:{request.pressure} is out of range")   

        self.get_logger().info(f"the data :temp={request.temp},humidity={request.humidity},pressure={request.pressure}")  
        response.response="all the data are valid"
        
        return response     

def main(args=None):
    rclpy.init(args=args)
    node=RemoteStationService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if (__name__=='__main__'):
    main()    