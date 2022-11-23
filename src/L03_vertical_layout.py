import sys

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# create application
app = QApplication([])

# set up main widget
window = QWidget()
window.setWindowTitle("QVBoxLayout")

# set up layout manager
layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Bottom"))

window.setLayout(layout)

# Show your application's GUI
window.show()

# Run your application's event loop
sys.exit(app.exec())