import cv2
import mediapipe as mp
import time
import os
from utils.wrapper import log

# Hand checking model
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

# Drawing utilities
mp_drawing = mp.solutions.drawing_utils

# Finger colors
finger_colors = {
    "thumb": (255, 0, 0),
    "index": (0, 255, 0),
    "middle": (0, 0, 255),
    "ring": (255, 255, 0),
    "pinky": (255, 0, 255)
}

# Finger Landmarks
landmark_name = {
    0: "WRIST"
    , 1: "THUMB_CMC", 2: "THUMB_MCP", 3: "THUMB_IP", 4: "THUMB_TIP",
    5: "INDEX_FINGER_MCP", 6: "INDEX_FINGER_PIP", 7: "INDEX_FINGER_DIP", 8: "INDEX_FINGER_TIP",
    9: "MIDDLE_FINGER_MCP", 10: "MIDDLE_FINGER_PIP", 11: "MIDDLE_FINGER_DIP", 12: "MIDDLE_FINGER_TIP",
    13: "RING_FINGER_MCP", 14: "RING_FINGER_PIP", 15: "RING_FINGER_DIP", 16: "RING_FINGER_TIP",
    17: "PINKY_MCP", 18: "PINKY_PIP", 19: "PINKY_DIP", 20: "PINKY_TIP"
}


def get_detection_results(frame, convert_to_rgb=False):
    """
    Given the image of a hand, get the result landmarks.
    :param frame: An image, or a video frame.
    :param convert_to_rgb: Convert the image from BGR to RGB
    :return: Results
    """
    # Convert frame from BGR to RGB
    if convert_to_rgb:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect if there is any hand
    result = hand.process(frame)

    return result


def draw_detection_results(frame, detection_result):
    """
    Based on the result from get_detection_results(), draw the result on the image.
    :param frame: An image, or a video frame.
    :param detection_result: The result given by get_detection_results.
    :return:
    """
    for hand_idx, hand_landmarks in enumerate(detection_result.multi_hand_landmarks):
        # Draw all the connection lines
        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))


def log_detection_results(detection_result, save_path=None):
    """
    Log the data detected at a specific frame
    :param detection_result: A
    :param save_path: A path to the save destination of data.
    :return:

    """

    if not save_path:
        raise ValueError("No save paths!")

    def log_write_file(file, data):
        print(data)
        file.write(data)

    with open(save_path, "a") as f:

        for hand_idx, hand_landmarks in enumerate(detection_result.multi_hand_landmarks):
            log_write_file(f, f"\n{time.time()}\n")
            # Landmarks for a single hand
            hand_landmarks_coord = []
            for ldmk_idx, landmark in enumerate(hand_landmarks.landmark):
                this_landmark_name = landmark_name[ldmk_idx]
                this_landmark_coord = ("{:.16f}".format(landmark.x), "{:.16f}".format(landmark.y), landmark.z)
                log_write_file(f, f"{this_landmark_name} {' '*(17-len(this_landmark_name))} - {this_landmark_coord}\n")


def process_single_frame(frame, save_path=None, convert_to_rgb=False):
    """
    Process a single frame, i.e. an image. Get the result and draw it on the canvas.
    :param frame: The image to be processed.
    :param save_path: A path to the save destination of data.
    :param convert_to_rgb: Convert the image from BGR to RGB
    :return:
    """

    result = get_detection_results(frame, convert_to_rgb)

    # Detected Hand
    if result.multi_hand_landmarks:
        draw_detection_results(frame, result)
        log_detection_results(result, save_path)

    cv2.imshow("Hand Detection", frame)


def process_image(image):
    process_single_frame(image)
    cv2.waitKey(0)


def process_stream(cap, save_path=None, convert_to_rgb=False):
    """
    Process a stream, including a video or a camera capture.
    :param cap: The video/camera stream to be processed.
    :param save_path: The save path to the data.
    :param convert_to_rgb: Convert the image from BGR to RGB.
    :return:
    """

    # If file in the save path exists, delete it
    if save_path and os.path.exists(save_path):
        os.remove(save_path)

    while True:
        success, frame = cap.read()
        if not success or cv2.waitKey(1) == 27:
            break

        process_single_frame(frame, save_path, convert_to_rgb)
