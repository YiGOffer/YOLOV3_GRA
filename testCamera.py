import numpy as np
import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(5)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,960)
# FourCC 编码是 XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("test1.avi", fourcc, fps, (width, height))
cv2.resizeWindow("frame", 1000,500)
while 1:
    ret, frame = cap.read()
    print('wideth:',width,height)
    
    if frame is None:
        break
    else:
        # 对每一帧都进行处理
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow("video", frame)
        k = cv2.waitKey(25) & 0xFF
        if k == 27:
            break

cap.release()
out.release()
cv2.destroyAllWindows()