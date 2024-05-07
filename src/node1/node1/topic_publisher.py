import rclpy
from rclpy.node import Node
from std_msgs.msg import String

param = 2023741071  # Define the parameter value

class UniversityIDPublisher(Node):

    def __init__(self):
        super().__init__('university_id_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publish_id)
        self.uid = param

    def publish_id(self):
        msg = String()
        msg.data = 'UID : %d' % self.uid
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing University ID: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    
    university_id_publisher = UniversityIDPublisher()
    
    rclpy.spin(university_id_publisher)
    
    university_id_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
