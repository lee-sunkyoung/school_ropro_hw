import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class UniversityIDSubscriber(Node):
    def __init__(self):
        super().__init__('university_id_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received University ID: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    university_id_subscriber = UniversityIDSubscriber()
    rclpy.spin(university_id_subscriber)
    university_id_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

