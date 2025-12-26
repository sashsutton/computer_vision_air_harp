# Air-Harp: Computer Vision Musical Instrument

Air-Harp is an interactive computer vision application that transforms your hand movements into a digital musical instrument. By using your webcam and Google’s MediaPipe technology, it detects your finger positions in real-time to "pluck" virtual strings suspended in mid-air.

---

## ✨ Features
- Real-Time Hand Tracking: Utilises MediaPipe’s Hand Landmarker to track the tip of your index finger with high precision.

- Virtual "Pluck" Logic: Triggers audio samples when your finger crosses a specific horizontal detection line from top to bottom.

- Visual Feedback: Features an on-screen HUD (Heads-Up Display) that shows the harp zones, the detection line, and a tracking marker on your finger.

- Multi-Channel Audio: Built with pygame.mixer to allow multiple sounds to trigger and overlap naturally.

## 🛠️ Tech Stack
- Python 3.x

- OpenCV: For video capture and visual rendering.

- MediaPipe: For advanced hand landmark detection.

- Pygame: For low-latency audio playback.

## 📂 Project Structure
```text
.
├── app.py              # Main application logic and UI
├── hand_tracker.py     # MediaPipe hand detection wrapper
├── audio_engine.py     # Audio playback management
├── hand_landmarker.task # Pre-trained MediaPipe model
└── sounds/             # Directory containing harp .wav samples
```
---
## 🚀 Getting Started

## 1. Prerequisites
- Ensure you have the following libraries installed:

    ```bash
    pip install opencv-python mediapipe pygame
    ```

### 2. Assets
- Place 5 harp sound files in the `sounds/` directory named `harp1.wav` through `harp5.wav`.

- Ensure the `hand_landmarker.task` file is in the root directory.

### 3. Running the App
- Execute the main script to start the harp:
    ```bash
    python app.py
    ```

## 🎹 How to Play
- Calibration: Stand in front of your webcam. You will see a red line labelled "STRINGS" across the screen.

- Zones: The screen is divided into 5 vertical zones, each corresponding to a different harp sound.

- Plucking: Move your index finger from above the red line to below it within a specific zone. The corresponding sound will trigger.

- Reset: Lift your finger back above the red line to "reset" the string for the next pluck.

- Exit: Press 'q' on your keyboard to close the application.

## ⚙️ Configuration
- You can customise the instrument by modifying constants in `app.py`:

- DETECTION_LINE_Y: Change the height of the virtual strings.

- STRING_COUNT: Adjust the number of zones/sounds (ensure you update SOUND_PATHS accordingly).




