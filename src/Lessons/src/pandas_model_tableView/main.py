from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableView, QFileDialog, \
    QApplication

import pandas as pd

from table_view_pandas_model import TableViewPandasModel


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)
        vLayout = QVBoxLayout(self)
        hLayout = QHBoxLayout()
        self.pathLE = QLineEdit(self)
        hLayout.addWidget(self.pathLE)
        self.loadBtn = QPushButton("Select File", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.loadFile)
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)")
        self.pathLE.setText(fileName)
        df = pd.read_csv(fileName)
        model = TableViewPandasModel(df)
        self.pandasTv.setModel(model)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())
