import cv2
import os
from glob import glob
import sys

folder_name = 'snapshots/' + sys.argv[1]

image_files = sorted(glob(os.path.join(folder_name, '*.webp')))

if not image_files:
    print(f"No images found in folder {folder_name}.")
    exit()

frame = cv2.imread(image_files[0])
height, width, layers = frame.shape

output_video = cv2.VideoWriter(f'{folder_name}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

for image_file in image_files:
    frame = cv2.imread(image_file)
    output_video.write(frame)

output_video.release()

print(f"Video has been saved as {folder_name}.mp4")
