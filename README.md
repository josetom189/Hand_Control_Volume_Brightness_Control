# 🎛️ Dual Hand Control — Volume & Brightness

Control your **system volume** and **screen brightness** using simple hand gestures captured through your webcam.  
Built with **Python**, **OpenCV**, and **MediaPipe** for real-time hand tracking.  

---

## ✨ Features
- **Right Hand** → Adjust **Volume**
- **Left Hand** → Adjust **Brightness**
- Smooth control based on distance between thumb and index finger
- Real-time webcam preview with visual feedback
- No extra hardware required — just your webcam

---

## 📦 Requirements

Install all dependencies:

```bash
pip install opencv-python mediapipe numpy pycaw screen-brightness-control comtypes


How It Works

OpenCV captures your webcam feed.

MediaPipe Hands detects hand landmarks.

Script calculates distance between thumb tip (landmark 4) and index tip (landmark 8).

Distance is mapped to a percentage using numpy.interp:

Right Hand → System volume via pycaw

Left Hand → Screen brightness via screen-brightness-control

▶️ Usage

Connect your webcam.

Run:

python Dualhandcontrol_Volume_Brightness.py


Gestures:

Right Hand: Thumb & index apart → Increase volume

Left Hand: Thumb & index apart → Increase brightness

Press q to quit.

🖥️ Control Mapping
Gesture	Hand	Action
Thumb & index close together	Right	Volume low
Thumb & index far apart	Right	Volume high
Thumb & index close together	Left	Brightness low
Thumb & index far apart	Left	Brightness high
