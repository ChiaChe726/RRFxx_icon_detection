from roboflow import Roboflow
file_path = "roboflow_api_key.text"

# 開啟檔案並將每行讀入列表
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        # 例如：處理每行數據，去除多餘空白並印出
        lines = line.strip()

print(lines)

rf = Roboflow(api_key=lines)
project = rf.workspace("hhe-3jp9r").project("hhe")
version = project.version(6)
dataset = version.download("yolov11")
