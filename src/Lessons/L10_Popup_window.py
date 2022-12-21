import sys

from PyQt6.QtCore import QRect
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication


class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class MainWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.btn1 = QPushButton("Click me", self.cw)
        self.btn1.setGeometry(QRect(0, 0, 100, 30))
        self.btn1.clicked.connect(self.doit)
        self.w = None

    def doit(self):
        print("Opening a new popup window...")
        self.w = MyPopup()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()


class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.main.show()


def main(args):
    global app
    app = App(args)
    sys.exit(app.exec())


if __name__ == "__main__":
    main(sys.argv)
