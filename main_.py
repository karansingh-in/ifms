import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QLineEdit, QTextEdit, QComboBox, QPushButton, QDateEdit
from PyQt5.QtCore import QDate
from utils.lookup import search
from utils.search import search_
from pages.ic_setup import ICSetup
from pages.main_prompt_screen import MainWindow


    
    
def main():
    app = QApplication([])
    with open("styles/dark.qss", "r") as file:
        app.setStyleSheet(file.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()