import cv2
from hand_tracker import HandTracker
from audio_engine import AudioEngine

# Configuration - Ensure these filenames match your 5 harp sounds
SOUND_PATHS = [
    "sounds/harp1.wav",
    "sounds/harp2.wav",
    "sounds/harp3.wav",
    "sounds/harp4.wav",
    "sounds/harp5.wav"
]
STRING_COUNT = 5
DETECTION_LINE_Y = 350  # Height of your "invisible strings"


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera access denied. Check macOS System Settings > Privacy > Camera.")
        return

    tracker = HandTracker(model_path='hand_landmarker.task')
    audio = AudioEngine(SOUND_PATHS)

    # Track state: is the finger currently "below" the line in a specific zone?
    string_states = [False] * STRING_COUNT

    while True:
        success, img = cap.read()
        if not success: break

        img = cv2.flip(img, 1)  # Mirror for natural hand movement
        h, w, _ = img.shape
        lm_list = tracker.find_position(img)

        # Draw Harp Zones (Visual Guide)
        zone_width = w // STRING_COUNT
        for i in range(STRING_COUNT):
            cv2.line(img, (i * zone_width, 0), (i * zone_width, h), (100, 100, 100), 1)

        if len(lm_list) > 0:
            # We track the Tip of the Index Finger (Landmark 8)
            index_x, index_y = lm_list[8][1], lm_list[8][2]

            # Determine which zone the finger is in
            zone = min(index_x // zone_width, STRING_COUNT - 1)

            # PLUCK LOGIC: Trigger if finger crosses the line from top to bottom
            if index_y > DETECTION_LINE_Y and not string_states[zone]:
                audio.play(zone)
                string_states[zone] = True
                print(f"Plucked String {zone + 1}")
            elif index_y < DETECTION_LINE_Y:
                string_states[zone] = False  # Reset when hand is lifted

            # Visual feedback on finger
            cv2.circle(img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)

        # Draw the "String Line"
        cv2.line(img, (0, DETECTION_LINE_Y), (w, DETECTION_LINE_Y), (0, 0, 255), 2)
        cv2.putText(img, "STRINGS", (10, DETECTION_LINE_Y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Air-Harp", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()