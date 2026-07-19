import sqlite3
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QWidget, QGridLayout, QListWidget, QListWidgetItem
from utils.message import message

class search(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.setWindowTitle('Lookup')
        self.setGeometry(660, 380, 700, 450)
        self.parent_window = parent_window
        self.initUI()

    def initUI(self):
        self.searchbar = QLineEdit()
        self.searchbar.setPlaceholderText('Enter the  IC Name')
        searchbutton = QPushButton('Search')
        searchbutton.clicked.connect(self.see)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid = QGridLayout()
        
        self.listwidget = QListWidget()

        grid.addWidget(self.searchbar, 0, 0)
        grid.addWidget(searchbutton, 1, 0)
        grid.addWidget(self.listwidget, 2, 0)
        
        central_widget.setLayout(grid)
        self.listwidget.itemActivated.connect(self.select_ic)

    def select_ic(self, item):
        index_of_separation = item.text().index('-')
        ic_number = item.text()[:index_of_separation - 1]
        self.parent_window.searchbar.setText(ic_number)
        self.parent_window.show()
        self.close()
        

    def closeEvent(self, a0):
        self.parent_window.show()
        return super().closeEvent(a0)

    def back(self):
        self.parent_window.show()
        self.close()

    def see(self):
        entry = self.searchbar.text()
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
                       select ic_no, ic_name from ic_master where ic_name like ?

                        ''', ('%' + entry + '%', ))
        
        row = cursor.fetchall()
        
        for opt in row:
            
            item = QListWidgetItem(f'{opt['ic_no']} - {opt['ic_name']}')
            self.listwidget.addItem(item)
        
        if row is None:
            self.msg = message('Entry not found')
            self.msg.show()
            
            self.close()
        
        