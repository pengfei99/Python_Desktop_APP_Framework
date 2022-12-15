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
       a data store which stores the a tuple of values of the todo_app list in the format [(bool, str), (bool, str), (bool, str)]
       where bool is the done state of a given entry, and str is the text of the todo_app.

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
             the data store of the model which is a python list. It stores a tuple of values in the format
             [(bool, str), (bool, str), (bool, str)] where bool is the done state of the task
        kwargs :
        """
        super(TodoModel, self).__init__(*args, **kwargs)
        # This will set self.todos to the provided todos value if it is truthy (i.e. anything other than an empty list,
        # the boolean False or None the default value), otherwise it will be set to the empty list [].
        self.todos = todos or []

    def data(self, index, role):
        """This is the core function of QAbstractListModel, which handles requests for data from the view and
           returns the appropriate result

           If the view asks for display, it returns the text of the todo_app list. If it asks for decoration, it returns
           the status of the todo_app list(e.g. complete, or not)

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
        """
        This method is called by the view to get the number of rows in the current data. This is required
        for the view to know the maximum index it can request from the data store (row count-1). Since we're using
        a Python list as our data store, the return value is the len() of the list.

        Parameters
        ----------
        index : int
              The starting index to start the row count

        Returns
        -------
        int
           The total row count of the data store
        """
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # setupUi is defined in Ui_mainWindow class which create all Widgets
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        # todoView is a QListView which accept a model
        self.todoView.setModel(self.model)
        # link the button with a function
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        Add an item to our todo_app list, getting the text from the QLineEdit .todoEdit
        and then clearing it.

        Returns
        -------
        """
        text = self.todoEdit.text()
        if text: # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            # persist the data to a file
            self.save()

    def delete(self):
        """
        Delete an item to our toto_app list.

        Returns
        -------

        """
        # get the index of the selected task
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    def load(self):
        """
        Read the json file and assign the returned list to the model
        Returns
        -------

        """
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        """
        Write the todo task list into a file
        Returns
        -------

        """
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
