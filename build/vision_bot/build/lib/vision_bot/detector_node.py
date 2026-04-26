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

        self.bridge = CvBridge()
        self.model = YOLO("yolov8n.pt")

        self.sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.callback,
            10
        )

        self.pub = self.create_publisher(String, '/object_position', 10)

    def callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        results = self.model(frame)

        for r in results:
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box)
                cx = (x1 + x2)//2

                out = String()
                out.data = str(cx)
                self.pub.publish(out)

                cv2.circle(frame, (cx, int((y1+y2)/2)), 5, (0,255,0), -1)

        cv2.imshow("Detection", frame)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = Detector()
    rclpy.spin(node)
    rclpy.shutdown()