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

## ⚙️ How It Works
1. **OpenCV** captures your webcam feed.
2. **MediaPipe Hands** detects hand landmarks.
3. The script calculates the **distance** between:
   - **Thumb tip** → Landmark `4`
   - **Index tip** → Landmark `8`
4. Distance is mapped to a percentage using `numpy.interp`:
   - **Right Hand** → Adjusts **system volume** via `pycaw`
   - **Left Hand** → Adjusts **screen brightness** via `screen-brightness-control`

---

## ▶️ Usage
1. Connect your webcam.
2. Run the script:
   ```bash
   python Dualhandcontrol_Volume_Brightness.py

## 📦 Requirements

Install all dependencies:

```bash
pip install opencv-python mediapipe numpy pycaw screen-brightness-control comtypes

---
