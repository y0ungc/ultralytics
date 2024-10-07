from ultralytics import YOLO, KD_YOLO
import torch

 # Initialize teacher and student models
teacher_model = KD_YOLO("yolov8n-seg.yaml" )
student_model = KD_YOLO("yolov8n-seg.yaml", teacher_model=teacher_model, distillation_alpha=0.5, temperature=3,feature_layers=[6])
model = YOLO("yolov8n-seg.yaml")
# Train the model
# results = model.train(data=r"E:\code\yolo-kl\ultralytics\coco8-seg\coco8-seg.yaml", epochs=100, imgsz=640)