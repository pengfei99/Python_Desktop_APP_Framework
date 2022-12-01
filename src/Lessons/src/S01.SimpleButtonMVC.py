import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget


# control class
class Controller:
    def __init__(self, view, model=None):
        self._view = view
        self._model = model
        self._connectSignalsAndSlots()

    def _theButtonWasClicked(self):
        label = self._view.msgLabel
        history = label.text()
        if history:
            label.setText(f"{history}\nclicked!")
        else:
            label.setText("clicked")

    def _connectSignalsAndSlots(self):
        self._view.button.clicked.connect(self._theButtonWasClicked)


# view class
class MainView(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # setup Vertical layout manager
        layout = QVBoxLayout()

        # create button widget and add it to layout
        self.button = QPushButton("Press Me!")
        layout.addWidget(self.button)

        # create a text area and add it to layout
        self.msgLabel = QLabel("")
        layout.addWidget(self.msgLabel)

        # Set the main Window layout.

        self.setLayout(layout)


app = QApplication([])
mainView = MainView()
mainView.show()
Controller(view=mainView)
sys.exit(app.exec())
