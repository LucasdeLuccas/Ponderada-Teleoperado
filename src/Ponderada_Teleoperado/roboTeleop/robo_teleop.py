import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class RoboTeleop(Node):
    def __init__(self):
        super().__init__('robo_teleop')
        self.subscription = self.create_subscription(
            String,
            'robot_command',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info('Robo Teleop Node has been started')

    def listener_callback(self, msg):
        command = msg.data
        twist = Twist()
        if command == 'w':
            twist.linear.x = 0.5
        elif command == 's':
            twist.linear.x = -0.5
        elif command == 'a':
            twist.angular.z = 0.5
        elif command == 'd':
            twist.angular.z = -0.5
        elif command == 'x':
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        self.publisher_.publish(twist)
        self.get_logger().info('Movimentação: "%s"' % command)

def main(args=None):
    rclpy.init(args=args)
    robo_teleop = RoboTeleop()
    rclpy.spin(robo_teleop)
    robo_teleop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
