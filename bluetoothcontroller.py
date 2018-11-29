from bluetooth import *
from threading import Thread

from actions import Actions
from packet import *

class BluetoothController:
    def __init__(self):
        self.sock : BluetoothSocket = BluetoothSocket(RFCOMM)
        self.thread : Thread = None

    def getDevices(self):
        return discover_devices(lookup_names=True)

    def Connect(self, addrport):
        self.sock.connect(addrport)
        self.thread = Thread(target= self._read)
        self.thread.start()

    def Close(self):
        self.sock.close()
        self.thread.close()

    def _readPacket(self):
        length = self.sock.recv(4)
        total : int = 0
        currentLength: int = 0
        data = bytes

        if (len(length) == 0):
            return

        length = UnpackBytes(length)

        if (length < 2):
            return

        while (currentLength != length):
            data = self.sock.recv(length)

            if (len(data) == 0):
                return

            currentLength += len(data)

        return Packet(data)

    def _read(self):
        try:
            while True:
                packet = self._readPacket()
                print(packet.data)
        except IOError:
            pass

    def Send(self, packet: Packet):
        data = packet.data
        length = PackInt(len(data))

        self.sock.send(bytearray(length.extend(data)))