from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
import sqlite3
import datetime

class dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IFMS')
        self.showMaximized()
        self.initUI()
        
    def initUI(self):
        ifms_label = QLabel('IFMS')
        username_label = QLabel()
        time_label = QLabel()
        home_button = QPushButton('Home')
        audit_button = QPushButton('Audit')
        ic_button = QPushButton('IC')
        trust_button = QPushButton('Trust')
        journal_button = QPushButton('Journal')
        report_button = QPushButton('Report')
        queue_button = QPushButton('Queue')
        logout_button = QPushButton('Logout')
        work_area = QStackedWidget()
        
        grid = QGridLayout()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid.addWidget(ifms_label, 0, 0)
        grid.addWidget(username_label, 0, 4)
        grid.addWidget(time_label, 0, 5)
        grid.addWidget(logout_button, 0, 6)
        grid.addWidget(home_button, 1, 0)
        grid.addWidget(ic_button, 1, 1)
        grid.addWidget(trust_button, 1, 2)
        grid.addWidget(journal_button, 1, 3)
        grid.addWidget(audit_button, 1, 4)
        grid.addWidget(report_button, 1, 5)
        grid.addWidget(queue_button, 1, 6)
        grid.addWidget(work_area, 2, 0)
        
        
        



