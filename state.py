from enum import Enum, auto

class State(Enum):
    PLAYING = auto()
    PAUSED = auto()
    GAMEOVER = auto()
    MENU = auto()

