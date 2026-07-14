from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QLineEdit, QComboBox, QPushButton, QDateEdit
from PyQt5.QtCore import QDate, Qt
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
        
        self.label1 = QLabel("Date of creation", self)
        
        self.label2 = QLabel("Master Data Type", self)

        self.label3 = QLabel("Function", self)
        
        self.dropdown1 = QComboBox(self)
        options = ['I: IC Master setup', 'T: Trust Master setup']
        self.dropdown1.addItems(options)
        
        self.dropdown2 = QComboBox(self)
        options2 = ['C: Create', 'A: Amend', 'E: Enquiry']
        self.dropdown2.addItems(options2)
        
        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(QDate.currentDate())

        self.searchbar = QLineEdit()
        self.searchbar.setMaximumWidth(280)
        self.searchbar.setPlaceholderText('Enter IC Number')
        
        self.SubmitButton = QPushButton('Submit')
        self.CancelButton = QPushButton('Cancel')
        self.roleselection = QComboBox(self)
        role_options = ['Maker', 'Checker']
        self.roleselection.addItems(role_options)
        self.queue = QPushButton('Pending')
        self.lookupbutton = QPushButton('Lookup')
        self.lookupbutton.hide()
        self.searchbar.hide()
        self.lookupbutton.clicked.connect(self.lookup)
        
        self.dropdown2.currentTextChanged.connect(self.show_search)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid = QGridLayout()
        
        grid.addWidget(label, 0, 0)
        grid.addWidget(self.roleselection, 1, 2)
        grid.addWidget(self.queue, 2, 2)
        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.label3, 3, 0)
        grid.addWidget(self.dateEdit, 1, 1)
        grid.addWidget(self.dropdown1, 2, 1)
        grid.addWidget(self.dropdown2, 3, 1)
        grid.addWidget(self.searchbar, 4, 1)
        grid.addWidget(self.SubmitButton, 5, 1)
        grid.addWidget(self.CancelButton, 5, 2)
        grid.addWidget(self.lookupbutton, 5, 3)
        
        central_widget.setLayout(grid)
        
        self.SubmitButton.clicked.connect(self.submit)
        self.roleselection.currentTextChanged.connect(self.role_switch)
        
        
    # switch roles between maker and checker    
    def role_switch(self):
        self.role = self.roleselection.currentText()
        if self.role == 'Checker':
            self.label1.hide()
            self.label2.hide()
            self.label3.hide()
            self.dateEdit.hide()
            self.dropdown1.hide()
            self.dropdown2.hide()
            self.searchbar.hide()
            self.SubmitButton.hide()
            self.CancelButton.hide()
            self.lookupbutton.show()
        else:
            self.label1.show()
            self.label2.show()
            self.label3.show()
            self.dateEdit.show()
            self.dropdown1.show()
            self.dropdown2.show()
            self.searchbar.hide()
            self.SubmitButton.show()
            self.CancelButton.show()
            self.lookupbutton.hide()
            
    # show the searchbar
    def show_search(self):
        function_selection = self.dropdown2.currentText()
        if function_selection != 'C: Create':
            self.lookupbutton.show()
            self.searchbar.show()
         #  entry = self.searchbar.text()
         #   self.SubmitButton.clicked.connect(self.searching)
        else:
            self.lookupbutton.hide()
            self.searchbar.hide()
          #  self.SubmitButton.clicked.connect(self.open_icsetup)
        
    # different operations on submit button
    def submit(self):
        self.function = self.dropdown2.currentText()
        if self.function == 'C: Create':
            self.role = self.roleselection.currentText()
            self.ic_window = ICSetup(function=self.function, role=self.role, parent_window=self)
            self.ic_window.show()
            self.close()
        else:
            entry = self.searchbar.text()
            self.role = self.roleselection.currentText()
            self.search_ic = search_(entry=entry, function=self.function, role=self.role)
            self.close()
            
    
    def lookup(self):
        master_type = self.dropdown1.currentText()        
        self.searchwindow = search(self)
        self.searchwindow.show()
        self.close()
