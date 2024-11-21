import os
import cv2
from ultralytics import YOLO

# Disable CUDA devices
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # CPU only

# Load the YOLO model
train_set = "train1"
model = YOLO(os.path.join(f"runs/{train_set}/weights/best.pt"))

# Open the video file
# video_name = "Lexus｜Apple CarPlay & Android Auto操作"
video_name = "剪輯_【Apple CarPlay & Android Auto連線教學、異常狀況排除】只要一招！馬上把BMW iDriv"

video_path = os.path.join("/home/hhe/Documents", f"{video_name}.mp4")
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frame rate
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of the frames
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height of the frames

# Define the codec and create VideoWriter object
output_path = os.path.join("/home/hhe/Documents",
                           f"{train_set}_output_{video_name}.mp4")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for .mp4 files
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video
        out.write(annotated_frame)

        # Display the annotated frame (optional, can be removed in headless environments)
        cv2.imshow("YOLO Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture and writer objects, and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved to: {output_path}")
