# import torch
# import torchvision
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# boxes = torch.tensor([[0., 1., 2., 3.]]).to(device)
# scores = torch.randn(1).to(device)
# iou_threshold = 0.5
# try:
#     torchvision.ops.nms(boxes, scores, iou_threshold)
#     print("torchvision supports CUDA.")
# except NotImplementedError as e:
#     print("torchvision does not support CUDA.")
#     print(e)

import torch
import torchvision

print("Torch Version:", torch.__version__)
print("TorchVision Version:", torchvision.__version__)
print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("CUDA Device:", torch.cuda.get_device_name(0))