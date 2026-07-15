import sqlite3
from PyQt5.QtWidgets import QMainWindow, QListWidget, QWidget, QLabel, QListWidgetItem, QGridLayout
from utils.message import message

class rejection_queue(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.setWindowTitle('Pending Queue')
        self.setGeometry(660, 380, 700, 450)
        self.parent_window = parent_window
        self.initUI()
        
    def initUI(self):
        
        conn = sqlite3.connect('ic_master.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
                       select request_status, request_id, ic_no, ic_name, action, submitted_by, submitted_at from ic_pending
                       ''')

        self.queue = cursor.fetchall()
        
        self.listwidget = QListWidget()
        
        for q in self.queue:
            if q['request_status'] == 'Rejected':
                item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
                self.listwidget.addItem(item)
        
        self.grid = QGridLayout()
        
        self.label = QLabel('The rejected requests are: ')
        
        self.grid.addWidget(self.label, 0, 0)
        self.grid.addWidget(self.listwidget, 1, 0)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.central_widget.setLayout(self.grid)
            
        item = self.listwidget.itemActivated.connect(self.show_feedback)                 
    
    def show_feedback(self, item):
        index_of_separation = item.text().rfind('-')
        self.function = item.text()[index_of_separation + 1:]
        
        conn = sqlite3.connect('ic_master.db')

        self.index_of_first_dash = item.text().index('-')
        self.index_of_separation_second_dash = item.text().index('-', self.index_of_first_dash + 1)
        self.ic_number = item.text()[self.index_of_first_dash + 2:self.index_of_separation_second_dash - 1]
        self.ic_number = int(self.ic_number)
        
        cursor = conn.cursor()
        
        cursor.execute('''
                       select feedback from ic_pending where ic_no = ?                       
                       ''', (self.ic_number,))
        
        self.feedback_text = cursor.fetchone()["feedback"]
        msg = message(text=self.feedback_text)
        self.parent_window.show()
        msg.show()
        self.close()
        
        