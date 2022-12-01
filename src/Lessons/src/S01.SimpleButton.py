import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# define a slot, it will print message if no message is printed, if there is a message then remove it
def theButtonWasClicked():
    history=msgLabel.text()
    if history:
        msgLabel.setText(f"{history}\nclicked!")
    else:
        msgLabel.setText("clicked!")


# create application
app = QApplication([])

# define main window
window = QWidget()
window.setWindowTitle("My app")

# setup Vertical layout manager
layout = QVBoxLayout()

# create a button
button = QPushButton("Press Me!")


# add button to layout
layout.addWidget(button)

# create a text area and add it to layout
msgLabel = QLabel("")
layout.addWidget(msgLabel)

# add layout to main window
window.setLayout(layout)

# link button clicked signal to slot greet
button.clicked.connect(theButtonWasClicked)

# show application window
window.show()

sys.exit(app.exec())
