from ultralytics import YOLO

model = YOLO("runs/yolov8n_Dataset_type_v6_by_3090.pt")

model.export(format="engine", int8=True)

# for Jetson Orin Nano TensorRT
# model.export(format="engine", device="dla:1", half=True)
