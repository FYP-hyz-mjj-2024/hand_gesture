import cv2
import mediapipe as mp
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


def get_detection_results(image, convert_to_rgb=False):
    """
    Given the image of a hand, get the result landmarks.
    :param image: An image, or a video frame.
    :param convert_to_rgb: Convert the image from BGR to RGB
    :return: Results
    """
    # Convert frame from BGR to RGB
    if convert_to_rgb:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect if there is any hand
    result = hand.process(image)

    return result


@log
def draw_detection_results(image, detection_result):
    """
    Based on the result from get_detection_results(), draw the result on the image.
    :param image: An image, or a video frame.
    :param detection_result: The result given by get_detection_results.
    :return:
    """
    for hand_landmarks in detection_result.multi_hand_landmarks:
        # Draw all the connection lines
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))


@log
def process_single_frame(frame, convert_to_rgb=False):
    """
    Process a single frame, i.e. an image. Get the result and draw it on the canvas.
    :param frame: The image to be processed.
    :param convert_to_rgb: Convert the image from BGR to RGB
    :return:
    """

    result = get_detection_results(frame, convert_to_rgb)

    # Detected Hand
    if result.multi_hand_landmarks:
        draw_detection_results(frame, result, log_before_call=result.multi_hand_landmarks)

    cv2.imshow("Hand Detection", frame)


@log
def process_image(image):
    process_single_frame(image)
    cv2.waitKey(0)


@log
def process_stream(cap, convert_to_rgb=False):
    """
    Process a stream, including a video or a camera capture.
    :param cap: The video/camera stream to be processed.
    :param convert_to_rgb: Convert the image from BGR to RGB.
    :return:
    """
    while True:
        success, frame = cap.read()
        if not success or cv2.waitKey(1) == 27:
            break

        process_single_frame(frame, convert_to_rgb)
