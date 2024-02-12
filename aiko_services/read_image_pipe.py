from typing import Tuple
import cv2
from ultralytics import YOLO

from aiko_services import aiko, PipelineElement

_LOGGER = aiko.logger(__name__)
#cap = cv2.VideoCapture(0)

model = YOLO("yolov8n.pt")

# --------------------------------------------------------------------------- #

# class PE_ReadVideo(PipelineElement):
#     def __init__(self, context):
#         context.set_protocol("readvideo")
#         context.get_implementation("PipelineElement").__init__(self, context)

#     def process_frame(self, context, timer):
#         _LOGGER.info(f"PE_ReadVideo: {context}, read 10 seconds")

#         if (cap.isOpened() == False): 
#             _LOGGER("Unable to read camera feed")

#         frames = []
#         timer = int(timer)
#         while(timer > 0):
#             ret, frame = cap.read()
#             _LOGGER.info(timer)
#             frames.append(frame)
#             timer -= 1
#         return True, frames

class PE_ReadImage(PipelineElement):
    def __init__(self, context):
        context.set_protocol("readimage")
        context.get_implementation("PipelineElement").__init__(self, context)

    def process_frame(self, context, file_path_name):
        _LOGGER.info(f"PE_ReadImage: {context}, read an image")
        image = cv2.imread(file_path_name)
        return True, {"image": image}

# --------------------------------------------------------------------------- #

class PE_Predict(PipelineElement):
    def __init__(self, context):
        context.set_protocol("predict")
        context.get_implementation("PipelineElement").__init__(self, context)

    def process_frame(self, context, image):
        _LOGGER.info(f"PE_Predict: {context}, Model's prediction")
        model.predict(image, show=True)
        cv2.waitKey(0)

        return True, None

# --------------------------------------------------------------------------- #
