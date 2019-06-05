# 神经网络
## 资料
- [Faster R-CNN论文翻译——中英文对照](http://noahsnail.com/2018/01/03/2018-01-03-Faster%20R-CNN%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91%E2%80%94%E2%80%94%E4%B8%AD%E8%8B%B1%E6%96%87%E5%AF%B9%E7%85%A7/)
- [Faster R-CNN文章详细解读](https://blog.csdn.net/liuxiaoheng1992/article/details/81843363)
- [一文读懂Faster-RCNN](https://zhuanlan.zhihu.com/p/31426458)
- [Faster-RCNN  B站](https://www.bilibili.com/video/av52033795?t=1432&p=3)
- [莫烦B站](https://www.bilibili.com/video/av16001891?t=612&p=22)
## 术语
- softmax:概率学中的归一化函数，可以计算每个推荐具体属于哪个类别，输出为cls_prob分类预测的概率向量（0-1.0之间）
- 全连接层（fully connected layers，FC）：分类器的作用。
- [锚（anchors）](https://blog.csdn.net/sinat_33486980/article/details/81099093)：实际上就是一组矩形，可以由一组矩阵表示，n行4列，n行代表矩形的个数，4列代表（x,y,w,h），表示矩形的形状。一般的为9个矩形，长宽比大约为{1:2，1:1,2:1}三种。

- [卷积和池化（pooling）](https://blog.csdn.net/qq_40525008/article/details/79964306):
![卷积](http://ufldl.stanford.edu/wiki/images/6/6c/Convolution_schematic.gif)
- [VGG](https://baike.baidu.com/item/VGG%20%E6%A8%A1%E5%9E%8B/22689655?fr=aladdin):
