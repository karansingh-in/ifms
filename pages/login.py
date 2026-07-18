from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QGridLayout
from PyQt5.QtCore import Qt

class login_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(550, 250, 900, 500)
        self.initUI()
    def initUI(self):
        
        username_label = QLabel('Username :')
        password_label = QLabel('Password :')
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        
        self.username_text.setPlaceholderText('username')
        self.password_text.setPlaceholderText('password')
        self.username_text.setMaximumWidth(580)
        self.password_text.setMaximumWidth(580)
        
        self.password_text.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton('Login')
        self.login_button.setMaximumWidth(100)
        
        self.register_button = QPushButton('New User? Register here.')
        self.register_button.setFlat(True)
        self.register_button.setCursor(Qt.PointingHandCursor)
        
        self.register_button.clicked.connect(self.registration)
        self.register_button.setStyleSheet("""
                    QPushButton {
                        color: #8C8C8C;
                        background-color: #161616;
                    }
                    QPushButton:hover {
                        color: #6bb8ff;
                    }
                    """)
        grid = QGridLayout()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid.addWidget(username_label, 1, 0)
        grid.addWidget(self.username_text, 1, 1)
        grid.addWidget(password_label, 2, 0)
        grid.addWidget(self.password_text, 2, 1)
        grid.addWidget(self.login_button, 3, 1)
        grid.addWidget(self.register_button, 4, 1)
        
        grid.setSpacing(3)
        grid.setContentsMargins(90,90,90,90)
        
        central_widget.setLayout(grid)
        
    def registration(self):
        print('works')
        