from PIL import Image, ImageDraw
import random
import math
import os
from moviepy.editor import ImageSequenceClip

def save_brownian_motion_frames(frame_count=100, steps_per_frame=10, image_size=(500, 500), line_color=(255, 0, 0), line_width=2, output_folder="brownian_frames"):
    """
    Generates a sequence of frames showing Brownian motion and saves them as images.

    :param frame_count: Number of frames to generate.
    :param steps_per_frame: Number of steps (movements) in each frame.
    :param image_size: Size of the image (width, height).
    :param line_color: Color of the path line (R, G, B).
    :param line_width: Width of the path line.
    :param output_folder: Folder to save the frames.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize the starting point at the center of the image
    x, y = image_size[0] // 2, image_size[1] // 2

    # Initialize the image and drawing object
    image = Image.new("RGB", image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Generate frames
    for frame in range(frame_count):
        for _ in range(steps_per_frame):
            # Randomly choose a direction and distance for the next step
            angle = random.uniform(0, 2 * math.pi)
            dx, dy = line_width * math.cos(angle), line_width * math.sin(angle)

            # Draw a line from the current position to the new position
            draw.line([x, y, x + dx, y + dy], fill=line_color, width=line_width)

            # Update the position
            x, y = x + dx, y + dy

        # Save the frame
        frame_path = os.path.join(output_folder, f"frame_{frame:03d}.png")
        image.save(frame_path)

# Example usage
save_brownian_motion_frames()

def create_video_from_frames(frame_folder="brownian_frames", fps=10, output_file="brownian_motion.mp4"):
    # Get the list of all frame file names in sorted order
    frame_files = sorted([os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(".png")])

    # Create a video clip from the frames
    clip = ImageSequenceClip(frame_files, fps=fps)

    # Write the video file to disk
    clip.write_videofile(output_file)

# Create the video
create_video_from_frames()
