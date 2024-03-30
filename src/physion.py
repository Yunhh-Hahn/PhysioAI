import os
from dotenv import load_dotenv
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

load_dotenv()

model_path = os.getenv('MODEL_PATH')
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# callback function - called on each inference of pose landmark
def print_result(result: PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
        print('pose landmarker result: {}'.format(result))

# configure the options for pose landmark model
options = PoseLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.LIVE_STREAM,
        result_callback=print_result)

def physion_bot():
    with PoseLandmarker.create_from_options(options) as landmarker:
            cap = cv2.VideoCapture(0)

            while True:
                    ret, frame = cap.read()
                    if not ret:
                            break

                    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
                    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

                    # Send live image data to perform pose landmarking.
                    landmarker.detect_async(mp_image, cv2.getTickCount())

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

            cap.release()
            cv2.destroyAllWindows()