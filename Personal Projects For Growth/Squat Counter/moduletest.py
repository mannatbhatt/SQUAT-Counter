import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import mediapipe as mp

print(mp.__version__)

mp_pose = mp.solutions.pose
print("MediaPipe working!")
