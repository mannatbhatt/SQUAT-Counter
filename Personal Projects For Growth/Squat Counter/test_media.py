import mediapipe as mp

print(mp.__version__)
print(hasattr(mp, "solutions"))

mp_pose = mp.solutions.pose

print("Working!")
