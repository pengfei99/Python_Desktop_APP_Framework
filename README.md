# Python_Desktop_APP_Framework

Python provides many frameworks to build desktop with GUI. The following are the most user-friendly and effective 
Python desktop app development frameworks:

- PyQT
- Tkinter
- Kivy
- WxPython
- Bottle
- PyGUI

In this repo, we will use PyQT to make some desktop applications.

## 1. Your first PyQT app

To run a PyQT app, you need to follow the below 5 steps
1. Import QApplication and all the required widgets 
2. Create an instance of QApplication
3. Create your application's GUI
4. Show your application's GUI
5. Run your application's event loop, when user click on close, the application will stop too.

You can find an example in [L01_hello_world.py](src/Lessons/L01_hello_world.py)


## 2. Code Styles of PyQT app

You can notice that `PyQt’s API doesn’t follow PEP 8 coding style` and naming conventions. PyQt is built 
around Qt, which is written in C++ and uses the **camel case** naming style for functions, methods, and variables. 

We will follow the PEP recommendation `where an existing library has a different style, internal consistency is preferred.`
So we will use camel case too in this repo.

## 3. Basics of PyQt

Below elements are the building blocks of any PyQt GUI application. Most of them are represented as `Python classes`
 that live in the `PyQt6.QtWidgets` module:
- Widgets
- Layout managers
- Dialogs
- Main windows
- Applications
- Event loops
- Signals and slots

### 3.1 Widgets

**Widgets are rectangular graphical components that you can place on your application’s windows to build the GUI**. 
Widgets have several attributes and methods that allow you to tweak their appearance and behavior. They can also paint 
a representation of themselves on the screen.

**Widgets also detect mouse clicks, keypresses, and other events from the user**, the window system, and other sources. 
Each time `a widget catches an event, it emits a signal to announce its state change`. PyQt has a rich and modern 
collection of widgets. Some of the most common and useful PyQt widgets are:
- Buttons : You can create a button by instantiating `QPushButton`, a class that provides a classic command button. 
            Typical buttons are Ok, Cancel, Apply, Yes, No, and Close.
- Labels :  you can create with `QLabel`. Labels let you display useful information as `text or images`
- Line edits (input box): It allows you to enter a single line of text. You can create line edits with the `QLineEdit` class
- Combo boxes : You can create them by instantiating `QComboBox`. A combo box will present your user with a dropdown 
                list of options in a way that takes up minimal screen space.
- Radio buttons : You can create with `QRadioButton`. A QRadioButton object is an option button that you can click to 
                switch on.

### 3.2 Layout managers

You need to arrange the widgets so that your GUI is both coherent and functional. If you use methods such as `.resize()` 
, `.resizeEvent()` and `.move()` to give widgets absolute sizes and positions. You will have below major drawbacks:
- Many manual calculations to determine the correct size and position of every widget 
- Extra calculations to respond to window resize events
- Redo most of your calculations when the window’s layout changes in any way

**To avoid all the manual calculations, we need to use Layout managers**. PyQt provides four basic layout manager 
classes:

- QHBoxLayout : arranges widgets horizontally from left to right. code example [L02_horizontal_layout.py](src/Lessons/L02_horizontal_layout.py)
- QVBoxLayout : arranges widgets vertically from top to bottom. code example [L03_vertical_layout.py](src/Lessons/L03_vertical_layout.py)
- QGridLayout : arranges widgets in a `grid of rows and columns`. Every widget will have a `relative position` on the grid. 
                You can define `a widget’s position with a pair of coordinates like (row, column)`. Each coordinate must 
                be an `integer` number. [L04_grid_layout.py](src/Lessons/L04_grid_layout.py)
- QFormLayout : arranges widgets in a **two-column layout**. The first column usually `displays messages in labels`. The
                second column generally `contains widgets like QLineEdit, QComboBox, QSpinBox`, and so on. code example
                [L05_form_layout.py](src/Lessons/L05_form_layout.py).

### 3.3 Dialogs window app

PyQt application can be divided into two categories:

**A main windowstyle application**: The application’s main window inherits from `QMainWindow`.
**A dialog-style application**: The application’s main window inherits from `QDialog`.

A **dialog window** is a stand-alone window that you can use as the main window for your application. `Dialog windows 
are commonly used in main windowstyle applications for brief communication and interaction with the user.`. A dialog
can be
- Modal: Blocks input to any other visible windows in the same application. You can display a modal dialog by calling 
         its `.exec()` method.
- Modeless: Operates independently of other windows in the same application. You can display a modeless dialog 
         by using its `.show()` method.

> A dialog is always an independent window. If a dialog has a parent, then it’ll display centered on top of the parent 
  widget. Dialogs with a parent will share the parent’s task bar entry. If you don’t set parent for a given dialog, 
  then the dialog will get its own entry in the system’s task bar.


A code example can be found in [L06_dialog.py](src/Lessons/L06_dialog.py)

### 3.4 Main window app

Most of the time, your GUI applications will be `main window style apps`. This means that they’ll have a `menu bar, 
some toolbars, a status bar, and a central widget that’ll be the GUI’s main element`. It’s also common for your apps 
to have `several dialogs to accomplish secondary actions` that depend on a user’s input.

**QMainWindow** provides a framework for building your application’s GUI quickly. This class has its own built-in layout, 
which accepts the following graphical components:

