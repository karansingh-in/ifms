import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QLineEdit, QTextEdit, QComboBox, QPushButton, QDateEdit
from PyQt5.QtCore import QDate
import sqlite3
from pages.ic_setup import ICSetup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IC Master")
        self.setGeometry(550, 250, 900, 500)
        self.initUI()
                
    def initUI(self):
        self.setStyleSheet(""" 
                           QLabel {
                               width: 200px;
                               height: 100px;
                               font-size: 20px;
                               font: arial;     
                           }
                           
                           QLabel#header {
                               width: 10px;
                               height: 10px;
                               font-size: 20px;
                               font-family: Arial;
                               color: white;
                               background-color: blue;
                           }
                           
                           QComboBox {                         
                               font-size: 20px;
                               font-family: Arial;
                           }
                           """)

        label = QLabel("IC Master Set up - prompt", self)
        label.setObjectName("header")
        label.setFixedHeight(30)
        
        label1 = QLabel("Date of creation", self)
        
        label2 = QLabel("Master Data Type", self)

        label3 = QLabel("Function", self)
        
        self.dropdown1 = QComboBox(self)
        options = ['I: IC Master setup', 'T: Trust Master setup']
        self.dropdown1.addItems(options)
        
        self.dropdown2 = QComboBox(self)
        options2 = ['C: Create', 'A: Ammend', 'E:Enquiry']
        self.dropdown2.addItems(options2)
        
        dateEdit = QDateEdit()
        dateEdit.setDate(QDate.currentDate())
        
        SubmitButton = QPushButton('Submit')
        CancelButton = QPushButton('Cancel')
        SubmitButton.clicked.connect(self.open_icsetup)
        lookupbutton = QPushButton('Lookup')
        self.searchbar = QLineEdit()
        # searchbutton = QPushButton('Search')
        # searchbutton.clicked.connect(self.search)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid = QGridLayout()
        
        grid.addWidget(label, 0, 0)
        grid.addWidget(label1, 1, 0)
        grid.addWidget(label2, 2, 0)
        grid.addWidget(label3, 3, 0)
        grid.addWidget(dateEdit, 1, 1)
        grid.addWidget(self.dropdown1, 2, 1)
        grid.addWidget(self.dropdown2, 3, 1)
        grid.addWidget(SubmitButton, 4, 1)
        grid.addWidget(CancelButton, 4, 2)
        grid.addWidget(self.searchbar, 5, 2)
        grid.addWidget(lookupbutton, 5, 3)
        
        central_widget.setLayout(grid)
        
    def open_icsetup(self):
       # master_type = self.dropdown1.currentText()
        function_selection =  self.dropdown2.currentText()
        
        self.ic_window = ICSetup(function_selection)
        self.ic_window.show()
        
        self.close()
            
    def search(self):
        number = self.searchbar.text()
        self.lookup(number)
        self.lookup.show()

        self.close()
    
    def lookup(self, number):
        conn = sqlite3.connect('ic_master.db')
        cursor = conn.cursor()
        
        cursor.execute(f'''
                       select * from ic_master where id={number}
                       ''')
        
        row = cursor.fetchone()
        print(row)
    
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()