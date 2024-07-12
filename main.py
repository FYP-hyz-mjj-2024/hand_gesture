from source_capture import get_camera_source
from source_process import process_stream

cap = get_camera_source()
process_stream(cap, True)
