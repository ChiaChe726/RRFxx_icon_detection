from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("runs/yolov8n_Dataset_type_v6_by_3090.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates '*.onnx'

# Export the model to NCNN format
model.export(format="ncnn")  # creates

#https://github.com/Tencent/ncnn/wiki/how-to-build#build-for-android
