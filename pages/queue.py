import sqlite3
from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem, QLabel, QGridLayout, QWidget, QDateEdit
from utils.pending import pending_queue
from utils.rejections import rejection_queue

class Queue(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()
        self.approved_button = QPushButton('Approved')
        self.history_button = QPushButton('History')
        self.pending_button = QPushButton('Pending')
        self.rejected_button = QPushButton('Rejected')
        self.rejected_button.setStyleSheet('background-color: #9C2007;')
        self.label = QLabel('The list is below :')
        self.filter_by_date = QDateEdit()
        self.list_widget = QListWidget()
        
        grid.addWidget(self.pending_button,   0, 0)
        grid.addWidget(self.rejected_button,  0, 1)
        grid.addWidget(self.approved_button,  0, 2)
        grid.addWidget(self.history_button,   0, 3)
        grid.addWidget(self.filter_by_date,   0, 4)

        grid.addWidget(self.label,            1, 0, 1, 5)
        grid.addWidget(self.list_widget,      2, 0, 1, 5)
        
        grid.setRowStretch(2, 1)
        grid.setColumnStretch(4, 1)
        
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(10)
        
        self.pending_button.setMinimumHeight(35)
        self.rejected_button.setMinimumHeight(35)
        self.approved_button.setMinimumHeight(35)
        self.history_button.setMinimumHeight(35)
        
        grid.setContentsMargins(200,200,200,200)
        self.setLayout(grid)
        
    
        
    
        
        
        
        