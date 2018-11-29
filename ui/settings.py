from PyQt5 import uic
from PyQt5.QtWidgets import *

class Settings(QFrame):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        uic.loadUi("./ui/settings.ui", self)
