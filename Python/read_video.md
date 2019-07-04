```python
import numpy as np
import cv2

cap = cv2.VideoCapture("C:/Users/方人杰/Desktop/1.MOV")

w = cap.get(3)
h = cap.get(4) #获取整个视频的长和高

mx = int(w/2)
my = int(h/2) #取视频的中间点

count = 0

while(cap.isOpened()): #当视频成功打开时,执行
    ret, frame = cap.read()
    try:
        count = count + 1
        text = str(count)
        cv2.putText(frame,text,(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        frame2 = frame

        line1 = np.array([[100, 100], [300, 100], [350, 200]], np.int).reshape((-1, 1, 2)) #视频中画线
        line2 = np.array([[400, 50], [450, 300]], np.int).reshape((-1, 1, 2))

        frame2 = cv2.polylines(frame2, [line1], False, (255, 0, 0), thickness=2)
        frame2 = cv2.polylines(frame2, [line2], False, (0, 0, 255), thickness=1)

        cv2.imshow("Frame", frame2)
        
    except:
        print("EOF")
        break

    k = cv2.waitKey(30)
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

```
