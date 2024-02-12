import cv2, pickle, time, copy
from threading import Thread
from typing import Tuple

from ultralytics import YOLO

from aiko_services import aiko, PipelineElement

_LOGGER = aiko.logger(__name__)

model = YOLO("yolov8n.pt")

# --------------------------------------------------------------------------- #

class PE_ReadVideo(PipelineElement):
    def __init__(self, context):
        context.set_protocol("ReadVideo")
        context.get_implementation("PipelineElement").__init__(self, context)

    def process_frame(self, context, frame) -> Tuple[bool, dict]:
        time_now = time.time()
        _LOGGER.info(f"PE_ReadVideo: {context}, {time_now:0.3f}")

        return True, {"frame": frame}
    
    def _run(self, context, video):
        frame_id = 0

        while not context["terminate"]:
            frame_context = copy.deepcopy(context)
            frame_context["frame_id"] = frame_id

            success, frame = video.read()
            self.create_frame(frame_context, {"frame": frame})
            frame_id += 1

    def start_stream(self, context, stream_id) -> Tuple[bool, dict]:
        context["terminate"] = False
        video = cv2.VideoCapture(0)
        Thread(target=self._run, args=(context, video, )).start()

    def stop_stream(self, context, stream_id):
        context["terminate"] = True

# --------------------------------------------------------------------------- #

class PE_Predict(PipelineElement):
    def __init__(self, context):
        context.set_protocol("predict")
        context.get_implementation("PipelineElement").__init__(self, context)

    def process_frame(self, context, frame):
        time_now = time.time()
        #_LOGGER.info(f"PE_Predict: {context}, Model's prediction")
        _LOGGER.info(f"PE_Predict: {context}, {time_now:0.3f}")
        time_now = time.time()
        _LOGGER.info(f"PE_Predict: {context}, {time_now:0.3f}")
        model.predict(source=frame, show=True)

        return True, {}

# --------------------------------------------------------------------------- #