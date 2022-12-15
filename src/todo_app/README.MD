# Todo app

In this project, we will build a little app that can stores a todo list, when a task is done
user can mark the event as done. User can also add and remove task in the todo list.


## 1. PyQT design pattern

The main objective is to illustrate the design pattern of PyQt:

### 1.1 MVC
- **Model**: holds the data structure which the app is working with.
- **View**: is any representation of information as shown to the user, whether graphical or tables. 
            Multiple views of the same data model are allowed.
- **Controller**: accepts input from the user, transforming it into commands to for the model or view.

> In `Qt/PyQt land` the distinction between the View & Controller gets a little murky. Qt accepts input events from 
the user (via the OS) and delegates these to the widgets (Controller) to handle. However, widgets also handle 
presentation of the current state to the user, putting them squarely in the View. Rather than agonize over where to 
draw the line, in Qt-speak the View and Controller are instead merged together creating a **Model/ViewController 
architecture  called "Model View" for simplicity’s sake**.


### 1.2 The Model View pattern

The Model acts as the interface between the data store and the ViewController. The Model holds the data 
(or a reference to it) and presents this data through a `standardised API` which Views then consume and present 
to the user. Multiple Views can share the same data, presenting it in completely different ways.


- **Model**: stores the data, or a reference to it and returns individual or ranges of records, and associated 
             metadata or display instructions. Model can use any `data store` (e.g. python list, dict, DB via sqlAlchemy)
- **View**: requests data from the model and displays what is returned on the widget.

## 2. The app UI

The app UI is created by using Qt designer. The generated UI source is [mainwindow.ui](./mainwindow.ui). To make it more
robust, we convert the .ui to .py by using below command

```shell
pyuic6 -o mainWindowUI.py main_window_ui
```

For more information about Qt designer, please visit [QT_designer_tutorial.md](../../QT_designer_tutorial.md)

## 3. The app model

We define our `custom model by subclassing from a base implementation`, allowing us to focus on the parts unique to 
our model. Qt provides a number of different model bases:
- lists
- trees
- tables (ideal for spreadsheets).

For this application, we are displaying the result to a **QListView**. The matching base model for this is 
**QAbstractListModel**. 

> You should always choose the base model based on how you want to display the data (View).

Below is an example of the todo list data model. You need to pay attention on 
- .data(index,role): handles requests for data from the `view` and returns the appropriate result
- .rowCount(): returns the number of rows in the current data store

The **role** in data() method indicates which type of data the view is requesting. In our code we handled **DisplayRole**
and **DecorationRole**. There are many other roles which the data can receive, below is a full list.

| Role                           | 	Value | 	Description                                                                               |
|--------------------------------|--------|--------------------------------------------------------------------------------------------|
| Qt.ItemDataRole.DisplayRole    | 	0	    | The key data to be rendered in the form of text. (QString)                                 |
| Qt.ItemDataRole.DecorationRole | 	1	    | The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap) |
| Qt.ItemDataRole.EditRole       | 	2	    | The data in a form suitable for editing in an editor. (QString)                            |
| Qt.ItemDataRole.ToolTipRole    | 	3	    | The data displayed in the item's tooltip. (QString)                                        |
| Qt.ItemDataRole.StatusTipRole  | 	4	    | The data displayed in the status bar. (QString)                                            |
| Qt.ItemDataRole.WhatsThisRole  | 	5	    | The data displayed for the item in "What's This?" mode. (QString)                          |
| Qt.ItemDataRole.SizeHintRole   | 	13	   | The size hint for the item that will be supplied to views. (QSize)                         |



```python
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
           The total row count in the current data store
        """
        return len(self.todos)
```
## 4. The app View/Controller