| Component                                                                                                        | 	Position on Window       | 	Description                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One [menu bar](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qmenubar.html)                 | 	Top	                     | Holds the application’s main menu                                                                                                                                 |
| One or more [toolbars](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qtoolbar.html)         | 	Sides	                   | Hold [tool buttons](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qtoolbutton.html) and other widgets, such as QComboBox, QSpinBox, and more |
| One central widget	                                                                                              | Center	                   | Holds the window’s central widget, which can be of any type, including a composite widget                                                                         |
| One or more [dock widgets](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qdockwidget.html)	 | Around the central widget | 	Are small, movable, and hidable windows                                                                                                                          |
| One [status bar](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qstatusbar.html)	            | Bottom	                   | Holds the app’s status bar, which shows status information                                                                                                        |

Code example can be found in [L07_main_window.py](src/Lessons/L07_main_window.py)

### 3.5. Applications

`QApplication` is the core component of any PyQt application. It manages the `application’s control flow` and its `main settings`.

**Every PyQt GUI application must have one QApplication instance**. Some responsibilities of this class include:

- Handling the app’s `initialization and finalization`
- Providing the `event loop` and event handling
- Handling most system-wide and application-wide `settings`
- Providing access to `global information`, such as the application’s directory, screen size, and so on
- Parsing common `command-line arguments`
- Defining the application’s `look and feel`
- Providing `localization` capabilities

### 3.6 Event loops

GUI applications are `event-driven`, which means that functions and methods are called in response to user actions (e.g. clicking on a button). 
**Events are handled by an event loop, also known as a main loop, which is an infinite loop**. The event loop continues 
to work until the application is terminated.

**All GUI applications have an event loop**. When an event happens, then the loop checks if it’s a `terminate event`. 
In that case, the loop finishes, and the application exits. Otherwise, the event is sent to the `application’s event 
queue` for further processing, and the loop iterates again. In PyQt6, you can run the app’s event loop by calling 
`.exec() on the QApplication object`.


### Signals and Slots

`PyQt widgets act as event-catchers`. This means that every `widget can catch specific events`, like mouse clicks, 
keypresses, and so on. In response to these events, a `widget emits a signal`, which is a kind of message that 
announces `a change in its state`.

The `signal on its own doesn’t perform any action`. If you want a signal to trigger an action, then you need to 
**connect it to a slot**. This is the function or method that’ll perform an action whenever its associated signal 
is emitted. You can use any `Python callable as a slot`.

If a signal isn’t connected to any slot, then nothing happens and the signal is ignored. Some of the most relevant 
features of signals and slots include the following:

- A signal can be connected to one or many slots.
- A signal may also be connected to another signal.
- A slot may be connected to one or many signals.

You can use the following syntax to connect a signal and a slot:
```python
widget.signal.connect(slot_function)
```

A complete example can be found in [L08_signal_slot.py](src/Lessons/L08_01_signal_slot.py)

In the previous code example, the **slot** does not take arguments. But in real life situation, slot may take one or 
more arguments. We can use two ways to link a slot with arguments to a signal
- functools.partial
- lambda function

You can check the [L08_signal_slot_improved.py](src/Lessons/L08_02_signal_slot_improved.py) for the functools example.

## 4. A real life project

In this section, we will develop a calculator GUI app using the `Model-View-Controller (MVC) design pattern`. This 
pattern has three layers of code, with each one having different roles:

1. The **model** takes care of your app’s business logic. It contains the core functionality and data. In your 
   calculator app, the model will handle the input values and the calculations.

2. The **view** implements your app’s GUI. It hosts all the widgets that the end user would need to interact with 
   the application. The view also receives a user’s actions and events. For this application, the view will be the 
   calculator window on your screen.

3. The **controller** connects the model and the view to make the application work. Users’ events, or requests, are 
   sent to the controller, which puts the model to work. When the model delivers the requested result, or data, in 
   the right format, the controller forwards it to the view. In your calculator app, the controller will receive 
   the target math expressions from the GUI, ask the model to perform calculations, and update the GUI with the result.


Here’s a step-by-step description of how your GUI calculator app will work:

1. The user performs an `action or request (event)` on the view (GUI).
2. The view `notifies the controller` about the user’s action.
3. The controller gets the user’s request and `queries the model` for a response.
4. The model processes the controller’s query, performs the `required computations`, and returns the `result`.
5. The controller receives the model’s response and `updates the view` accordingly.
6. The user finally sees the requested `result on the view`.

###  4.1 Create a view class

### 4.2 Model

### 4.3 Control

## 5. A more complete example

In this example, we will implement a todo list, it consists of a `QListView` for the list of items, a `QLineEdit` to 
enter new items, and a set of buttons to add, delete, or mark items as done.

### 5.1 The UI

We build the UI by using Qt designer. The output is mainwindow.ui. The pyqt can load this file formart directly by
using below code. Or you can convert it to .py file and import the class. For more information, please check section 6.

### 5.2 The Model

We define our custom model (e.g. TodoModel) by subclassing from a base implementation, allowing us to focus on the 
parts unique to our model. Qt provides a number of different model bases, including `lists, trees and tables(ideal 
for spreadsheets).`

For this example we are displaying the result to a `QListView`. The matching base model for this is `QAbstractListModel`.
The outline definition for our model is shown below.

```python
class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the data structure.
            status, text = self.todos[index.row()]
            # Return the todo text only.
            return text

    def rowCount(self, index):
        return len(self.todos)
```

## 6. Qt designer

Qt designer is a good tool, if you have complex UI to develop. You can check this [QT_designer_tutorial.md](QT_designer_tutorial.md) to learn the basic.

## External source

pyqt6 tutorial : https://github.com/janbodnar/PyQt6-Tutorial-Examples
https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/