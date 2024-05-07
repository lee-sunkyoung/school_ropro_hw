import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from custom_action_interfaces.action import UID

class UIDActionServer(Node):

    def __init__(self):
        super().__init__('UID_action_server')
        self._action_server = ActionServer(
            self,
            UID,
            'UID',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = UID.Feedback()
        feedback_msg.partial_sequence = []
        partial_sequence = [2, 0, 2, 3, 7, 4, 1, 0, 7, 1]

        for i in range(0, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                partial_sequence[i])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = UID.Result()
        result.sequence = feedback_msg.partial_sequence
        return result


def main(args=None):
    rclpy.init(args=args)

    UID_action_server = UIDActionServer()

    rclpy.spin(UID_action_server)


if __name__ == '__main__':
    main()
