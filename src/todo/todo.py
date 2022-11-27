import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt

# import the generated UI
from mainWindowUI import Ui_MainWindow

# load ui from .ui source, can have performance issues when UI is complex
# qt_creator_file = "mainwindow.ui"
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage('tick.png')


class TodoModel(QtCore.QAbstractListModel):
    """
    A model class that connects data source with the view

    '''
    Attributes
    ----------
    todos: List
       a data store which stores the a tuple of values of the todo list in the format [(bool, str), (bool, str), (bool, str)]
       where bool is the done state of a given entry, and str is the text of the todo.

    Methods
    -------
    data(index,role)
         It handles requests for data from the view and returns the appropriate result.
    rowCount(index)
        It is called by the view to get the number of rows in the current data
    """

    def __init__(self, *args, todos=None, **kwargs):
        """
        Parameters
        ----------
        args :
        todos : List
             a data store which stores the a tuple of values of the todo list
        kwargs :
        """
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        """This is the core function of QAbstractListModel, which handles requests for data from the view and
           returns the appropriate result

           If the view asks for display, it returns the text of the todo list. If it asks for decoration, it returns
           the status of the todo list(e.g. complete, or not)

        Parameters
        ----------
        index : QModelIndex
           is the position/coordinates of the data which the view is requesting, accessible by two methods
           .row() and .column() which give the position in each dimension.
        role : int
           is a flag indicating the type of data the view is requesting. This is because the .data() method actually
           has more responsibility than just the core data. It also handles requests for style information, tooltips,
           status bars, etc.  basically anything that could be informed by the data itself.
           The naming of Qt.ItemDataRole.DisplayRole is a bit weird, but this indicates that the view is asking us
           "please give me data for display". There are other roles which the data can receive for styling requests
           or requesting data in "edit-ready" format.

        Returns
        -------

        """
        if role == Qt.ItemDataRole.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


class todoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connectSignalAndSlot()

    def _add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.view.todoEdit.text()
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.view.todoEdit.setText("")
            self._save()

    def _delete(self):
        indexes = self.view.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.view.todoView.clearSelection()
            self._save()

    def _complete(self):
        indexes = self.view.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.view.todoView.clearSelection()
            self._save()

    def _load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def _save(self):
        with open('data.db', 'w') as f:
            json.dump(self.model.todos, f)

    def connectSignalAndSlot(self):
        self._load()
        self.view.todoView.setModel(self.model)
        self.view.addButton.pressed.connect(self._add)
        self.view.deleteButton.pressed.connect(self._delete)
        self.view.completeButton.pressed.connect(self._complete)


app = QtWidgets.QApplication(sys.argv)
todoView = MainWindow()
todoView.show()
todoModel = TodoModel()
todoController(todoModel, todoView)
app.exec()
