import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import ffmpeg
from PIL import Image
import librosa
from tqdm import tqdm

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 6:
	print("Usage: python oscilloscope.py <input_file> <output_directory> <fps> <width> <height>")
	sys.exit(1)

# Read command line arguments
input_file = sys.argv[1]
output_directory = sys.argv[2]
fps = int(sys.argv[3])
width = int(sys.argv[4])
height = int(sys.argv[5])

print("Input file:", input_file)
print("Output directory:", output_directory)
print("Frame rate:", fps)
print("Resolution:", width, "x", height)

# Load the audio file
audio_data, sample_rate = librosa.load(input_file, sr=None)

print("Audio loaded. Duration:", len(audio_data) / sample_rate)

# Calculate the number of frames based on the frame rate
duration = len(audio_data) / sample_rate
num_frames = int(duration * fps)

print("Number of frames:", num_frames)

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(width/100, height/100))

# Set the axis limits and labels
ax.set_xlim(0, duration)
ax.set_ylim(-1, 1)
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')

# Create a blank line object for the oscilloscope waveform
line, = ax.plot([], [])

# Define the update function for each frame of the animation
def update(frame):
	# Calculate the time range for the current frame
	t_start = frame / num_frames * duration
	t_end = (frame + 1) / num_frames * duration

	# Get the audio samples up to the current time
	samples = audio_data[:int(t_end * sample_rate)]

	# Update the line object with the new samples
	line.set_data(np.linspace(0, t_end, len(samples)), samples)

	return line,

# Create the animation using the update function
animation = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps)

# Create a temporary directory for storing the animation frames
temp_dir = 'temp_frames'
os.makedirs(temp_dir, exist_ok=True)

print("Saving animation frames...")

# Save each frame of the animation as an image with a progress bar
for frame in tqdm(range(num_frames), desc="Progress"):
	animation.event_source.start()
	output_file = os.path.join(temp_dir, f'frame_{frame:05d}.png')
	fig.savefig(output_file, dpi=100)
	animation.event_source.stop()

print("Animation frames saved.")

# Use ffmpeg to convert the frames into a video
output_file = os.path.join(output_directory, 'output.mp4')
animation.save(output_file, writer='ffmpeg', fps=fps)

print("Video file saved:", output_file)

# Remove the temporary directory and its contents
os.system(f'rm -r {temp_dir}')

print("Temporary directory removed.")

# Print the path of the output file
print("Output file saved at:", output_file)
