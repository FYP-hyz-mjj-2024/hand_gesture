
# Hand Gesture Detection Demo using Mediapipe

## Setup the demo

1. Run `python -m venv hand_venv`
2. Run `source hand_venv/bin/activate` if you use mac. Run `hand_venv/Scripts/activate` if you use windows.
3. Run `pip install -r requirements.txt` to install openCV and mediapipe.

## Run the demo
### Video Mode
Run `python main.py video data/source/<file_name>.mp4 data/landmarks/<output_file_name>.txt`. 

### Camera Mode
Run `python main.py camrea`. Remember to allow this program to access your camera.

### Image Mode
Work in progress.

## Project Structures
### `source_capture/`
Capture the sources for detection. You can use an image or a stream. A stream is either a video or a real-time camera capture.

### `source_process/`
Given the captured source, process the source. With the mediapipe hand detection model, retrieve the data points and draw them on the canvas.

## Sample

A detection result for a specific frame:
```console
-------------------
[landmark {
  x: 0.908537507
  y: 1.05050921
  z: 6.6770059e-07
}
landmark {
  x: 0.81755954
  y: 0.979975641
  z: -0.115867198
}
landmark {
  x: 0.762154877
  y: 0.8458758
  z: -0.160453662
}
landmark {
  x: 0.74231261
  y: 0.712517202
  z: -0.175989434
}
landmark {
  x: 0.780311406
  y: 0.617112756
  z: -0.185466141
}
landmark {
  x: 0.918740571
  y: 0.720607042
  z: -0.141742826
}
landmark {
  x: 0.942003846
  y: 0.522598326
  z: -0.172112137
}
landmark {
  x: 0.94596988
  y: 0.396635443
  z: -0.192264
}
landmark {
  x: 0.947727323
  y: 0.306746453
  z: -0.201445758
}
landmark {
  x: 0.963380098
  y: 0.712064564
  z: -0.074523285
}
landmark {
  x: 0.979586124
  y: 0.534644961
  z: -0.0875244737
}
landmark {
  x: 0.956810594
  y: 0.433138043
  z: -0.0920002535
}
landmark {
  x: 0.940359712
  y: 0.373467028
  z: -0.0947659165
}
landmark {
  x: 0.978215039
  y: 0.714163721
  z: -0.0107686529
}
landmark {
  x: 0.974235296
  y: 0.563725352
  z: -0.0247343685
}
landmark {
  x: 0.945077777
  y: 0.464183807
  z: -0.031291198
}
landmark {
  x: 0.933612585
  y: 0.406582952
  z: -0.0310732294
}
landmark {
  x: 0.976388
  y: 0.716671228
  z: 0.046552591
}
landmark {
  x: 0.962805629
  y: 0.586900711
  z: 0.0404239371
}
landmark {
  x: 0.947052896
  y: 0.506292284
  z: 0.041402258
}
landmark {
  x: 0.944795847
  y: 0.463924766
  z: 0.0461087637
}
]
```