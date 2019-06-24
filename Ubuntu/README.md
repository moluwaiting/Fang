# Ubuntu系统安装教程
- 1.磁盘分区：我的电脑->管理->磁盘管理，进行磁盘分区，200G以上，分出来的是黑色区域。
- 2.[制作U盘启动项](https://blog.csdn.net/yaoyut/article/details/78003061)：下载[ubuntu-16.04.5-desktop-amd64.iso](https://blog.51cto.com/13669226/2145171)文件，利用[UltraISO](https://www.baidu.com/link?url=CgjOghuhQnzMD7pHeymjaGmvXzI4dW5OOgNebyTk-jXmOh4HJUDb6ohHt7HP4Q_pv7iqLD9mDv7IiTAho0anF_&wd=&eqid=ce6f84f400000b3d000000065d01febd)制作U盘启动盘，
- 3.重启电脑，按F2(华硕电脑)进入Bios界面，选择启动项为u盘启动，然后按F10保存。
- 4.开始安装，自定义磁盘分区，设置：/boot 8000M ,swap 2000M,/ 25000M,/home（最大）,其余所有的空间。下面的引导选项选择boot那个分区。
- 5.重启之后在系统选择界面，按e，然后找到quit splash，改为，splash acpi_osi=Linux nomodeset,按F10保存
- 6.如果成功进入系统，且显示正常，则在终端输入 sudo gedit /boot/grub/grub.cfg  ,找到刚刚那个位置，加上同样的代码即可。如果进入系统之后显示分辨率不正常，则在附加驱动中选择显卡驱动，然后重启即可。



# Ubuntu系统常用命令
```shell
sudo apt-get update
sudo apt-get install <软件名>

切换bash:  chsh -s /bin/bash
切换zsh:   chsh -s /bin/zsh

#给文件夹创建快捷方式
# ln -s [绝对路径] ~/桌面/快捷方式名称
ln -s /data/long.com/ ~/桌面/long

#环境变量配置文件
sudo gedit .bashrc
source .bashrc

#开机出现 检测到系统程序出现问题
sudo apt install gksu
gksu gedit /etc/default/apport
将 enabled = 1 修改为 enabled = 0

激活tensorflow环境之后，导入cv2相关的包时候，会出现ImportError: /opt/ros/kinetic/lib/python2.7/dist-packages/cv2.so: undefined symbol: PyCObject_Type
这是因为安装了ROS，受到了ROS的影响，可以才去的解决办法有：
一：
source activate tensorflow
python3  #这时候进入了python的环境，使用python ***.py就无效了
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')  #把ROS写入path中的路径给清除
import cv2  #这时候正常导入cv2库
二：
把.bashrc文件中的ROS的路径注释掉,运行完毕之后再取消注释。
```
# 网址导航
- [Ubuntu完全教程，让你成为Ubuntu高手！](https://blog.csdn.net/qq_19998189/article/details/78566486)
- [Linux 命令大全](https://www.runoob.com/linux/linux-command-manual.html)
- [Ubuntu16.04安装ROS（机器人操作系统）教程](https://blog.csdn.net/m0_38087936/article/details/81484889)
- [Thinkpad E470C(集成网卡rlt8111/8618/8411系列) 无线网卡rtl8821CE系列 安装ubuntu 和win10双系统没有无线网问题](https://blog.csdn.net/fljhm/article/details/79281655)
- [ubuntu下的PCL安装过程](https://blog.csdn.net/mush_room/article/details/78339578)
- [Ubuntu16.04安装WPS并解决系统缺失字体问题](https://blog.csdn.net/u012177641/article/details/78547351)
- [Ubuntu16.04.3 下安装Qt5.9.1 OpenCV3.2.0 (包括OpenCV_contrib)完美版](https://blog.csdn.net/Chang_Shuang/article/details/78239660)
- [清华大学开源软件镜像](https://mirrors.tuna.tsinghua.edu.cn/)
- [opencv/opencv_contrib-Github](https://github.com/opencv/opencv_contrib/releases)
- [Ubuntu 解决E: 无法获得锁 /var/lib/dpkg/lock - open (11: 资源暂时不可用)](https://blog.csdn.net/demonliuhui/article/details/77488296)
- [Ubuntu16.04中 VTK8.1.1 安装](https://blog.csdn.net/dell5200/article/details/81142951?utm_source=blogxgwz8)
- [Ubuntu WallpapersCraft](https://wallpaperscraft.com/tag/ubuntu/1920x1080)
- [ubuntu下网易云音乐无法打开](https://blog.csdn.net/Handoking/article/details/81026651)
- [ubuntu16.04网易云音乐下载](https://github.com/ljb233/netease-cloud-music_ubuntu)
- [更新linux时候提示无法“由于没有公钥，无法验证下列签名 ”的解决方案](https://blog.csdn.net/loovejava/article/details/21837935)
- [ubuntu16.04下安装CUDA，cuDNN及tensorflow-gpu版本过程](https://blog.csdn.net/u014595019/article/details/53732015)
- [Ubuntu16.04安装显卡驱动、Anaconda、TensorFlow-GPU教程](https://www.jianshu.com/p/38f4a1944242)
- [CMake实践](https://blog.csdn.net/xyz599/article/details/53606149)
- [ubuntu实时显示网速cpu占用和内存占用率](https://www.cnblogs.com/hjw1/p/7901048.html)
