import sys

from interface2.srv import MultiplyTwoInts
import rclpy
from rclpy.node import Node


class MultiplyClientAsync(Node):

    def __init__(self):
        super().__init__('multiply_client_async')
        self.cli = self.create_client(MultiplyTwoInts, 'multiply_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available')
        self.req = MultiplyTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main():
    rclpy.init()
    
    multiply_client = MultiplyClientAsync()
    response = multiply_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    multiply_client.get_logger().info(
        'Result : %d * %d = %d' % (int(sys.argv[1]), int(sys.argv[2]), response.sum))
    multiply_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

