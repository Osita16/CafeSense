import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ultralytics import YOLO
import cv2

class Detector(Node):
    def __init__(self):
        super().__init__('detector_node')

        self.get_logger().info("🚀 Detector Node Started (Webcam Mode)")

        # Load YOLO
        try:
            self.model = YOLO("yolov8n.pt")
            self.get_logger().info("✅ YOLO model loaded")
        except Exception as e:
            self.get_logger().error(f"❌ YOLO load failed: {e}")

        # Webcam
        self.cap = cv2.VideoCapture(0)

        # Publisher
        self.pub = self.create_publisher(String, '/object_position', 10)

        # Timer instead of ROS subscription
        self.timer = self.create_timer(0.1, self.detect)

    def detect(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warn("⚠️ Camera not working")
            return

        try:
            results = self.model(frame)

            detected = False

            for r in results:
                if r.boxes is None:
                    continue

                for box in r.boxes.xyxy:
                    x1, y1, x2, y2 = map(int, box)

                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    # Publish position
                    msg = String()
                    msg.data = str(cx)
                    self.pub.publish(msg)

                    self.get_logger().info(f"📍 Object at x={cx}")

                    # Draw
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

                    detected = True

            if not detected:
                self.get_logger().info("⚠️ No object detected")

            cv2.imshow("YOLO Detection", frame)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"❌ Detection error: {e}")

def main():
    rclpy.init()
    node = Detector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.cap.release()
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()