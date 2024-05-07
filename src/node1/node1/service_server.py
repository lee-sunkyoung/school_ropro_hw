from interface2.srv import MultiplyTwoInts

import rclpy
from rclpy.node import Node


class MultiplyService(Node):

    def __init__(self):
        super().__init__('multiply_service')
        self.srv = self.create_service(MultiplyTwoInts, 'multiply_two_ints', self.multiply_two_ints_callback)

    def multiply_two_ints_callback(self, request, response):
        response.sum = request.a * request.b
        self.get_logger().info('Multiplying %d and %d' % (request.a, request.b))
        return response

def main():
    rclpy.init()
    multiply_service = MultiplyService()
    rclpy.spin(multiply_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

