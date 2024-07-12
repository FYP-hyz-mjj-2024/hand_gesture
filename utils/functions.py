def get_distance(landmark1, landmark2):
    """
    Get the distance between the two landmarks.
    :param landmark1: The first landmark.
    :param landmark2: The second landmark.
    :return:
    """
    return ((landmark1.x - landmark2.x) ** 2 + (landmark1.y - landmark2.y) ** 2) ** 0.5