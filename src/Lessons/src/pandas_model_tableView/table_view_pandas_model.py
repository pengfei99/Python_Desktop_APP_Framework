from PyQt6.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex

import pandas as pd


class TableViewPandasModel(QAbstractTableModel):
    """
    This class allows user to build a model for QTableView from a pandas dataframe.
    """

    def __init__(self, df: pd.DataFrame = pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """ Override method from QAbstractTableModel. Return dataframe index as vertical header data and
        columns as horizontal header data.

        Parameters
        ----------
        section : index to select a sub set of the data frame
        orientation : table view orientation
        role : Display role of the table view

        Returns  dataframe index as vertical header data and columns as horizontal header data.
        -------

        """
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()

        if orientation == Qt.Orientation.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError,):
                return QVariant()
        elif orientation == Qt.Orientation.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError,):
                return QVariant()

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """

        Parameters
        ----------
        index
        role

        Returns
        -------

        """
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()

        if not index.isValid():
            return QVariant()

        return QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QModelIndex()):
        """ Override method from QAbstractTableModel. Return row count of the pandas DataFrame
        Parameters
        ----------
        parent

        Returns row count of the pandas DataFrame
        -------

        """
        if parent == QModelIndex():
            return len(self._df.index)
        else:
            return 0

    def columnCount(self, parent=QModelIndex()):
        """ Override method from QAbstractTableModel. Return column count of the pandas DataFrame
        Parameters
        ----------
        parent

        Returns column count of the pandas DataFrame
        -------

        """
        if parent == QModelIndex():
            return len(self._df.columns)
        else:
            return 0

    def sort(self, column, order):
        """ This method sort the dataframe with a given column name and an order. It will update the table
        view after the sort.

        Parameters
        ----------
        column (str): Column name that will be used as the sort index column
        order (PyQt6.QtCore.Qt.SortOrder.AscendingOrder): Sorting order (e.g. Descending, Ascending)

        Returns
        -------

        """
        # get column name that needs to be sorted
        colName = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        # call pandas df sort method to sort the rows
        self._df.sort_values(colName, ascending=order == Qt.SortOrder.AscendingOrder, inplace=True)
        # reset index after sorting
        self._df.reset_index(inplace=True, drop=True)
        # update table view
        self.layoutChanged.emit()
