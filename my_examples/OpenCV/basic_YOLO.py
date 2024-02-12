from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

# path = "test.jpg"
# image = cv2.imread(path)

#model.predict("car-detection.mp4", save=True, show=True)

results = model(source="test.jpg", show=True)

