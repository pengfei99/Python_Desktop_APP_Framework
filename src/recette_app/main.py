import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import pandas as pd
from DataReader import read_csv, read_sas, read_json, read_parquet, read_file
# from mainWindowUI import


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, filePath):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = read_file(filePath)

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

    def resetTableModel(self,filePath):
        self.model=TableModel(read_file(filePath))
        self.table.reset()
        self.table.setModel(self.model)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow("../../data/airline.csv")
window.show()
app.exec()
