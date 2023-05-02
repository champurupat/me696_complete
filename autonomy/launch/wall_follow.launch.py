from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='autonomy',
            executable='autonomy_node',
        ),
        Node(
            package='autonomy',
            executable='state_est_node',
        ),
    ])