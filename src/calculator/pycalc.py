import sys

from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QGridLayout,
                             QLineEdit, QPushButton,
                             QVBoxLayout,
                             )

# constant for window size
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

ERROR_MSG = "ERROR"


# The main window class extends QMainWindow
class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pengfei's pyqt calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        # add general layout
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        # set central widget to use general layout
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        # add the display line
        self._createDisplay()
        self._createButtons()

    # for better code modularity, we create a method for each component on the central widget
    # this is the lineEdit that will print the user input and calculation result
    def _createDisplay(self):
        # create an qlineEdit() widget
        self.display = QLineEdit()
        # set up height, alignment, and readonly
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        # add it to layout
        self.generalLayout.addWidget(self.display)

    # This method create buttons for the calculator
    def _createButtons(self):
        self.buttonMap = {}
        # create a second layer layout for buttons
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                # add buttons widget on the second layer
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        # add the second layer on the first layer
        self.generalLayout.addLayout(buttonsLayout)

    # functions to print text on display line, a plot
    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    # functions to get text on display line
    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    # functions to clear text on display line
    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")


class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()
