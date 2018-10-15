from enum import Enum

# override
class BaseEnum(Enum):
    def _generate_next_value_(name, start, count, last_value):
        return name
