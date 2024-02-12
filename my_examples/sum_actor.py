from aiko_services import *

ACTOR_NAME = "sum"
_LOGGER = aiko.logger(ACTOR_NAME)

class Sum(Actor):
    def __init__(self, context):
        context.get_implementation("Actor").__init__(self, context)
        print(f"MQTT topic: {self.topic_in}")

    def get_logger(self):
        return _LOGGER
    
    def sum(self, x, y):
        s = int(x) + int(y)
        _LOGGER.info(f"The sum of 2 number is: {s}")

if __name__ == "__main__":
    init_args = actor_args(ACTOR_NAME)
    sum = compose_instance(Sum, init_args)
    aiko.process.run()