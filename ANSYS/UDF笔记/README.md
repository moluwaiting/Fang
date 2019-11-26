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
