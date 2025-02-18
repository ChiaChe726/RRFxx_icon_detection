import os
import cv2
import time
import numpy as np
import mss
import gc
from ultralytics import YOLO

# =======================
# 參數設定
# =======================
# 螢幕參數：設定擷取區域、解析度與幀率
screen_width = 1920     # 螢幕寬度
screen_height = 1080    # 螢幕高度
fps = 60                # 目標幀率
frame_delta = 1 / fps   # 每一幀理想間隔時間（秒）

# 錄製持續時間（秒），長時間執行請自行調整（此處示範 1 小時）
duration = 3600
total_frames = int(fps * duration)

# 影片輸出設定：僅儲存辨識結果影片
output_folder = os.path.join("runs", "detect")
os.makedirs(output_folder, exist_ok=True)
output_filename = "annotated_detection_video.mp4"
output_path = os.path.join(output_folder, output_filename)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(
    output_path, fourcc, fps, (screen_width, screen_height))

# =======================
# YOLO 模型初始化
# =======================
# 載入已訓練的 YOLO 模型（根據實際模型路徑調整）
model_path = "runs/yolov8n_Dataset_type_v6_by_3090.engine"
model = YOLO(model_path)  # 若需要明確指定任務可加參數: task='detect'

# =======================
# 螢幕錄製與即時物件偵測
# =======================
with mss.mss() as sct:
    monitor = {"top": 0, "left": 0,
               "width": screen_width, "height": screen_height}
    start_time = time.perf_counter()  # 使用高精度計時器

    for frame_num in range(total_frames):
        # 擷取螢幕畫面
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # 執行 YOLO 物件偵測，取得辨識結果並標註
        results = model(frame)
        annotated_frame = results[0].plot()  # 模型內建繪製函式

        # 將標註後的影像寫入輸出影片（僅存結果影片）
        video_writer.write(annotated_frame)

        # 計算並顯示延遲：計算目前執行時間與理想時間的差值
        elapsed_time = time.perf_counter() - start_time
        expected_time = (frame_num + 1) * frame_delta
        delay = expected_time - elapsed_time
        print(
            f"Frame {frame_num + 1}/{total_frames} - Delay: {delay:.4f} s", end='\r', flush=True)

        # 若延遲為正，則等待以達到目標幀率
        if delay > 0:
            time.sleep(delay)

        # 先進行即時顯示，確保 annotated_frame 尚未被刪除
        cv2.imshow("YOLO Inference", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("\n使用者中斷錄製。")
            break

        # 記憶體優化：釋放中間變數
        del frame, results, annotated_frame, screenshot
        # 每處理一定幀數時強制回收垃圾以降低記憶體占用
        if frame_num % 100 == 0:
            gc.collect()

# 釋放資源
video_writer.release()
cv2.destroyAllWindows()
print(f"\n辨識結果影片儲存於: {output_path}")
