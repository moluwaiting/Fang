# 网址导航
- [ROS中文官网](http://wiki.ros.org/cn)
- [古月居主页](http://www.guyuehome.com/)
- [基于ROS应用Tensorflow实现物体识别](https://blog.csdn.net/qq_37464350/article/details/81009695)
- [ROS学习笔记——简单的消息发布器和订阅器 (Python版)](https://blog.csdn.net/florida_tang/article/details/79601168)
- [Ros与Tensorflow的整合](https://blog.csdn.net/xuanlvxin/article/details/80325736)
- [ROS_Tensorflow_Github](https://github.com/cong/ros_tensorflow)
- [维航机器人ROS教程](http://www.wh-robot.com/whb/?page_id=70)

# ROS命令
```shell
env | grep ros   #查看ROS相关的环境变量
```

# ROS中的分布式通信
---
```shell
ifconfig 查看各个主机IP地址
sudo gedit /etc/hosts 将对方的IP添加到hosts文件中，修改完的hosts文件如下所示；
```


```seq
127.0.0.1	localhost
127.0.1.1	fang-TUF-GAMING-FX504GE-FX80GE

127.0.0.1 	rasberrypi

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
192.30.253.113 github.com
151.101.25.194 github.global.ssl.fastly.net
192.30.253.121 codeload.github.com
```

```shell
ping rasberrypi  所有主机的hosts文件都修改之后，通过ping命令来测试是否连得上
export ROS_MASTER_URI=http://fang-TUF-GAMING-FX504GE-FX80GE:11311/  在树莓派的.bashrc文件中添加这一行，设置主ROS_MASTER_URI,因为只有一个ROS_MASTER
```
# ROS通信编程
-----
## ROS话题编程
```shell
catkin_create_pkg fang std_msgs roscpp rospy  在src文件夹下创建功能包
```

# ROS学习笔记
---
- 基本工作空间的创建
```shell
1.创建工作空间
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace

2.编译工作空间
cd ~/catkin_ws
catkin_make

3.设置环境变量
sudo gedit .bashrc
在.bashrc文件中加入下列命令行：
source ~/catkin_ws/devel/setup.bash
保存退出
source .bashrc #让配置在终端中生效

4.检查环境变量
echo $ROS_PACKAGE_PATH #这时候显示两个路径，说明上一步路径已经添加

5.创建功能包
cd ~/catkin_ws/src
catkin_create_pkg test std_msgs rospy roscpp

6.编译功能包
cd ~/catkin_ws
catkin_make
```
---
- ROS通信编程 1
  - 在src中创建好功能包之后，将代码建立到功能包的src文件夹中；
  - 然后开始编译自己的C++代码（python为脚本语言，不需要编译），打开CMakeLists.txt
  ```shell
  在CMakeLists中添加以下两句话
  add_executable(talker src/talker.cpp)
  target_link_libraries(talker ${catkin_LIBRARIES})
  add_executable(listener src/listener.cpp)
  target_link_libraries(listener ${catkin_LIBRARIES})
  ```
  - 然后在工作空间中执行,catkin_make
  ```shell
  roscore
  rosrun test talker
  rosrun test listener
  ```
 - ROS通信编程 2 （[用Python实现上述功能](https://www.cnblogs.com/sea-stream/p/10246046.html)）
 ---
 
 
 # ROS小知识点
---
- 运行usb_cam节点的时候，可以在launch文件中修改需要读取的摄像头端口号/dev/video1
- 运行 rosrun image_view video_recorder image:=/usb_cam/image_raw 可以保存摄像头录制的视频
 
 
 
