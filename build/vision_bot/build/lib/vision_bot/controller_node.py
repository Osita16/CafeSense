import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Controller(Node):
    def __init__(self):
        super().__init__('controller_node')

        self.sub = self.create_subscription(
            String,
            '/object_position',
            self.callback,
            10
        )

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def callback(self, msg):
        cx = int(msg.data)

        cmd = Twist()

        if cx < 300:
            cmd.angular.z = 0.5
        elif cx > 340:
            cmd.angular.z = -0.5
        else:
            cmd.linear.x = 0.2

        self.pub.publish(cmd)

def main():
    rclpy.init()
    node = Controller()
    rclpy.spin(node)
    rclpy.shutdown()