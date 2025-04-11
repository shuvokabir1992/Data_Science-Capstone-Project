import cv2
import threading

# List your video file paths here
video_paths = [
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_3\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_9\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_10\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_11\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_12\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_13\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_14\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_16\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_17\result_3.mp4",
    r"M:\Ravinaidu, Goutham\Inference\output_video\Model_Train_19\result_3.mp4"

]

# Function to loop a video in a window
def play_video_loop(video_path, window_name, x, y, width, height):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.moveWindow(window_name, x, y)

    while True:
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # End of video
            frame_resized = cv2.resize(frame, (width, height))
            cv2.imshow(window_name, frame_resized)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyWindow(window_name)
                return
        cap.release()  # Restart video

# Define large window size
window_width = 150     # Half of 1920 screen width
window_height = 150    # Tall enough to fit 5 stacked rows on a 1080 screen

# Positioning logic for 5 rows × 2 columns
positions = []
for i in range(10):
    col = i % 2
    row = i // 2
    x = col * window_width
    y = row * window_height
    positions.append((x, y))

# Launch threads for each video
threads = []
for i in range(len(video_paths)):
    t = threading.Thread(
        target=play_video_loop,
        args=(video_paths[i], f'Video {i+1}', positions[i][0], positions[i][1], window_width, window_height)
    )
    t.start()
    threads.append(t)

# Keep running
for t in threads:
    t.join()

cv2.destroyAllWindows()
