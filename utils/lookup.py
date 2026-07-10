import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QWidget, QGridLayout

class search(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lookup')
        self.setGeometry(760, 480, 500, 200)
        self.initUI()

    def initUI(self):
        searchbar = QLineEdit()
        searchbutton = QPushButton('Search')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid = QGridLayout()

        grid.addWidget(searchbar, 0, 0)
        grid.addWidget(searchbutton, 1, 0)

        central_widget.setLayout(grid)

def main():
    app = QApplication([])
    window = search()
    window.show()
    sys.exit(app.exec_())

main()
