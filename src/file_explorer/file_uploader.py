import sys

from functools import partial
from PyQt6.QtCore import Qt,QSize,QFileInfo
from PyQt6 import QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QGridLayout, QListWidgetItem,
                             QLineEdit, QPushButton,
                             QVBoxLayout,QListWidget,QFileDialog
                             )

class ImageListView(QWidget):
    def __init__(self):
        super().__init__()

        self.view = QListWidget()
        self.view.setIconSize(QSize(64, 64))
        bigFont = self.font()
        bigFont.setPointSize(24)
        self.view.setFont(bigFont)

        self.addButton = QPushButton('Add image(s)')

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.addButton)

        self.addButton.clicked.connect(self.addImage)

    def addImage(self):
        paths, _ = QFileDialog.getOpenFileNames(self,
            'Select image(s)', '', 'Images (*.png *.jpg *.jpeg)')

        size = self.view.iconSize()
        for path in paths:
            source = QtGui.QPixmap(path)
            if source.isNull():
                continue

            if source.width() > size.width() or source.height() > size.height():
                source = source.scaled(size, Qt.KeepAspectRatio,
                    Qt.SmoothTransformation)

            # create an empty squared image to keep vertical alignment
            square = QtGui.QPixmap(size)
            square.fill(Qt.transparent)
            qp = QtGui.QPainter(square)
            rect = source.rect()
            rect.moveCenter(square.rect().center())
            qp.drawPixmap(rect, source)
            qp.end()

            name = QFileInfo(path).baseName()
            item = QListWidgetItem(name)
            item.setIcon(QtGui.QIcon(square))
            item.setToolTip(path)
            item.setSizeHint(size)
            self.view.addItem(item)

def main():
    """PyCalc's main function."""
    app = QApplication([])
    pycalcWindow = ImageListView()
    pycalcWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()