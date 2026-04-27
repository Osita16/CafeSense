import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2

class Detector(Node):
    def __init__(self):
        super().__init__('detector_node')

        self.get_logger().info("🚀 Detector Node Started")

        self.bridge = CvBridge()

        # Load YOLO model
        try:
            self.model = YOLO("yolov8n.pt")
            self.get_logger().info("✅ YOLO model loaded")
        except Exception as e:
            self.get_logger().error(f"❌ YOLO load failed: {e}")

        # Subscriber
        self.sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.callback,
            10
        )

        # Publisher
        self.pub = self.create_publisher(String, '/object_position', 10)

    def callback(self, msg):
        self.get_logger().info("📸 Image received")

        try:
            # Convert ROS image → OpenCV
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Run YOLO
            results = self.model(frame, stream=True)

            detected = False

            for r in results:
                if r.boxes is None:
                    continue

                for box in r.boxes.xyxy:
                    x1, y1, x2, y2 = map(int, box)

                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    # Publish center x
                    out = String()
                    out.data = str(cx)
                    self.pub.publish(out)

                    self.get_logger().info(f"📍 Object at x={cx}")

                    # Draw point
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

                    detected = True

            if not detected:
                self.get_logger().info("⚠️ No object detected")

            # Show window
            cv2.imshow("YOLO Detection", frame)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"❌ Error in callback: {e}")

def main():
    rclpy.init()
    node = Detector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()