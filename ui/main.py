from PyQt5 import uic
from PyQt5.QtWidgets import *

from ui.devices import Devices
from ui.settings import Settings
from bluetoothcontroller import *

class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        uic.loadUi("./ui/main.ui", self)

        self.bluetooth = BluetoothController()

        # UI Tabs
        self.container: QVBoxLayout = self.findChild(QVBoxLayout, "container")
        self.devices: QFrame = Devices(self.bluetooth)
        self.settings: QFrame = Settings()

        self.container.addWidget(self.devices)
        self.container.addWidget(self.settings)

        # setup tab signals
        buttons: [QToolButton] = self.findChildren(QToolButton)
        for btn in buttons:
            btn.clicked.connect(self.onTabClick)

        # Hide tabs not in use
        self.settings.hide()

    def onTabClick(self):
        sender: QToolButton = self.sender()

        self.devices.hide()
        self.settings.hide()

        action = sender.objectName().rstrip("Btn")
        if action == "home":
            self.devices.show()
        elif action == "settings":
            self.settings.show()
        else:
            self.devices.show()