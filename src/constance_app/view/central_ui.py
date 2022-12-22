from PyQt6.QtWidgets import QWidget, QHBoxLayout


class CentralWidget(QWidget):
    def __int__(self):
        super(CentralWidget, self).__int__()
        layout = QHBoxLayout(self)

        self.setLayout(layout)

        # left side widget
        left = QWidget()

        # right side widget
        right = QWidget()

        layout.addWidget(left)
        layout.addWidget(right)
