from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt
class message(QMainWindow):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle('Notification')
        self.setGeometry(760,480,350,150)
        self.initUI(text)

    def initUI(self, text):
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        self.okbutton = QPushButton('OK')

        central_widget = QWidget()
        self.setCentralWidget((central_widget))

        grid = QGridLayout()

        grid.addWidget(label, 0, 0)
        grid.addWidget(self.okbutton, 1, 0)
        
        central_widget.setLayout(grid)