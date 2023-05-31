# Oscilloscope Animation Program

This program generates an oscilloscope animation based on an input audio file. The program uses the matplotlib library to create the animation frames and the ffmpeg library to convert the frames into a video.

## Prerequisites

- Python 3.x
- Required Python packages: numpy, matplotlib, ffmpeg-python, Pillow, librosa, tqdm

## Usage

```
python oscilloscope.py <input_file> <output_directory> <fps> <width> <height>
```

- `<input_file>`: Path to the input audio file.
- `<output_directory>`: Directory where the output video file will be saved.
- `<fps>`: Frames per second of the output video.
- `<width>`: Width of the output video in pixels.
- `<height>`: Height of the output video in pixels.

## Example

```
python oscilloscope.py audio.wav output/ 30 800 600
```

## Functionality

1. The program reads the command line arguments to obtain the input file, output directory, frame rate, width, and height for the video.
2. It loads the audio file using the librosa library.
3. The number of frames is calculated based on the duration of the audio and the frame rate.
4. The program initializes the figure and axis for the oscilloscope waveform.
5. The update function is defined, which is called for each frame of the animation and updates the waveform based on the current audio samples.
6. The animation is created using the FuncAnimation class from matplotlib.
7. A temporary directory is created to store the animation frames.
8. Each frame of the animation is saved as an image file in the temporary directory.
9. The program uses ffmpeg to convert the frames into a video file.
10. The temporary directory and its contents are removed.
11. The path of the output video file is printed.

## Dependencies

- numpy: Used for numerical operations on arrays.
- matplotlib: Used for creating the oscilloscope animation and saving frames.
- ffmpeg: Used for converting the frames into a video.
- Pillow: Used for image processing and saving frames.
- librosa: Used for loading the audio file.
- tqdm: Used for displaying a progress bar during frame saving.

## Credits

This program was created by OpenAI ChatGPT.