# Vectornav ROS2 Driver

A ROS2 node for VectorNav INS / GNSS devices. 

This package that provides both raw and sensor_msg interfaces for the VN100, 200, & 300 devices. 
It has been entirely redesigned from the ROS1 package to provide a good basis to build into applications
without requiring modification of the node itself. The majority of the device configuration settings are 
exposed as ROS2 parameters that can be modified from a launch file. 

I added a subscriber to the code, which reads the ntrip_client topic,
and also add a "send" function from the vectornav functions,
which forwards the rtcm messages to the sensor for proper rtk correction.


## Install dependencies

### Install mavros:

```
sudo apt-get install ros-<rosdistro>-mavros ros-<rosdistro>-mavros-extras
```

### Install ntrip_client:

```
mkdir ros2_ws/src -p && cd ros2_ws/src
git clone https://github.com/LORD-MicroStrain/ntrip_client.git -b ros2
```

### Install nmea_msgs:

```
cd ros2_ws/src
git clone https://github.com/ros-drivers/nmea_msgs.git -b ros2
```

### Install rtcm_msgs:

```
cd ros2_ws/src
git clone https://github.com/tilk/rtcm_msgs.git
```

### Install vectornavDriver:

```  
cd ros2_ws/src
git clone https://github.com/Symi1995/vectornavDriver.git -b ros2
cd ..
rosdep install --from-paths src --ignore-src -r -y
```  


## Build:

```
cd ros2_ws
colcon build
```

## Quick start:

```
source ros2_ws/install/steup.bash
ros2 launch ntrip_client ntrip_client_launch.py 
ros2 launch vectornav vectornav.launch.py  
```
Before runing the driver, you have to grant permission to the `/dev/ttyUSB0` port with `sudo chmod`.


## vectornav node:

This node provides a ROS2 interface for a vectornav device. It can be configured
via ROS parameters and publishes sensor data via custom ROS topics as close to raw as possible.


## vn_sensor_msgs node:

This node will convert the custom raw data topics into ROS2 sensor_msgs topics to make it easier 
to integrate with other ROS2 packages. 

## ntrip_client:

This package use two more package: `nmea_msgs` and `rtcm_msgs`. You have to install them and write the correct rtcm client parameters: `usr`, `pass`, `broadcast address`, `port` and `mount point` to the launch params or ntrip_ros.py.

## Comment:

This driver work succesfully only the ros2 humble.
If you want use it on older version like foxy, than you must copy two file from humble workspace. So copy `tf2_geometry_msgs.hpp` to `/ opt/ros/foxy/include/tf2_geometry_msgs` and `tf2_sensor_msgs.hpp` to `/opt/ros/foxy/include/tf2_sensor_msgs`. Furthermore the `broadcaster.cpp` is not work correctly in ros2 foxy you have to remove it from CMakeLists.txt or you have to rewrite it to ros2 foxy format. The [ROS2 Foxy documentation](https://docs.ros.org/en/foxy/Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Cpp.html#) will help you do that.


## References:

[1] [VectorNav](http://www.vectornav.com/)  
[2] [Dereck Wonnacott - dawonn](https://github.com/dawonn/vectornav/tree/ros2)