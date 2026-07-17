import sqlite3
from PyQt5.QtWidgets import QMainWindow, QListWidget, QWidget, QLabel, QListWidgetItem, QGridLayout
from utils.message import message
from pages.ic_setup import ICSetup
import datetime

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

        queue = cursor.fetchall()
        
        self.listwidget = QListWidget()
        
        for q in queue:
            if q['request_status'] == 'Rejected':
                item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
                self.listwidget.addItem(item)
        
        grid = QGridLayout()
        
        self.label = QLabel('The rejected requests are: ')
        
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.listwidget, 1, 0)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        central_widget.setLayout(grid)
            
        item = self.listwidget.itemActivated.connect(self.show_feedback)                 
    
      # updating the values for resubmission
    def update_ic(self):
        conn = sqlite3.connect('ic_master.db')

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
    
    # opening the rejected entry
    def open_ic(self, item):
        index_of_separation = item.text().rfind('-')
        self.function = item.text()[index_of_separation + 1:]
        
        conn = sqlite3.connect('ic_master.db')
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
            self.close()
        else:
            print(row)
            self.ic_window = ICSetup(function=self.function, role=self.role, parent_window=self)
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
           # self.ic_window.cancelbutton.clicked.connect(self.give_feedback)
            
        
            self.ic_window.show()
            self.msg.close()
            self.close()

    # showing rejection feedback
    def show_feedback(self, item):
        index_of_separation = item.text().rfind('-')
        self.function = item.text()[index_of_separation + 1:]
        
        conn = sqlite3.connect('ic_master.db')
        conn.row_factory = sqlite3.Row

        self.index_of_dash = item.text().index('-')
        self.request_id = item.text()[:self.index_of_dash - 1]
        self.request_id = int(self.request_id)
        
        
        cursor = conn.cursor()
        
        cursor.execute('''
                       select feedback, ic_no from ic_pending where request_id = ?                       
                       ''', (self.request_id,))
        
        self.feedback_text = cursor.fetchone()["feedback"]
        print(self.feedback_text)
        self.parent_window.show()

        self.msg = message(text=self.feedback_text)
        self.msg.setWindowTitle('Feedback')
        self.msg.setGeometry(700, 400, 450, 270)
        self.msg.okbutton.setText('Modify')
        self.msg.okbutton.clicked.connect(lambda: self.open_ic(item))
        self.msg.show()
        self.close()
    
    # open the parent window to closing the current one
    def closeEvent(self, a0):
        self.parent_window.show()
        return super().closeEvent(a0)
        
        
        
        
        