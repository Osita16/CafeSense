# ☕ CafeSense: Vision-Guided Autonomous Robot System 🚀

A complete **perception-to-action pipeline** built using ROS2, Gazebo, and YOLOv8.
The robot perceives its environment through a simulated camera, detects objects in real-time, and reacts autonomously inside a cafe environment.

---

## 🔥 Features

* 👁️ Real-time object detection using YOLOv8
* 🤖 Autonomous robot response based on visual input
* 🔄 ROS2 modular node architecture
* 🌍 Simulation in Gazebo (Cafe environment)
* ⚡ End-to-end perception → action pipeline

---

## ⚙️ Tech Stack

* ROS2 Humble
* Gazebo
* OpenCV
* YOLOv8 (Ultralytics)
* Python

---

## 🔄 System Pipeline

```
Gazebo Camera → YOLO Detection → ROS2 Topic → Controller → Robot Motion
```

---

## 📦 Installation

```bash
# Create workspace
mkdir -p ~/sim_ws/src
cd ~/sim_ws/src

# Clone repository
git clone https://github.com/Osita16/CafeSense.git

# Build workspace
cd ~/sim_ws
colcon build
source install/setup.bash
```

---

## ▶️ How to Run (Complete Pipeline)

### 1️⃣ Launch Gazebo Cafe World

```bash
cd ~/sim_ws
source install/setup.bash

ros2 launch gazebo_ros gazebo.launch.py world:=/usr/share/gazebo-11/worlds/cafe.world
```

---

### 2️⃣ Spawn TurtleBot3

```bash
export TURTLEBOT3_MODEL=burger

ros2 run gazebo_ros spawn_entity.py \
-file /opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf \
-entity tb3
```

---

### 3️⃣ Verify Camera Topic

```bash
ros2 topic list | grep camera
```

Expected:

```
/camera/camera/image_raw
```

(Optional visual check)

```bash
rqt_image_view
```

---

### 4️⃣ Run Vision Node (YOLO)

```bash
cd ~/sim_ws
source install/setup.bash

ros2 run vision_bot detector
```

---

### 5️⃣ Run Controller Node

```bash
ros2 run vision_bot controller
```

---

## 🎯 Expected Output

* Robot receives camera feed from Gazebo
* YOLO detects objects in real-time
* Object position is published to `/object_position`
* Robot moves based on detected object location

---

## 🎥 Demo

<img width="1058" height="942" alt="image" src="https://github.com/user-attachments/assets/ccfe0534-5ba4-4e74-90d3-4f0326f399ea" />

---

## 🚀 Future Scope

* Object-specific tracking
* Smooth motion control (PID / filtering)
* Integration with Nav2
* Deployment on real robot

---

## 🧾 Author

**Osita Bharti**
Robotics | ROS2 | Autonomous Systems

---

## ⭐ Support

If you found this useful, consider giving it a ⭐
