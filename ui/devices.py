from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *

DeviceUI, DeviceBase = uic.loadUiType("./ui/device.ui")

class Device(QFrame, DeviceUI):
    clicked = pyqtSignal()

    def __init__(self, name, addr, parent=None):
        super(Device, self).__init__(parent)
        self.setupUi(self)
        self.info = (name, addr)

        addrLabel: QLabel = self.findChild(QLabel, "address")
        nameLabel: QLabel = self.findChild(QLabel, "deviceName")

        addrLabel.setText(addr)
        if name != "" and name != None:
            nameLabel.setText(name)
        else:
            nameLabel.setText("Unknown")

        self.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.clicked.emit()

        return super(Device, self).eventFilter(source, event)


class Devices(QFrame):
    def __init__(self, bluetooth, parent=None):
        super(Devices, self).__init__(parent)
        uic.loadUi("./ui/devices.ui", self)

        self.bluetooth = bluetooth
        self.container: QVBoxLayout = self.findChild(QVBoxLayout, "devicesContainer")
        self.container.setAlignment(Qt.AlignTop)

        self.refreshDevices()

    def refreshDevices(self):
        for i in range(self.container.count()): self.container.itemAt(i).widget().close()

        devices = self.bluetooth.getDevices()

        for addr, name in devices:
            device : Device = Device(name, addr)
            device.clicked.connect(self.onDeviceClick)

            self.container.addWidget(device)

    def onDeviceClick(self):
            sender = self.sender()
            print(sender)