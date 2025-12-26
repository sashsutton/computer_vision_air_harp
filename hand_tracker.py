import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2


class HandTracker:
    def __init__(self, model_path='hand_landmarker.task'):
        # Configure the Task
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1,
            running_mode=vision.RunningMode.IMAGE  # We will process frame by frame
        )
        self.detector = vision.HandLandmarker.create_from_options(options)

    def find_position(self, img):
        # MediaPipe Tasks requires an mp.Image object
        # Convert OpenCV BGR to RGB first
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_img)

        # Detect
        result = self.detector.detect(mp_image)
        lm_list = []

        # Parse the result into our [id, x, y] format
        if result.hand_landmarks:
            landmarks = result.hand_landmarks[0]
            h, w, _ = img.shape
            for id, lm in enumerate(landmarks):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

        return lm_list