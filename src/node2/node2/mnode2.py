# unified_node.py
import rclpy
from rclpy.node import Node
from topic_subscriber import TopicSubscriberNode
from service_client import ServiceClientNode
from action_client import ActionClientNode

class MNode2(Node):

    def __init__(self):
        super().__init__('m_node2')
        self.topic_subscriber = TopicSubscriberNode()
        self.service_client = ServiceClientNode()
        self.action_client = ActionClientNode()

def main(args=None):
    rclpy.init(args=args)
    m_node2 = MNode2()
    rclpy.spin(m_node2)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

