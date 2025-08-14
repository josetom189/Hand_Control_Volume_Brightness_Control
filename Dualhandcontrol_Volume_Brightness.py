import cv2
import mediapipe as mp
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
# PyCaw setup (Volume)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_ctrl = cast(interface, POINTER(IAudioEndpointVolume))
min_vol, max_vol = volume_ctrl.GetVolumeRange()[0:2]

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Webcam
cap = cv2.VideoCapture(0)

def get_distance(lm_list, p1, p2, w, h):
    x1, y1 = int(lm_list[p1].x * w), int(lm_list[p1].y * h)
    x2, y2 = int(lm_list[p2].x * w), int(lm_list[p2].y * h)
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance, (x1, y1), (x2, y2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_handedness.classification[0].label  # 'Left' or 'Right'
            lm_list = hand_landmarks.landmark

            # Get distance between thumb and index finger
            dist, (x1, y1), (x2, y2) = get_distance(lm_list, 4, 8, w, h)

            # Draw hand and gesture line
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

            if label == 'Right':
                # Control Volume
                vol = np.interp(dist, [20, 150], [min_vol, max_vol])
                vol_percent = np.interp(dist, [20, 150], [0, 100])
                volume_ctrl.SetMasterVolumeLevel(vol, None)
                cv2.putText(img, f'Volume: {int(vol_percent)}%', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            elif label == 'Left':
                # Control Brightness
                brightness = np.interp(dist, [20, 150], [0, 100])
                try:
                    sbc.set_brightness(int(brightness))
                except Exception as e:
                    print("Brightness Error:", e)
                cv2.putText(img, f'Brightness: {int(brightness)}%', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

    cv2.imshow("Dual Hand Control (Volume & Brightness)", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows(

