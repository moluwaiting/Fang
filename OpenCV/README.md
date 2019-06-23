# 注意事项
- 安装opencv的命令:在cmake之前，需要将.bashrc文件中的Anaconda路径注释掉，才能正常编译
```shell
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_OPENMP=ON -D ENABLE_PRECOMPILED_HEADERS=OFF -D OPENCV_EXTRA_MODULES_PATH=/home/fang/soft/opencv-3.4/opencv_contrib-3.4/modules/ ..

sudo make -j10

sudo make install

sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'

sudo ldconfig  
#如果这里出现了/sbin/ldconfig.real: /usr/local/cuda-9.0/targets/x86_64-linux/lib/libcudnn.so.7 不是符号连接，执行下述命令
#sudo ln -sf /usr/local/cuda-8.0/targets/x86_64-linux/lib/libcudnn.so.4.0.7 /usr/local/cuda-8.0/targets/x86_64-linux/lib/libcudnn.so.4 

#然后进行测试
```

- [<<OpenCV3编程入门>>书本配套源代码](https://github.com/QianMo/OpenCV3-Intro-Book-Src)
- [ubuntu16.04 安装opencv IPPICV 和 face_landmark_model.dat下载不下来的问题解决](https://blog.csdn.net/CSDN330/article/details/86747867)
- [openCV下载地址](https://opencv.org/)
- [openCV_contrib下载地址](https://github.com/opencv/opencv_contrib)
