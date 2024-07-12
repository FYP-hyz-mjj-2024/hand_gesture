import cv2
import mediapipe as mp
import time
import os
from utils.wrapper import log
from utils.dictionaries import finger_colors, finger_indexes, landmark_name

# Hand checking model
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

# Drawing utilities
mp_drawing = mp.solutions.drawing_utils


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

    # For all hands, draw their landmarks
    for hand_idx, hand_landmarks in enumerate(detection_result.multi_hand_landmarks):
        # Draw all the connection lines.
        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

        # Draw each finger with custom settings
        for finger_name, finger_indices in finger_indexes.items():
            # Extract landmarks for the current finger
            finger_landmarks = [hand_landmarks.landmark[i] for i in finger_indices]

            # Draw landmarks of the current finger.
            for landmark in finger_landmarks:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, finger_colors[finger_name], -1)
                # Add coordinates next to the landmark
                cv2.putText(frame,
                            f"({x}, {y})",
                            (x + 10, y),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.3,
                            finger_colors[finger_name],
                            1)

            # Draw connections between the landmarks of the current finger.
            for i in range(len(finger_landmarks) - 1):
                start = finger_landmarks[i]
                end = finger_landmarks[i + 1]
                x1, y1 = int(start.x * frame.shape[1]), int(start.y * frame.shape[0])
                x2, y2 = int(end.x * frame.shape[1]), int(end.y * frame.shape[0])
                cv2.line(frame, (x1, y1), (x2, y2), finger_colors[finger_name], 2)
    return


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
        log_write_file(f, f"\n\nFRAME-{time.time()}\n")
        for hand_idx, hand_landmarks in enumerate(detection_result.multi_hand_landmarks):
            log_write_file(f, f"\nHAND-{hand_idx}\n")
            # Landmarks for a single hand
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
        log_detection_results(result, save_path) if save_path else None

    cv2.imshow("Hand Detection", frame)


def process_image(frame, convert_to_rgb=False):
    """
    Process an image, including only one frame.
    :param frame: The only frame in the image.
    :param convert_to_rgb: Convert the image from BGR to RGB.
    :return:
    """
    process_single_frame(frame, convert_to_rgb=convert_to_rgb)
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
