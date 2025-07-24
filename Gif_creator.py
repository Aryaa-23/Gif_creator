import imageio.v3 as iio
from PIL import Image
import numpy as np
import os

# --- Setup folders ---
input_folder = "C:/Users/Dell/Downloads/gif_creator/images"
output_folder = "C:/Users/Dell/Downloads/gif_creator/output_gif"
output_file = os.path.join(output_folder, "my_gif.gif")

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# --- Load and sort image files ---
image_files = sorted([
    f for f in os.listdir(input_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
])

if not image_files:
    raise ValueError("No images found in the 'images/' folder.")

# --- Load and process images ---
first_image_path = os.path.join(input_folder, image_files[0])
first_image = Image.open(first_image_path)
target_size = first_image.size  # (width, height)

images = []
for filename in image_files:
    path = os.path.join(input_folder, filename)
    img = Image.open(path).convert("RGB").resize(target_size)
    images.append(np.array(img))

# --- Create and save GIF ---
iio.imwrite(output_file, images, duration=500, loop=0)

print(f"✅ GIF successfully created: {output_file}")
