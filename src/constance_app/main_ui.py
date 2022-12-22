import sys, pathlib
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QStatusBar
from PyQt6.QtGui import QIcon, QAction
from view.central_ui import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # basic setup
        iconPath = pathlib.Path.cwd() / 'resources'
        self.setWindowTitle('DataValidator')
        self.setWindowIcon(QIcon(str(iconPath / 'casd_favicon.png')))
        self.setGeometry(100, 100, 1024, 768)

        # set up centralWidget
        self.centralWidget = CentralWidget(self)
        self.setCentralWidget(self.centralWidget)

    def init_ui(self,iconPath):
        # Menu bar setup
        menuBar = self.menuBar()

        # Add three menu
        fileMenu = menuBar.addMenu('&File')
        editMenu = menuBar.addMenu('&Edit')
        helpMenu = menuBar.addMenu('&Help')

        # Add three action to file_menu
        fileMenu.addAction('New Etude', lambda: print('New'))
        fileMenu.addAction('Open', lambda: print('Open'))
        fileMenu.addAction('Exit', self.destroy)

        # Add two action to edit_menu
        undo_action = QAction(QIcon(str(iconPath / 'undo.png')), 'Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        # link to the textEdit slot undo (provided by Qt)

        editMenu.addAction(undo_action)

        redo_action = QAction(QIcon(str(iconPath / 'redo.png')), 'Redo', self)
        redo_action.setShortcut('Ctrl+Y')

        editMenu.addAction(redo_action)

        # Create a toolbar and add it to the MainWindow
        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        # add action to toolbar
        toolbar.addAction(undo_action)
        toolbar.addAction(redo_action)

        # setup a status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Awesome data validator v0.1.0')

        self.show()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
