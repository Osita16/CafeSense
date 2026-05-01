# ☕ CafeSense: Vision-Guided Autonomous Robot System 🚀

This project demonstrates a complete **perception-to-action pipeline** in robotics using ROS2, Gazebo, and YOLOv8.
A custom robot (**Medibot**) detects objects in real-time and reacts autonomously inside a simulated cafe environment.

---

## 🔥 Features

* 👁️ Real-time object detection using YOLOv8
* 🤖 Autonomous robot response based on visual input
* 🧠 Custom robot (**Medibot**) with camera + LiDAR integration
* 🔄 ROS2 node-based modular architecture
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

## ▶️ How to Run

### 1️⃣ Launch Gazebo Cafe World

```bash
ros2 launch gazebo_ros gazebo.launch.py world:=/usr/share/gazebo-11/worlds/cafe.world
```

---

### 2️⃣ Spawn Custom Robot (Medibot)

```bash
ros2 run gazebo_ros spawn_entity.py \
-file ~/medibot_ws/src/medibot_description/urdf/medibot.urdf \
-entity medibot
```

---

### 3️⃣ Run Vision Node (YOLO Detection)

```bash
ros2 run vision_bot detector_node
```

---

### 4️⃣ Run Controller Node

```bash
ros2 run vision_bot controller_node
```

---

## 🎯 Expected Output

* Robot receives camera feed from Gazebo
* Detects objects using YOLOv8
* Publishes object position to ROS2 topic
* Moves autonomously based on detected object location

---

## 🎥 Demo

<img width="1058" height="942" alt="image" src="https://github.com/user-attachments/assets/ccfe0534-5ba4-4e74-90d3-4f0326f399ea" />

---

## 🧠 System Highlights

* Custom URDF-based robot design (Medibot)
* Sensor integration (camera + LiDAR)
* Real-time perception-to-action loop
* ROS2 topic-based communication architecture

---

## 🚀 Future Scope

* Object-specific tracking (class filtering)
* Smooth motion control (PID / proportional control)
* Integration with Nav2 for autonomous navigation
* Deployment on real robot hardware

---

## 🧾 Author

**Osita Bharti**
Robotics | ROS2 | Autonomous Systems

---

## ⭐ Support

If you found this useful, consider giving it a ⭐
