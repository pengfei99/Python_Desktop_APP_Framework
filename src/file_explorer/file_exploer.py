import sys
from PyQt6.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout, QAbstractItemView
from PyQt6.QtGui import QIcon, QFileSystemModel


class App(QWidget):

    def __init__(self,rootPath):
        super().__init__()
        self.title = 'Explorer files'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI(rootPath)

    def initUI(self,rootPath):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.model = QFileSystemModel()
        self.model.setRootPath(rootPath)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        # hide the size column
        self.tree.hideColumn(1)
        # hide type column
        self.tree.hideColumn(3)
        # hide the creation time
        self.tree.hideColumn(3)
        self.tree.setRootIndex(self.model.index(rootPath))
        self.tree.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.tree.setColumnWidth(0, 150)
        self.tree.setAlternatingRowColors(True)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App("/home/pengfei")
    sys.exit(app.exec())