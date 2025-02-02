from ultralytics import YOLO

yolo = YOLO("yolov8n.pt")

results = yolo.train(data='datasets/HHE-6/data.yaml', epochs=1, batch=8)
