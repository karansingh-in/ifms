from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QWidget, QLabel, QGridLayout
import sys



class message(QMainWindow):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle('Notification')
        self.setGeometry(760,480,450,150)
        self.initUI(text)

    def initUI(self, text):
        label = QLabel(text)
        okbutton = QPushButton('OK')

        central_widget = QWidget()
        self.setCentralWidget((central_widget))

        grid = QGridLayout()

        grid.addWidget(label, 0, 0)
        grid.addWidget(okbutton, 1, 0)
        
        central_widget.setLayout(grid)

def main():
    app = QApplication([])
    window = message('wetfguijjiugfdresrtghj')
    window.show()
    sys.exit(app.exec_())

main()
        






        
        
        
        