
```python
import cv2
import time

camera = cv2.VideoCapture(0)
cv2.namedWindow('MyCamera')
a=0
while True:
    a=a+1
    check, frame = camera.read() #返回两个值，第一个是判断视频读取有没有成功，第二个是一帧一帧的图片
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('MyCamera',frame)

    if cv2.waitKey(1) & 0xff == ord('q'): #按q退出
        break

print("视频中共有"+str(a)+"帧图片！")

cv2.destroyAllWindows

camera.release()

```
