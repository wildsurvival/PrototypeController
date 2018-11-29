from PyQt5 import uic
from PyQt5.QtWidgets import *

from ui import resources
from ui.main import Main

import sys, time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(800, 480)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # SHOW SPLASH
        self.splash: QSplashScreen = uic.loadUi("./ui/splash.ui")
        self.splash.show()

        # LOAD UI
        self.ui: QWidget = Main()

        self.splash.finish(self.ui)
        self.setCentralWidget(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

