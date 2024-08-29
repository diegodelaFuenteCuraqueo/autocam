import cv2
import os
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

def get_timestamp():
    now = datetime.now()
    folder_name = now.strftime("%Y%m%d")
    timestamp = now.strftime("%Y.%m.%d-%H.%M.%S.%f")[:-3]
    return folder_name, timestamp

def save_image(frame, folder_name, timestamp):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, f"{timestamp}.webp")
    try:
        cv2.imwrite(file_path, frame, [cv2.IMWRITE_WEBP_QUALITY, 92])
        print(f"Saved {file_path}")
    except Exception as e:
        print(f"Error saving {file_path}: {e}")

with ThreadPoolExecutor(max_workers=4) as executor:
    while True:
        ret, frame = cap.read()
        if not ret: break

        folder_name, timestamp = get_timestamp()
        executor.submit(save_image, frame, 'snapshots/'+folder_name, timestamp)

        time.sleep(1)

cap.release()
cv2.destroyAllWindows()
