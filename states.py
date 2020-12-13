from enum import Enum, auto


class State(Enum):
    STARTED = auto()
    STOPPED = auto()


class SubState(Enum):
    LOGIN = auto()
