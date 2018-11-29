from enum import Enum

class Actions(Enum):
    Initialize = 0,
    Keyboard = 1

    def __new__(cls, value):
        member = object.__new__(cls)
        member._value_ = value
        return member

    def __int__(self):
        return self.value