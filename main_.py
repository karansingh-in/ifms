import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QLineEdit, QTextEdit, QComboBox, QPushButton, QDateEdit
from PyQt5.QtCore import QDate
from utils.lookup import search
from utils.search import search_
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
                               background-color: #0A84FF;
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
        
        self.searchbar = QLineEdit()
        self.searchbar.setMaximumWidth(280)
        self.searchbar.setPlaceholderText('Enter IC Number')
        
        self.SubmitButton = QPushButton('Submit')
        self.CancelButton = QPushButton('Cancel')
        self.lookupbutton = QPushButton('Lookup')
        self.lookupbutton.hide()
        self.searchbar.hide()
        self.lookupbutton.clicked.connect(self.lookup)
        
        self.dropdown2.currentTextChanged.connect(self.show_search)
        
        
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
        grid.addWidget(self.searchbar, 4, 1)
        grid.addWidget(self.SubmitButton, 5, 1)
        grid.addWidget(self.CancelButton, 5, 2)
        grid.addWidget(self.lookupbutton, 5, 3)
        
        central_widget.setLayout(grid)
            
    def show_search(self):
        function_selection = self.dropdown2.currentText()
        if function_selection != 'C: Create':
            self.lookupbutton.show()
            self.searchbar.show()
            entry = self.searchbar.text()
            self.SubmitButton.clicked.connect(self.searching)
        if function_selection == 'C: Create':
            self.lookupbutton.hide()
            self.searchbar.hide()
            self.SubmitButton.clicked.connect(self.open_icsetup)
        
    def searching(self):
        function_selection = self.dropdown2.currentText() 
        entry = self.searchbar.text()
        self.search_ic = search_(entry=entry,function=function_selection)
        self.close()
    
    def open_icsetup(self):
        function_selection = self.dropdown2.currentText() 
        
        self.ic_window = ICSetup(function_selection)
        self.ic_window.show()
        
        self.close()
            
    
    def lookup(self):
        master_type = self.dropdown1.currentText()        
        self.searchwindow = search()
        self.searchwindow.show()
        self.close()

    
def main():
    app = QApplication([])
    with open("styles/dark.qss", "r") as file:
        app.setStyleSheet(file.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()