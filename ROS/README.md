# 网址导航
- [ROS中文官网](http://wiki.ros.org/cn)
- [古月居主页](http://www.guyuehome.com/)
- [基于ROS应用Tensorflow实现物体识别](https://blog.csdn.net/qq_37464350/article/details/81009695)
- [ROS学习笔记——简单的消息发布器和订阅器 (Python版)](https://blog.csdn.net/florida_tang/article/details/79601168)

# ROS命令
```shell
env | grep ros   #查看ROS相关的环境变量
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
