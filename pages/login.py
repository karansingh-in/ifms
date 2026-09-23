from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QGridLayout
import sqlite3
import bcrypt
from utils.message import message
from pages.dashboard import dashboard

class login_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(600, 300, 810, 450)
        self.initUI()
    def initUI(self):
        
        username_label = QLabel('Username :')
        password_label = QLabel('Password :')
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        show_password_button = QPushButton('👀')
        show_password_button.clicked.connect(self.toggle_password)
        show_password_button.setMaximumWidth(50)
        show_password_button.setStyleSheet('''
                                    QPushButton{
                                        color: #8C8C8C;
                                        background-color: #161616;
                                    }
                                    ''')
        
        self.username_text.setPlaceholderText('username')
        self.password_text.setPlaceholderText('password')
        self.username_text.setMaximumWidth(580)
        self.password_text.setMaximumWidth(580)
        
        self.password_text.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton('Login')
        self.login_button.setMaximumWidth(150)
        self.login_button.clicked.connect(self.check_login)
    
        grid = QGridLayout()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid.addWidget(username_label, 1, 0)
        grid.addWidget(self.username_text, 1, 1)
        grid.addWidget(password_label, 2, 0)
        grid.addWidget(self.password_text, 2, 1)
        grid.addWidget(self.login_button, 3, 1)
        grid.addWidget(show_password_button, 2,2)
        
        grid.setSpacing(14)
        grid.setContentsMargins(90,90,90,90)
        
        central_widget.setLayout(grid)
             
    def toggle_password(self):
        if self.password_text.echoMode() == QLineEdit.Password :
            self.password_text.setEchoMode(QLineEdit.Normal)
        else:
            self.password_text.setEchoMode(QLineEdit.Password)
            
    def check_login(self):
        
        conn = sqlite3.connect('ifms.db')
        cursor = conn.cursor()
        
        cursor.execute('''
                       select password_hash from users where username = ?
                       
                       ''', (self.username_text.text(), ))
        conn.commit()
        
        row = cursor.fetchone()
        
        cursor.execute('''
                       select role from users where username = ?
                       ''', (self.username_text.text(), ))
        
        self.roles = cursor.fetchone()
        self.role = self.roles[0]
        
        entered_password = self.password_text.text()
        entered_password = entered_password.encode('utf-8')
        
        if row is None:
             self.msg = message('The user does not exist')
             self.msg.setWindowTitle('Error!')
             self.msg.show()
             self.close()
        else:
            hased_password = row[0].encode('utf-8')
            if(bcrypt.checkpw(password=entered_password, hashed_password=hased_password)):
                self.main_window = dashboard(user= self.username_text.text(), role=self.role)
                self.main_window.show()
                self.close()
                
                print('works')
                
        conn.close()
        
        
        