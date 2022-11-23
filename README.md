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

You can find an example in [L01_hello_world.py](./src/L01_hello_world.py)


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

- QHBoxLayout : arranges widgets horizontally from left to right. code example [L02_horizontal_layout.py](src/L02_horizontal_layout.py)
- QVBoxLayout : arranges widgets vertically from top to bottom. code example [L03_vertical_layout.py](src/L03_vertical_layout.py)
- QGridLayout : arranges widgets in a `grid of rows and columns`. Every widget will have a `relative position` on the grid. 
                You can define `a widget’s position with a pair of coordinates like (row, column)`. Each coordinate must 
                be an `integer` number. [L04_grid_layout.py](src/L04_grid_layout.py)
- QFormLayout : arranges widgets in a **two-column layout**. The first column usually `displays messages in labels`. The
                second column generally `contains widgets like QLineEdit, QComboBox, QSpinBox`, and so on. code example
                [L05_form_layout.py](src/L05_form_layout.py).

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


A code example can be found in [L06_dialog.py](./src/L06_dialog.py)

### 3.4 Main window app

Most of the time, your GUI applications will be `main window style apps`. This means that they’ll have a `menu bar, 
some toolbars, a status bar, and a central widget that’ll be the GUI’s main element`. It’s also common for your apps 
to have `several dialogs to accomplish secondary actions` that depend on a user’s input.

**QMainWindow** provides a framework for building your application’s GUI quickly. This class has its own built-in layout, 
which accepts the following graphical components:

| Component                                                                                        | 	Position on Window | 	Description                      |
|--------------------------------------------------------------------------------------------------|---------------------|-----------------------------------|
| One [menu bar](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qmenubar.html) | 	Top	               | Holds the application’s main menu |
One or more toolbars	Sides	Hold tool buttons and other widgets, such as QComboBox, QSpinBox, and more
One central widget	Center	Holds the window’s central widget, which can be of any type, including a composite widget
One or more dock widgets	Around the central widget	Are small, movable, and hidable windows
One status bar	Bottom	Holds the app’s status bar, which shows status information