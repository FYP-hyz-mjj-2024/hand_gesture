
# Hand Gesture Detection Demo using Mediapipe

## Setup the demo

1. Run `python -m venv hand_venv` to create a dedicated virtual environment.
2. Run `source hand_venv/bin/activate` if you use mac. Run `hand_venv/Scripts/activate` if you use windows. This will activate the virtual environment you just created.
3. Run `pip install -r requirements.txt` to install openCV and mediapipe, along with any other required packages.

## Run the demo
### Image Mode
Run `python main.py image <path_to_image>`.

### Video Mode
Run `python main.py video <path_to_video> <path_to_txt_output>`. 

### Camera Mode
Run `python main.py camrea`. Remember to allow this program to access your camera.

### Virtual Camera Mode
Run `python main.py virtual_camera`. Remember to configure you virtual camera. It is recommended to use OBS.

## Project Structures
### `source_capture/`
Capture the sources for detection. You can use an image or a stream. A stream is either a video or a real-time camera capture.

### `source_process/`
Given the captured source, use the model to retrieve the data points for each frame and draw the data points and connections onto the frame.

## Source Processing Flowchart
### Definitons
**Frame -** A frame is a 2D array of pixels. A pixel is a 3-tuple of RGB/BGR values.
Therefore a frame is a 3D array.

**Image -** An image is a data structure that contains only one frame.

**Stream -** Both a video and a camera capture belongs to a stream.
A stream is a data structure that contains multiple frames.

### Process
No matter for Image or Stream, a frame is always processed by `process_single_frame`, a function
dedicated to use the mediapipe model to annotate the image.
![](./docs/source_process_flowchart.png)