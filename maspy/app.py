import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from pathlib import Path


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maspy 0.1")
        self.set_program_vars()
        tabs_widget = Tabs(self)
        self.setCentralWidget(tabs_widget)

    def set_program_vars(self):
        self.loaded_tracks = []
        self.loaded_reference = None


class Tabs(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_convert = QWidget()
        self.tab_master = TabMaster(self)
        # self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab_convert, "Convert")
        self.tabs.addTab(self.tab_master, "Master")

        # # Create first tab
        # self.tab_convert.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab_convert.layout.addWidget(self.pushButton1)
        # self.tab_convert.setLayout(self.tab_convert.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class TabMaster(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initlayout()
        self.initUI()

    def initlayout(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

    def initUI(self):
        self.layout.addWidget(InputSection(self))
        self.layout.addWidget(OutputSection(self))


class InputSection(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initlayout()
        self.initUI()

    def initlayout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.box = QGroupBox("Input")
        self.layout.addWidget(self.box)

        self.vbox = QVBoxLayout()
        self.box.setLayout(self.vbox)

    def initUI(self):
        button_load_target = QPushButton("Load tracks")
        button_load_target.setToolTip("Load tracks to master")
        button_load_target.clicked.connect(self.on_load_tracks)

        button_load_reference = QPushButton("Load reference")
        button_load_reference.setToolTip("Load reference track to master")
        button_load_reference.clicked.connect(self.on_load_reference)

        self.vbox.addWidget(button_load_target)
        self.vbox.addWidget(button_load_reference)

    def on_load_tracks(self):
        self.loaded_tracks = []
        home_dir = str(Path.home())
        fnames = QFileDialog.getOpenFileNames(
            self, "Open file", home_dir, filter="*.wav *.mp3 *.m4a *.ogg"
        )
        fnames

    def on_load_reference(self):
        self.loaded_reference = None
        home_dir = str(Path.home())
        fnames = QFileDialog.getOpenFileName(
            self, "Open file", home_dir, filter="*.wav *.mp3 *.m4a *.ogg"
        )
        fnames


class OutputSection(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initlayout()
        self.initUI()

    def initlayout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.box = QGroupBox("Output")
        self.layout.addWidget(self.box)

        self.vbox = QVBoxLayout()
        self.box.setLayout(self.vbox)

    def initUI(self):
        select_output = QComboBox()
        select_output.addItem("Wav")
        select_output.addItem("Mp3")
        select_output.currentIndexChanged.connect(self.on_output_changed)

        self.vbox.addWidget(select_output)

    def on_output_changed(self, index):
        index


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
