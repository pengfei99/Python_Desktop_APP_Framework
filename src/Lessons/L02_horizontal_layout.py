import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)
# create app
app = QApplication([])

# add window widget
window = QWidget()
window.setWindowTitle("QHBoxLayout")

# specify the layout manager
layout = QHBoxLayout()

# use layout manager to arrange button
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))

# add layout manager to main window
window.setLayout(layout)

# Show your application's GUI
window.show()

# Run your application's event loop
sys.exit(app.exec())