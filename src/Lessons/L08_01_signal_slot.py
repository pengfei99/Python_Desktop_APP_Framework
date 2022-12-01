import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# define a slot, it will print message if no message is printed, if there is a message then remove it
def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World!")


# create application
app = QApplication([])

# define main window
window = QWidget()
window.setWindowTitle("Signals and slots")

# setup Vertical layout manager
layout = QVBoxLayout()

# create a button
button = QPushButton("Greet")
# link button clicked signal to slot greet
button.clicked.connect(greet)

# add button to layout
layout.addWidget(button)

# create a text area and add it to layout
msgLabel = QLabel("")
layout.addWidget(msgLabel)

# add layout to main window
window.setLayout(layout)

# show application window
window.show()

sys.exit(app.exec())
