import pong
import cv2
pongGame = pong.PongGame()
#frame = pongGame.getPresentFrame()
for i in range(1,100):
    reward, frame = pongGame.getNextFrame(1)
frame = cv2.cvtColor(cv2.resize(frame, (80, 80)), cv2.COLOR_BGR2GRAY)
ret, frame = cv2.threshold(frame,1,255,cv2.THRESH_BINARY)
cv2.imwrite("out.jpg", frame)
