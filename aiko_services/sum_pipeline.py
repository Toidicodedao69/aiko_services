from typing import Tuple
from aiko_services import aiko, PipelineElement

_LOGGER = aiko.logger(__name__)

class SUM(PipelineElement):
    def __init__(self, context):
        context.set_protocol("Sum-2-numbers") 
        context.get_implementation("PipelineElement").__init__(self, context)
    
    def process_frame(self, context, x, y) -> Tuple[bool, dict]:
        s = int(x) + int(y)
        _LOGGER.info(f"SUM: {context}, The sum of 2 number is: {s}")
        return True, {"sum": s}