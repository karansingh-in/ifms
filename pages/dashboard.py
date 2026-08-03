from PyQt5.QtWidgets import QStackedWidget, QFrame, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import Qt
import datetime
from pages.main_prompt_screen import MainWindow
from pages.ic_setup import ICSetup
from utils.search import search_
from pages.queue import Queue

class dashboard(QMainWindow):
    def __init__(self, user, role):
        super().__init__()
        self.setWindowTitle('IFMS')
        self.user = user
        self.role = role
        self.initUI()
        self.showMaximized()
        
        
    def initUI(self):
        ifms_label = QLabel('IFMS')
        self.username_label = QLabel()
        self.username_label.setAlignment(Qt.AlignRight)
        self.time_label = QLabel(f'@{self.user} hh:mm, dd/mm/yyyy')
        self.time_label.setAlignment(Qt.AlignRight)
        self.home_button = QPushButton('Home')
        self.audit_button = QPushButton('Audit')
        self.ic_button = QPushButton('IC')
        self.trust_button = QPushButton('Trust')
        self.journal_button = QPushButton('Journal')
        self.report_button = QPushButton('Report')
        self.queue_button = QPushButton('Queue')
        self.logout_button = QPushButton('Logout')
        self.work_area = QStackedWidget()
        self.logout_button.setStyleSheet('background-color: #9C2007;')
        
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("""
                            QFrame {
                                color: #404040;
                                background-color: #000000;
                            }
                            """)
        
        grid = QGridLayout()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid.addWidget(ifms_label, 0, 0)
        grid.addWidget(self.username_label, 0, 4)
        grid.addWidget(self.time_label, 0, 5)
        grid.addWidget(self.logout_button, 0, 6)
        grid.addWidget(self.home_button, 1, 0)
        grid.addWidget(self.ic_button, 1, 1)
        grid.addWidget(self.trust_button, 1, 2)
        grid.addWidget(self.journal_button, 1, 3)
        grid.addWidget(self.audit_button, 1, 4)
        grid.addWidget(self.report_button, 1, 5)
        grid.addWidget(self.queue_button, 1, 6)
        grid.addWidget(line, 2, 0, 1, 7)
        grid.addWidget(self.work_area, 3, 0, 1, 7)
        
        grid.setRowStretch( 2, 1)
        central_widget.setLayout(grid)
          
                
        self.ic_button.clicked.connect(self.show_prompt_screen)
        self.queue_button.clicked.connect(self.show_queue)
        self.home_button.clicked.connect(self.home)
        
        
    def show_queue(self):
        self.queue = Queue(stacked_widget = self.work_area)
        self.work_area.addWidget(self.queue)
        self.work_area.setCurrentWidget(self.queue)
        
    def show_ic(self, function, role):
        self.ic = ICSetup(function=function, role=role)
        self.work_area.addWidget(self.ic)
        self.work_area.setCurrentWidget(self.ic)
        
    def show_ic_searched(self, entry, function, role):
        self.search_ic = search_(entry=entry, function=function, role=role, work_area=self.work_area)
        self.work_area.addWidget(self.search_ic)
        self.work_area.setCurrentWidget(self.search_ic)
        
    def show_prompt_screen(self):
        self.prompt_window = MainWindow(role=self.role)  
        self.prompt_window.SubmitButton.clicked.connect(self.on_submit)
        self.work_area.addWidget(self.prompt_window)
        self.work_area.setCurrentWidget(self.prompt_window)
        
    def on_submit(self):
        self.function = self.prompt_window.dropdown2.currentText()
        if self.function == 'C: Create':
            self.show_ic(function=self.function, role=self.role)
        else:
            entry = self.prompt_window.searchbar.text()
            self.show_ic_searched(entry=entry, function=self.function, role=self.role)
        
    def home(self):
        blank_page = QWidget()
        self.work_area.addWidget(blank_page)
        self.work_area.setCurrentWidget(blank_page)
        



