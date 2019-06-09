from PIL import Image
import cv2 as cv
import zlib

# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('/home/fang/桌面/m.jpeg')
imBytes1=im.tobytes()
print(len(imBytes1))
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//50, h//50))
# 把缩放后的图像用jpeg格式保存:
im.save('/home/fang/桌面/m1.jpeg', 'jpeg')
imBytes2=im.tobytes()
print(len(imBytes2))
im.show('/home/fang/桌面/m1.jpeg')
print(imBytes2)
