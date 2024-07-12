import cv2
from utils.wrapper import log


def _get_stream_source(source, w=640, h=480):
    """
    Initialize a stream source.
    :param source: Source of the stream.
    :param w: Width
    :param h: Height
    :return: A cv2 video capture object.
    """
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return cap


@log
def get_image_source(path):
    """
    Retrieves an image from the given path, and get an image object.
    :param path: A path to a desired image.
    :return: An image object.
    """
    image = cv2.imread(path)
    return image


@log
def get_camera_source(w=640, h=480):
    """
    Initialize a camera source.
    :param w: Width
    :param h: Height
    :return:
    """
    return _get_stream_source(0, w, h)

@log
def get_virtual_camera_source(w=640, h=480):
    """
    Initialize a virtual camera source.
    :param w: Width
    :param h: Height
    :return:
    """
    return _get_stream_source(1, w, h)

@log
def get_video_source(path, w=640, h=480):
    """
    Initialize a video source.
    :param path:
    :param w: Width
    :param h: Height
    :return:
    """
    return _get_stream_source(path, w, h)
