# ANSYS基本使用教程
---
## 例子：AUV直航运动阻力分析实例
### 1.打开软件：
> * 打开ANSYS的Workbench 15.0,双击图中所示的Fluent,给算例定义名字（最好是英文），本例为Example。
![1](https://github.com/moluwaiting/Fang/blob/master/ANSYS/Image/1.PNG)
![2](https://github.com/moluwaiting/Fang/blob/master/ANSYS/2.PNG)

### 2.模型导入：
> * 双击Geometry，然后点击File,再点击import External model(导入外部模型)。
> * 选择之前画好的模型(.stp格式),点击确定。
> * 稍等一会之后，点击黄色闪电标志的generate。
> * 再稍等一会，模型生成完毕，界面中会显示出模型，再点击退出即可。
![3](https://github.com/moluwaiting/Fang/blob/master/ANSYS/3.PNG)
![4](https://github.com/moluwaiting/Fang/blob/master/ANSYS/4.PNG)

### 3.网格划分以及命名：
> * 回到主界面之后，双击mesh，等待直到模型导入完毕。
> * 单击图中所示mesh，点击下方弹出框中的sizing,然后修改划分网格的参数，可参考图中所示。
![5](https://github.com/moluwaiting/Fang/blob/master/ANSYS/5.PNG)
![6](https://github.com/moluwaiting/Fang/blob/master/ANSYS/6.PNG)
![7](https://github.com/moluwaiting/Fang/blob/master/ANSYS/7.PNG)
> * 设置完毕之后点击Generate Mesh,等待网格划分完毕。
![8](https://github.com/moluwaiting/Fang/blob/master/ANSYS/8.PNG)
> * 点击select mode，选择Box select(框选模式)，把机器人框选出来（框选出来的机器人为绿色，一定要保证全部框选出来，且不能框选到其他物体），然后右键机器人，选择create named slection（给机器人起名字，随意起，英文即可）。
> * 然后再点击select mode，选择single select(点选模式)，
> * 点击流域中的流场入口那一面，右键，设定名字为inlet,
> * 点击流域中的流场出口那一面，右键，设定名字为outlet,
> * 剩余的为壁面，一起选中之后，右键，设定名字为wall,
> * 设置完毕之后，这里会出现设置的名字，然后退出界面即可。

### 4.求解器设置：
> * 再主界面上，右键mesh，点击update，等待更新完毕（geometry以及mesh都是 √ 状态）。
> * 双击setup,弹出的界面如图所示，选择双精度，并行计算等，然后进入求解器主界面。
![9](https://github.com/moluwaiting/Fang/blob/master/ANSYS/9.png)
> * 1.General：如图所示，选择压力基方法进行求解。
![10](https://github.com/moluwaiting/Fang/blob/master/ANSYS/12.png)
> * 2.Model:如图所示，选择湍流模型为RNG K-epsilon。
![11](https://github.com/moluwaiting/Fang/blob/master/ANSYS/11.png)
> * 3.Material：点击Create/Edit 
![12](https://github.com/moluwaiting/Fang/blob/master/ANSYS/13.png)
> * 然后点击 Fluent Database，下拉材料栏，选择water-liquid( h2o<l> ),点击copy，退出。
![13](https://github.com/moluwaiting/Fang/blob/master/ANSYS/14.png)
> * 4.Cell Zone condition：点击edit，材料名称中选择上一步的water-liquid( h2o<l> )
![14](https://github.com/moluwaiting/Fang/blob/master/ANSYS/15.png)
> * 5.Boundary condition：点击inlet->edit，设定速度。
![15](https://github.com/moluwaiting/Fang/blob/master/ANSYS/16.png)
> * 6.Boundary condition：点击wall->edit，壁面条件选择为Moving Wall（可滑移壁面），速度方向设置为水流速度方向一致。
![16](https://github.com/moluwaiting/Fang/blob/master/ANSYS/17.png)
> * 7.Solution Method：求解方法，选择SIMPLE方法，然后湍流动能以及湍流能量耗散率均设置为二阶迎风，精度更高。
![17](https://github.com/moluwaiting/Fang/blob/master/ANSYS/18.png)
> * 8.Monitor：双击残差设置，精度设置为0.00001。
![18](https://github.com/moluwaiting/Fang/blob/master/ANSYS/19.png)
> * 9.Monitor:点击create，选择阻力，升力或者力矩，然后进入勾选图示两项，点击AUV，确定。此设置可以在求解的过程中监视计算时的力以及力矩变化。
![19](https://github.com/moluwaiting/Fang/blob/master/ANSYS/20.png)
![20](https://github.com/moluwaiting/Fang/blob/master/ANSYS/21.png)
> * 10.Solution Initialization：勾选Standard Initialization，然后点击Initialize
![21](https://github.com/moluwaiting/Fang/blob/master/ANSYS/22.png)
> * 11.Calculation Activities：设置每迭代50步保存结果一次。
![22](https://github.com/moluwaiting/Fang/blob/master/ANSYS/23.png)
> * 12.Run Calculation:迭代次数设置为250次，然后点击run开始进行计算，等待计算完毕。
![23](https://github.com/moluwaiting/Fang/blob/master/ANSYS/24.png)
> * 13.Reports：计算完毕之后，点击reports，可以输出计算的一些结果，例如双击Forces，然后选择受力的类型，受力的方向，点击AUV，最后点击print，便可以在信息栏输出计算结果。
![24](https://github.com/moluwaiting/Fang/blob/master/ANSYS/25.png)
  
  
  
  
  
  
  
  
  
  
