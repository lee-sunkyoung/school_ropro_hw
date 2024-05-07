from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='node1',
            executable='publisher',
            name='publisher'
        ),
	Node(
            package='node1',
            executable='service',
            name='service'
        ),
        Node(
            package='node1',
            executable='action_server',
            name='action_server'
        ),
        Node(
            package='node2',
            executable='subscriber',
            name='subscriber'
        ),
        Node(
            package='node2',
            executable='client',
            name='client'
        ),
        Node(
            package='node2',
            executable='action_client',
            name='action_client'
        ),
    ])

