from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ChildWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Child Window")
        self.setModal(True)  # Set the dialog as modal
        self.resize(300, 200)

        # Add a label and close button
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is a modal dialog"))
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(600, 400)

        # Add a button to open the child window
        open_button = QPushButton("Open Child Window", self)
        open_button.clicked.connect(self.open_child_window)
        open_button.resize(200, 50)
        open_button.move(200, 175)

    def open_child_window(self):
        child = ChildWindow()
        child.exec_()  # Open the dialog modally

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
