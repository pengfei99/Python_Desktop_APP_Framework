import sys, pathlib
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QStatusBar, QMessageBox, QLabel
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

        # create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # populate ui
        self.init_ui(iconPath)

    def init_ui(self, iconPath):
        # Menu bar setup
        menuBar = self.menuBar()

        # Add three menu
        fileMenu = menuBar.addMenu('&File')
        editMenu = menuBar.addMenu('&Edit')
        helpMenu = menuBar.addMenu('&Help')

        # define actions for fileMenu
        # create study action
        newStudyAction = QAction(QIcon("/new_study.png"), 'New &Study', self)
        newStudyAction.setStatusTip('Create a new Study')
        newStudyAction.setShortcut("Ctrl+F1")
        newStudyAction.triggered.connect(self.createStudy)

        # create extraction action
        newExtractionAction = QAction(QIcon("/new_extraction.png"), 'New &Extraction', self)
        newExtractionAction.setStatusTip('Create a new Extraction')
        newExtractionAction.setShortcut("Ctrl+F2")
        newExtractionAction.triggered.connect(self.createExtraction)

        # create dataset action
        newDsAction = QAction(QIcon("/new_dataset.png"), 'New &Dataset', self)
        newDsAction.setStatusTip('Create a new Dataset')
        newDsAction.setShortcut("Ctrl+F3")
        newDsAction.triggered.connect(self.createDataset)

        # exit action
        exitAction = QAction(QIcon('./assets/exit.png'), '&Exit', self)
        exitAction.setStatusTip('Exit')
        exitAction.setShortcut('Alt+F4')
        exitAction.triggered.connect(self.quit)

        # Add three action to file_menu
        fileMenu.addAction(newStudyAction)
        fileMenu.addAction(newExtractionAction)
        fileMenu.addAction(newDsAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        # editMenu.addAction()
        # editMenu.addAction(redo_action)

        # Create a toolbar and add it to the MainWindow
        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        # add action to toolbar
        toolbar.addAction(newStudyAction)
        toolbar.addAction(newExtractionAction)
        toolbar.addAction(newDsAction)

        # setup a status bar
        self.toolVersion=QLabel('Awesome data validator v0.1.0')
        self.status_bar.addWidget(self.toolVersion)

        self.show()

    def createStudy(self):
        pass

    def createExtraction(self):
        pass

    def createDataset(self):
        pass

    def quit(self):
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to quit?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.destroy()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
