import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QLabel, QPushButton, QWidget, QGridLayout
import datetime

class feedback(QMainWindow):
    def __init__(self, parent_window, ic_number, role):
        super().__init__()
        self.setWindowTitle('Feedback')
        self.setGeometry(750, 410, 500, 300)
        self.parent_window = parent_window
        self.ic_number = ic_number
        self.role = role
        self.initUI()    
    
    def initUI(self):
        self.label = QLabel('Please provide a feedback for rejection:')
        self.textbox = QTextEdit()
        self.submitbutton = QPushButton('Submit')
        self.submitbutton.clicked.connect(self.insert_master)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid = QGridLayout()
        
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.textbox, 1, 0)
        grid.addWidget(self.submitbutton, 2, 0)
        
        central_widget.setLayout(grid)

    def insert_master(self):
        conn = sqlite3.connect('ic_master.db')
        cursor = conn.cursor()
        
        self.entry = self.textbox.toPlainText()
        cursor.execute(f'''
                       update ic_pending
                       set feedback = ?,
                       reviewed_by = ?,
                       reviewed_at = ?,
                       request_status = ?
                       where ic_no = ?
                       ''', (self.entry, self.role, datetime.datetime.now(), 'Rejected', self.ic_number,
                             ))
        conn.commit()
        conn.close()
        self.close()
        
    def closeEvent(self, a0):
        self.parent_window.show()
        return super().closeEvent(a0)

        