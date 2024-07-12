import sys
from source_capture import get_image_source, get_camera_source, get_video_source
from source_process import process_stream, process_image

#data/landmarks/test.txt
_, mode, src_path, save_path = sys.argv


def demo_image():
    frame = get_image_source(src_path, log_before_call=f"Opening {src_path}")
    process_image(frame)


def demo_video():
    cap = get_video_source(src_path)
    process_stream(cap, save_path, True)


def demo_camera():
    cap = get_camera_source()
    process_stream(cap, save_path, True)


mode_func = {
    'image': demo_image,
    'video': demo_video,
    'camera': demo_camera
}

mode_func[mode]()
