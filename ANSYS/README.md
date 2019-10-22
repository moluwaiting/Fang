# ANSYS基本使用教程
---
## 例子：AUV直航运动阻力分析实例
1.打开ANSYS的Workbench 15.0,双击图中所示的Fluent,给算例定义名字（最好是英文），本例为Example。
![1](https://github.com/moluwaiting/Fang/blob/master/ANSYS/Image/1.PNG)
![2](https://github.com/moluwaiting/Fang/blob/master/ANSYS/2.PNG)

2.模型导入：
双击Geometry，然后点击File,再点击import External model(导入外部模型)。
选择之前画好的模型(.stp格式),点击确定。
稍等一会之后，点击黄色闪电标志的generate。
再稍等一会，模型生成完毕，界面中会显示出模型，再点击退出即可。
![3](https://github.com/moluwaiting/Fang/blob/master/ANSYS/3.PNG)
![4](https://github.com/moluwaiting/Fang/blob/master/ANSYS/4.PNG)

3.网格划分以及命名：
回到主界面之后，双击mesh，等待直到模型导入完毕。
单击图中所示mesh，点击下方弹出框中的sizing,然后修改划分网格的参数，可参考图中所示。
![5](https://github.com/moluwaiting/Fang/blob/master/ANSYS/5.PNG)
![6](https://github.com/moluwaiting/Fang/blob/master/ANSYS/6.PNG)
![7](https://github.com/moluwaiting/Fang/blob/master/ANSYS/7.PNG)
设置完毕之后点击Generate Mesh,等待网格划分完毕。
![8](https://github.com/moluwaiting/Fang/blob/master/ANSYS/8.PNG)
点击select mode，选择Box select(框选模式)，把机器人框选出来（框选出来的机器人为绿色，一定要保证全部框选出来，且不能框选到其他物体），然后右键机器人，选择create named slection（给机器人起名字，随意起，英文即可）。
然后再点击select mode，选择single select(点选模式)，
点击流域中的流场入口那一面，右键，设定名字为inlet,
点击流域中的流场出口那一面，右键，设定名字为outlet,
剩余的为壁面，一起选中之后，右键，设定名字为wall,
设置完毕之后，这里会出现设置的名字，然后退出界面即可。

4.求解器设置：
再主界面上，右键mesh，点击update，等待更新完毕（geometry以及mesh都是 √ 状态）。
双击setup，
