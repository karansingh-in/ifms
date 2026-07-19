from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QGridLayout, QComboBox
import datetime
import sqlite3
import bcrypt
class registration_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registration')
        self.setGeometry(550, 250, 900, 500)
        self.initUI()
    def initUI(self):
        
        username_label = QLabel('Username :')
        password_label = QLabel('Password :')
        name_label = QLabel('Full Name :')
        email_label = QLabel('Email :')
        phone_label = QLabel('Phone :')
        role_label = QLabel('Role')
        self.role_dropdown = QComboBox()
        options = ['blank', 'Maker', 'Checker']
        self.role_dropdown.addItems(options)
        self.name_text = QLineEdit()
        self.email_text = QLineEdit()
        self.username_text = QLineEdit()
        self.password_text = QLineEdit()
        self.phone_text = QLineEdit()
        
        
        self.username_text.setPlaceholderText('username')
        self.password_text.setPlaceholderText('password')
        self.name_text.setPlaceholderText('Full name')
        self.email_text.setPlaceholderText('Email-id')
        self.phone_text.setPlaceholderText('Phone')
        self.username_text.setMaximumWidth(580)
        self.password_text.setMaximumWidth(580)
        self.register_button = QPushButton('Register')
        # self.register_button.setMaximumWidth(100)
        self.register_button.clicked.connect(self.insert_user)
        grid = QGridLayout()
        
        grid.addWidget(name_label, 1, 0)
        grid.addWidget(self.name_text, 1, 1)
        grid.addWidget(role_label, 2, 0)
        grid.addWidget(self.role_dropdown, 2, 1)
        grid.addWidget(username_label, 1, 2)
        grid.addWidget(self.username_text, 1, 3)
        grid.addWidget(password_label, 2, 2)
        grid.addWidget(self.password_text, 2, 3)
        grid.addWidget(phone_label, 1, 4)
        grid.addWidget(self.phone_text, 1, 5)
        grid.addWidget(email_label, 2, 4)
        grid.addWidget(self.email_text, 2, 5)
        grid.addWidget(self.register_button, 3, 0)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        
        
        grid.setSpacing(8)
        grid.setContentsMargins(50,50,50,50)
        
        central_widget.setLayout(grid)
        
    def insert_user(self):
        conn = sqlite3.connect('ifms.db')
        cursor = conn.cursor()
        
        encoded_password = self.password_text.text().encode('utf-8')
        hased_password = bcrypt.hashpw(password=encoded_password, salt=bcrypt.gensalt(rounds=12))   
        
        decoded_hash = hased_password.decode('utf-8')     
        
        cursor.execute('''
                       insert into users(
                            username,
                            password_hash,
                            full_name,
                            email,
                            role,
                            created_at,
                            phone_number
                       )VALUES(?,?,?,?,?,?,?)
                       ''', (
                           self.username_text.text(),
                           decoded_hash,
                           self.name_text.text(),
                           self.email_text.text(),
                           self.role_dropdown.currentText(),
                           datetime.datetime.now(),
                           self.phone_text.text()
                           
                       ))
        
        conn.commit()
        conn.close()
    