# ☕ CafeSense: Vision-Guided Autonomous Robot System 🚀

This project demonstrates a complete **perception-to-action pipeline** in robotics using ROS2, Gazebo, and YOLOv8.
A robot detects objects in real-time and reacts autonomously inside a simulated cafe environment.

---

## 🔥 Features

* 👁️ Real-time object detection using YOLOv8
* 🤖 Autonomous robot response based on visual input
* 🔄 ROS2 node-based modular architecture
* 🌍 Simulation in Gazebo (Cafe environment)
* ⚡ End-to-end perception → action pipeline
* 🔧 Custom robot (Medibot URDF with LiDAR + Camera integration)

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
Camera → YOLO Detection → ROS2 Topic → Controller → Robot Motion
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

# ▶️ Running the Project

## 🟢 Option 1: TurtleBot3 (Standard Demo)

### 1️⃣ Launch Cafe World

```bash
ros2 launch gazebo_ros gazebo.launch.py world:=/usr/share/gazebo-11/worlds/cafe.world
```

### 2️⃣ Spawn TurtleBot3

```bash
export TURTLEBOT3_MODEL=burger

ros2 run gazebo_ros spawn_entity.py \
-file /opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf \
-entity tb3
```

---

## 🔧 Option 2: Custom Medibot (Recommended)

### 1️⃣ Build Medibot Workspace

```bash
cd ~/medibot_ws
colcon build
source install/setup.bash
```

---

### 2️⃣ Launch Cafe World

```bash
ros2 launch gazebo_ros gazebo.launch.py world:=/usr/share/gazebo-11/worlds/cafe.world
```

---

### 3️⃣ Spawn Medibot

```bash
ros2 run gazebo_ros spawn_entity.py \
-file ~/medibot_ws/src/medibot_description/urdf/medibot.urdf \
-entity medibot
```

---

### 4️⃣ Verify Camera Topic

```bash
ros2 topic list | grep camera
```

Expected:

```
/camera/camera/image_raw
```

---

## 🧠 Run Perception + Control

### Vision Node (YOLO)

```bash
ros2 run vision_bot detector
```

### Control Node

```bash
ros2 run vision_bot controller
```

---

## 🎯 Expected Output

* Robot detects objects in real-time
* Publishes object position via ROS2
* Moves toward detected object

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
