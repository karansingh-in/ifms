import sys
from PyQt5.QtWidgets import QApplication
from pages.main_prompt_screen import MainWindow
from pages.login import login_screen

def main():
    app = QApplication([])
    with open("styles/dark.qss", "r") as file:
        app.setStyleSheet(file.read())
    window = login_screen()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()