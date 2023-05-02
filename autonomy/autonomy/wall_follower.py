# GPT BOILERPLATE
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallFollowerNode(Node):
    def __init__(self):
        super().__init__('wall_follower')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # Implement your wall following algorithm here
        # Use the LaserScan data to determine the direction and speed to move
        # For simplicity, this example just stops the robot when it detects an obstacle in front of it

        twist = Twist()
        if min(msg.ranges) < 0.5:  # if there's an obstacle closer than 0.5m
            twist.linear.x = 0.0  # stop
            twist.angular.z = 0.0  # stop
        else:
            twist.linear.x = 0.2  # move forward at 0.2 m/s
            twist.angular.z = 0.0  # no rotation
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    wall_follower = WallFollowerNode()
    rclpy.spin(wall_follower)
    wall_follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()