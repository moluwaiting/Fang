```python
import numpy as np
import cv2

cap = cv2.VideoCapture("C:/Users/方人杰/Desktop/1.MOV")

while(cap.isOpened()): #当视频成功打开时,执行
    ret, frame = cap.read()
    try:
        cv2.imshow("Frame",frame)
    except:
        print("EOF")
        break

    k = cv2.waitKey(30)
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

```
