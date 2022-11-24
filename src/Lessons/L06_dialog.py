import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)


# define a window class by inheriting from QDialog
class Window(QDialog):
    def __init__(self):
        # call the parent constructor
        super().__init__(parent=None)
        self.setWindowTitle("My Dialog Window")
        # first layer layout is Vertical layout
        dialogLayout = QVBoxLayout()
        # second layer layout is form layout
        formLayout = QFormLayout()
        # add rows to form layout
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        # add second layer to first layer
        dialogLayout.addLayout(formLayout)

        # build buttons
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        # add buttons to first layer
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
