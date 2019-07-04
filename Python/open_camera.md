
```python
import cv2
import time

camera = cv2.VideoCapture(0)
cv2.namedWindow('MyCamera')
a=0
while True:
    a=a+1
    check, frame = camera.read()
    #print(check)
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('MyCamera',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

print("视频中共有"+str(a)+"帧图片！")

cv2.destroyAllWindows

camera.release()
```
