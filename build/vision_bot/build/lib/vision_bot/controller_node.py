import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Controller(Node):
    def __init__(self):
        super().__init__('controller_node')

        self.get_logger().info("🤖 Controller Node Started")

        self.sub = self.create_subscription(
            String,
            '/object_position',
            self.callback,
            10
        )

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def callback(self, msg):
        try:
            cx = int(msg.data)

            cmd = Twist()

            # Frame center assumption (~640 width → center ≈ 320)
            if cx < 300:
                cmd.angular.z = 0.5
                self.get_logger().info(f"⬅️ Object Left ({cx}) → Turning Left")

            elif cx > 340:
                cmd.angular.z = -0.5
                self.get_logger().info(f"➡️ Object Right ({cx}) → Turning Right")

            else:
                cmd.linear.x = 0.2
                self.get_logger().info(f"⬆️ Object Center ({cx}) → Moving Forward")

            self.pub.publish(cmd)

        except Exception as e:
            self.get_logger().error(f"❌ Error: {e}")

def main():
    rclpy.init()
    node = Controller()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()