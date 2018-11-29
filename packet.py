from struct import pack, unpack
from actions import Actions

def PackInt(number: int) -> [int]:
    return list(pack("i", number))

def UnpackBytes(byteArr: bytes) -> int:
    return unpack('i', byteArr)[0]

class Packet:
    data: [int]
    action: Actions
    position: int

    def __init__(self, action: Actions):
        self.position = 0
        self.action = action
        self.data = bytearray()

        self.add(int(action))

    def __init__(self, data: bytes):
        self.data = list(data)
        self.action = self.get()

    def add(self, number: int):
        self.data.extend(PackInt(number))
        self.position += 4

    def get(self) -> int:
        data = UnpackBytes(self.data[self.position:self.position+4])
        self.position += 4
        return data
