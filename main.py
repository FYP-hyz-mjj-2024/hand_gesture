import sys
from source_capture import get_image_source, get_camera_source, get_video_source
from source_process import process_stream, process_image

# _, mode, src_path, save_path = sys.argv

args = {i: arg for i, arg in enumerate(sys.argv[1:], start=1)}
mode, src_path, save_path = args.get(1), args.get(2), args.get(3)


def demo_image():
    frame = get_image_source(src_path)
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
