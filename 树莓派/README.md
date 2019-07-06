# 树莓派总结
----
- 树莓派刷机教程
  - 1.从[网盘链接](https://pan.baidu.com/s/1ge6TNtL)下载**2019-04-08-raspbian-stretch-full.img**系统镜像文件;
  - 2.然后从[网盘链接](https://pan.baidu.com/s/1qXRArUW)下载**Win32 Disk Imager**;
  - 3.对TF卡进行格式化，需要保证写入之前，整个Tf卡只有一个***空的活动分区***，可以利用软件**diskGenius**进行Tf卡的格式化，以及分区调节;
  - 4.利用Win32 Disk Imager软件将系统镜像文件写入到TF卡中，大概十分钟左右
  - 5.然后进入系统，安装teamviwer 14，[**安装QT5+OPENCV-2.4.9(树莓派只能安装opencv2.4.9)**](https://blog.csdn.net/sha1996118/article/details/75622692)
  - 6. 创建release folder,then execute 
  ```shell
  cmake -D CMAKE_BUILD_TYPE=RELEASE -DENABLE_PRECOMPILED_HEADERS=OFF -D WITH_FFMPEG=OFF -D CMAKE_INSTALL_PREFIX=/usr/local ..
  ```
