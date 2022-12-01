import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget


def theButtonWasClicked():
    label = msgLabel
    history = label.text()
    if history:
        label.setText(f"{history}\nclicked!")
    else:
        label.setText("clicked")

app = QApplication([])
window = QWidget()
window.setWindowTitle("My App")
# setup Vertical layout manager
layout = QVBoxLayout()

# create button widget and add it to layout
button = QPushButton("Press Me!")
layout.addWidget(button)
button.clicked.connect(theButtonWasClicked)

# create a text area and add it to layout
msgLabel = QLabel("")
layout.addWidget(msgLabel)

# Set the main Window layout.

window.setLayout(layout)



window.show()

sys.exit(app.exec())
