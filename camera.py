import cv2

camera = cv2.VideoCapture(0)

while True:
    ret,frame = camera.read()
    if ret:
        frame = cv2.flip(frame,1)
        cv2.imshow('Video',frame)
        if(cv2.waitKey(1) & 0xFF == ord('x')):
            break
        
camera.release()
cv2.destroyAllWindows()