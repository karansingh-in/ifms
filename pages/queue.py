import sqlite3
from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem, QLabel, QGridLayout, QWidget, QDateEdit
from utils.pending import pending_queue
from utils.rejections import rejection_queue
from pages.ic_setup import ICSetup
from utils.message import message
import datetime

class Queue(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
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
        
        self.rejected_button.clicked.connect(self.show_rejections)
        self.pending_button.clicked.connect(self.show_pending)
        self.approved_button.clicked.connect(self.show_approved)
        self.history_button.clicked.connect(self.show_history)
        
    # show rejected requests
    def show_rejections(self):
        self.list_widget.clear()
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
                       select request_status, request_id, ic_no, ic_name, action, submitted_by, submitted_at from ic_pending
                       ''')

        r_queue = cursor.fetchall()
                
        for q in r_queue:
            if q['request_status'] == 'Rejected':
                item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
                self.list_widget.addItem(item)
        
        grid = QGridLayout()
            
        item = self.list_widget.itemActivated.connect(self.show_feedback)                 
    
    # show pending requests
    def show_pending(self):
        self.list_widget.clear()
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
                       select request_status, request_id, ic_no, ic_name, action, submitted_by, submitted_at from ic_pending
                       ''')

        r_queue = cursor.fetchall()
                
        for q in r_queue:
            if q['request_status'] == 'Pending':
                item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
                self.list_widget.addItem(item)
        
        grid = QGridLayout()
            
        item = self.list_widget.itemActivated.connect(self.show_feedback)
        
    # show approved requests
    def show_approved(self):
        self.list_widget.clear()
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
                       select request_status, request_id, ic_no, ic_name, action, submitted_by, submitted_at from ic_pending
                       ''')

        r_queue = cursor.fetchall()
                
        for q in r_queue:
            if q['request_status'] == 'approved':
                item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
                self.list_widget.addItem(item)
        
        grid = QGridLayout()
            
        item = self.list_widget.itemActivated.connect(self.show_feedback)
    
    # show all requests
    def show_history(self):
        self.list_widget.clear()
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
                       select request_status, request_id, ic_no, ic_name, action, submitted_by, submitted_at from ic_pending
                       ''')

        r_queue = cursor.fetchall()
                
        for q in r_queue:
            item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
            self.list_widget.addItem(item)
        
        grid = QGridLayout()
            
        item = self.list_widget.itemActivated.connect(self.show_feedback)
    
    # showing rejection feedback
    def show_feedback(self, item):
        index_of_separation = item.text().rfind('-')
        self.function = item.text()[index_of_separation + 1:]
        
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row

        self.index_of_dash = item.text().index('-')
        self.request_id = item.text()[:self.index_of_dash - 1]
        self.request_id = int(self.request_id)
        
        cursor = conn.cursor()
        
        cursor.execute('''
                       select feedback, ic_no from ic_pending where request_id = ?                       
                       ''', (self.request_id,))
        
        self.feedback_text = cursor.fetchone()["feedback"]

        self.msg = message(text=self.feedback_text)
        self.msg.setWindowTitle('Feedback')
        self.msg.setGeometry(700, 400, 450, 270)
        self.msg.okbutton.setText('Modify')
        self.msg.okbutton.clicked.connect(lambda: self.open_ic(item))
        self.msg.show()
           
   # updating the values for resubmission
    def update_ic(self):
        conn = sqlite3.connect('ifms.db')
        cursor = conn.cursor()
        
        # update ic pending
        cursor.execute(f'''
                       update ic_pending set 
                        
                        ic_name=?,
                        role=?,
                        department=?,
                        bank=?,
                        status=?,
                        
                        account_no=?,
                        lei_no=?,
                        pan_no=?,
                        gst_no=?,
                        branch=?,
                        ifsc_code=?,
                        
                        address1=?,
                        address2=?,
                        address3=?,
                        city=?,
                        pin_code=?,
                        
                        name1=?,
                        designation1=?,
                        phone1=?,
                        email1=?,
                        
                        name2=?,
                        designation2=?,
                        phone2=?,
                        email2=?,
                        
                        name3=?,
                        designation3=?,
                        phone3=?,
                        email3=?,
                        action=?,
                        submitted_by=?,
                        submitted_at=?,
                        request_status=?
                        
                        
                    
                    where ic_no={self.ic_window.ic_number_text.text()}
                    ''',(
                    self.ic_window.ic_name_text.text(),
                    self.ic_window.roledropdown.currentText(),
                    self.ic_window.department_text.text(),
                    self.ic_window.bank_text.text(),
                    self.ic_window.statusdropdown.currentText(),
                    self.ic_window.account_no_text.text(),
                    self.ic_window.lei_no_text.text(),
                    self.ic_window.pan_no_text.text(),
                    self.ic_window.gst_no_text.text(),
                    self.ic_window.branch_text.text(),
                    self.ic_window.ifsc_code_text.text(),
                    self.ic_window.address1_text.text(),
                    self.ic_window.address2_text.text(),
                    self.ic_window.address3_text.text(),
                    self.ic_window.city_text.text(),
                    self.ic_window.pin_code_text.text(),
                    self.ic_window.contact_name1_text.text(),
                    self.ic_window.designation1dropdown.currentText(),
                    self.ic_window.phone1_text.text(),
                    self.ic_window.email1_text.text(),
                    self.ic_window.contact_name2_text.text(),
                    self.ic_window.designation2dropdown.currentText(),
                    self.ic_window.phone2_text.text(),
                    self.ic_window.email2_text.text(),
                    self.ic_window.contact_name3_text.text(),
                    self.ic_window.designation3dropdown.currentText(),
                    self.ic_window.phone3_text.text(),
                    self.ic_window.email3_text.text(),
                    self.function,
                    self.role,
                    datetime.datetime.now(),
                    'Pending'
                    )
                    )
                    
        conn.commit()
        conn.close()
    
    # open ic form
    def open_ic(self, item):
        
        self.ic_window = ICSetup(main_window=self, function='Create', role='Maker')
        self.stacked_widget.addWidget(self.ic_window)
        self.stacked_widget.setCurrentWidget(self.ic_window)
        
        index_of_separation = item.text().rfind('-')
        self.function = item.text()[index_of_separation + 1:]
        
        conn = sqlite3.connect('ifms.db')
        conn.row_factory = sqlite3.Row

        self.index_of_first_dash = item.text().index('-')
        self.index_of_separation_second_dash = item.text().index('-', self.index_of_first_dash + 1)
        self.ic_number = item.text()[self.index_of_first_dash + 2:self.index_of_separation_second_dash - 1]
        self.ic_number = int(self.ic_number)
        
        cursor = conn.cursor()
        
        cursor.execute(f'''
                       select * from ic_pending where ic_no=?
                        ''', (self.ic_number, ))

        row = cursor.fetchone()
        
        self.function = row['action']
        self.role = row['role']
        
        if row is None:
            self.msg = message('Entry not found')
            self.msg.show()
        else:
            print(row)
            self.ic_window.ic_number_text.setText(str(row["ic_no"]))
            self.ic_window.ic_name_text.setText(row["ic_name"])
            self.ic_window.roledropdown.setCurrentText(row["role"])
            self.ic_window.city_text.setText(row["city"])
            self.ic_window.department_text.setText(row["department"])
            self.ic_window.bank_text.setText(row["bank"])
            self.ic_window.statusdropdown.setCurrentText(row["status"])
            self.ic_window.pin_code_text.setText(row["pin_code"])
            self.ic_window.account_no_text.setText(str(row["account_no"]))
            self.ic_window.pan_no_text.setText(row["pan_no"])
            self.ic_window.gst_no_text.setText(row["gst_no"])
            self.ic_window.lei_no_text.setText(row["lei_no"])
            self.ic_window.branch_text.setText(row["branch"])
            self.ic_window.ifsc_code_text.setText(row["ifsc_code"])

            self.ic_window.address1_text.setText(row["address1"])
            self.ic_window.address2_text.setText(row["address2"])
            self.ic_window.address3_text.setText(row["address3"])

            self.ic_window.contact_name1_text.setText(row["name1"])
            self.ic_window.contact_name2_text.setText(row["name2"])
            self.ic_window.contact_name3_text.setText(row["name3"])

            self.ic_window.designation1dropdown.setCurrentText(row["designation1"])
            self.ic_window.designation2dropdown.setCurrentText(row["designation2"])
            self.ic_window.designation3dropdown.setCurrentText(row["designation3"])

            self.ic_window.phone1_text.setText(row["phone1"])
            self.ic_window.phone2_text.setText(row["phone2"])
            self.ic_window.phone3_text.setText(row["phone3"])

            self.ic_window.email1_text.setText(row["email1"])
            self.ic_window.email2_text.setText(row["email2"])
            self.ic_window.email3_text.setText(row["email3"])
            self.ic_window.submitbutton_ic.setText('Re-Submit')
            self.ic_window.submitbutton_ic.clicked.connect(self.update_ic)
            self.ic_window.cancelbutton.setText('Delete')
            self.ic_window.cancelbutton.setMaximumWidth(140)
            self.ic_window.cancelbutton.setStyleSheet('background-color: #9C2007;')
            self.ic_window.cancelbutton.clicked.connect(self.give_feedback)
    
    
    