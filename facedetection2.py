import cv2 as cv
from  mtcnn.mtcnn import MTCNN
import numpy as np

capture = cv.VideoCapture(0)
detector = MTCNN()

while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        results = detector.detect_faces(frame)
        x1, y1, width, height = results[0]['box']
        x2, y2 = x1 + width, y1 + height
        cv.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), thickness=2)
        cv.imshow("Frame", frame)
        k = cv.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
