# UDF 笔记
## 基本步骤
>* 1.使用任意文本编辑器书写C语言代码，命名为X.c，保存至工作路径下。
```C
/*************************************************************************/
/* udfexample.c                                                          */
/* UDF for specifying a steady-state velocity profile boundary condition */
/*************************************************************************/
#include "udf.h"
DEFINE_PROFILE(inlet_x_velocity, thread, index)//第一个变量用于定义速度入口的函数，名称可以任意指定。
{
real x[ND_ND];//real number		/* this will hold the position vector */
real y;
face_t f;
begin_f_loop(f, thread)//用来形成对边界区域上所有单元面的循环（loop through all cell faces in the boundary zone）
{
F_CENTROID(x,f,thread);
y = x[1];
F_PROFILE(f, thread, index) = 20. - y*y/(.0745*.0745)*20.;
}
end_f_loop(f, thread)
}
```
>* 2.运行Fluent，读入，并且设置case文件。
>* 3.编译、注释C语言源代码，Define -> User-Defined -> Functions -> Interpreted....，在source file name中选择C文件，stack size可以根据具体的情况变大
>* 4.点击compile对UDF文件进行编译，如果编译失败的话，会出现错误信息的。编译结束之后，点击close。
>* 5.在边界条件的速度inlet这里点击constant，即可修改为udf_velocity，于是可以更改参数进行下一步的计算。
## 一些宏的介绍
```C
DEFINE_CG_MOTION（name,dt,vel,omega,time,dtime）主要用于描述刚体的运动，运动过程中物体的几何形状不会发生改变，只是质心位置改变
参数解释：name:宏的名称，随意定义，dt：一个指针一个指针Dynamic_Thread *dt，存储动网格属性，通常不需要用户干预。
         vel:平动速度，为一个数组，其中vel[0]为x方向速度，vel[1]为y方向速度，vel[2]为z方向速度。
         omega:转动速度，omega[0]为x方向角速度，omega[1]为y方向角速度，omega[2]为z方向角速度。
         time：当前时间。
         dtime：时间步长。
上述宏返回数据vel和omega。
```

## 论文源码
```C
#include "udf.h"
real a = 0.04 //振幅，real为实数
real f = 0.2 //震荡频率，可以进行修改
real w;
real L;
real velocity;
DEFINE_CG_MOTION(rov_shengchen,dt,vel,omega,time,dtime)
{
    #if!RP_HOST
      w=2.0*M_PI*f;//角速度的求解
      /*Check to see if there is data*/
      if (!Data_Valid_P())
      {
          Message0("\n\n No data->No mesh motion!!!\n\n");
          return;
      }//数据校核
      /* Reset velocities*/
      NV_S(vel,=,0.0);
      NV_S(omega,=,0.0);
      L=a*sin(w*time)
      velocity=a*w*cos(w*time);//物体的振幅存入velocity这个变量里面
      Message0("\n UDF rov:time=%f,dtime=%f,z_vel=%f,\n",time,dtime,velo);
      vel[2]=velocity;//Z方向的速度
    #endif
      node_to_host_real_1(velocity);
      node_to_host_real(vel,ND_ND);
}
```
