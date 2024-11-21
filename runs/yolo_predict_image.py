import os
from ultralytics import YOLO

# Disable CUDA devices
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # CPU only

jpg = "image/image001.jpg"
jpg2 = "image/image002.jpg"

# Load the YOLO model
train_set = "train3090"
model = YOLO(os.path.join(f"runs/{train_set}/weights/best.pt"))


# show=True will display the image with bounding boxes
results = model.predict(source=jpg, save=True, show=True)
# save=True will save the image with bounding boxes
results = model.predict(source=jpg2, save=True, show=True)
