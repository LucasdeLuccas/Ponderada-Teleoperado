import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class UserInterface(Node):
    def __init__(self):
        super().__init__('user_interface')
        self.publisher_ = self.create_publisher(String, 'robot_command', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('User Interface Node has been started')

    def timer_callback(self):
        command = input("Digite o comando para o robô (w, a, s, d, x para parar): ")
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info('Comando enviado: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    user_interface = UserInterface()
    rclpy.spin(user_interface)
    user_interface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
