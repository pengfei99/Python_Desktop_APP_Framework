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

- QHBoxLayout : arranges widgets horizontally from left to right
- QVBoxLayout : arranges widgets vertically from top to bottom
- QGridLayout
- QFormLayout