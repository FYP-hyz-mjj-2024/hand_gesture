import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Hand checking model
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

# Draw
mp_drawing = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()     # BGR
    if not success or cv2.waitKey(1) == 27:
        break

    # Convert frame from BGR to RGB
    RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect if there is any hand
    result = hand.process(RGB_frame)

    # Hand detected
    if result.multi_hand_landmarks:
        for hand_landmakrs in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmakrs, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Detection", frame)