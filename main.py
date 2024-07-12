import sys
from source_capture import get_image_source, get_camera_source, get_video_source
from source_process import process_stream, process_image

_, mode, path = sys.argv


def demo_image():
    frame = get_image_source(path, log_before_call=f"Opening {path}")
    process_image(frame)


def demo_video():
    cap = get_video_source(path)
    process_stream(cap, True)


def demo_camera():
    cap = get_camera_source()
    process_stream(cap, True)


mode_func = {
    'image': demo_image,
    'video': demo_video,
    'camera': demo_camera
}

mode_func[mode]()
