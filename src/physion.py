import cv2
import os
from dotenv import load_dotenv
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

load_dotenv()

model_path = os.getenv('MODEL_PATH')
window_name = "MediaPipe Pose Landmark"

device_id = 0
width = 500
height = 500
fps = 60

num_poses = 1
min_pose_detection_confidence = 0.5
min_pose_presence_confidence = 0.5
min_tracking_confidence = 0.5

def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)

    for idx in range(len(pose_landmarks_list)):
        pose_landmarks = pose_landmarks_list[idx]

        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(
                x=landmark.x,
                y=landmark.y,
                z=landmark.z) for landmark in pose_landmarks
        ])
        mp.solutions.drawing_utils.draw_landmarks(
            annotated_image,
            pose_landmarks_proto,
            mp.solutions.pose.POSE_CONNECTIONS,
            mp.solutions.drawing_styles.get_default_pose_landmarks_style())
    return annotated_image

to_window = None
last_timestamp_ms = 0

def print_result(detection_result: vision.PoseLandmarkerResult, output_image: mp.Image,
                 timestamp_ms: int):
    global to_window
    global last_timestamp_ms
    if timestamp_ms < last_timestamp_ms:
        return
    last_timestamp_ms = timestamp_ms
    to_window = cv2.cvtColor(
        draw_landmarks_on_image(output_image.numpy_view(), detection_result), cv2.COLOR_RGB2BGR)

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.LIVE_STREAM,
    num_poses=num_poses,
    min_pose_detection_confidence=min_pose_detection_confidence,
    min_pose_presence_confidence=min_pose_presence_confidence,
    min_tracking_confidence=min_tracking_confidence,
    output_segmentation_masks=False,
    result_callback=print_result
)

def physion_bot():
        with vision.PoseLandmarker.create_from_options(options) as landmarker:
                print("Starting PoseLandmarker...")
                cap = cv2.VideoCapture(0)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
                cap.set(cv2.CAP_PROP_FPS, fps)

                if cap.isOpened():
                        print("Successfully opened camera.")
                else:
                        print("Failed to open camera.")
                        return

                while cap.isOpened():
                        success, image = cap.read()
                        if not success:
                                print("Image capture failed.")
                                break

                        mp_image = mp.Image(
                                image_format=mp.ImageFormat.SRGB,
                                data=cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                        timestamp_ms = int(cv2.getTickCount() / cv2.getTickFrequency() * 1000)
                        landmarker.detect_async(mp_image, timestamp_ms)

                        if to_window is not None:
                                cv2.imshow(window_name, to_window)

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                                print("Quit command received. Exiting...")
                                break

                cap.release()
                cv2.destroyAllWindows()