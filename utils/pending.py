import sqlite3
from PyQt5.QtWidgets import QMainWindow, QListWidget, QWidget, QLabel, QListWidgetItem, QGridLayout, QLineEdit, QComboBox
from pages.ic_setup import ICSetup
from utils.message import message
import datetime

class pending_queue(QMainWindow):
    def __init__(self, role, parent_window):
        super().__init__()
        self.setWindowTitle('Pending Queue')
        self.setGeometry(660, 380, 700, 450)
        self.role = role
        self.parent_window = parent_window
        self.initUI()
        
    def initUI(self):
        
        conn = sqlite3.connect('ic_master.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
                       select request_id, ic_no, ic_name, action, submitted_by, submitted_at from ic_pending
                       ''')

        self.queue = cursor.fetchall()
        
        self.listwidget = QListWidget()
        
        for q in self.queue:
            item = QListWidgetItem(f'{q['request_id']} - {q['ic_no']} - {q['ic_name']} - {q['action']}')
            self.listwidget.addItem(item)
        
        grid = QGridLayout()
        
        self.label = QLabel('The pending requests are: ')
        
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.listwidget, 1, 0)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        central_widget.setLayout(grid)
        
        print(self.role)
        if self.role == 'Checker':
            item = self.listwidget.itemActivated.connect(self.open_ic)
        
    def insert_ic(self, submitted_name, submitted_time):
        conn = sqlite3.connect('ic_master.db')
        self.submitted_name = submitted_name
        self.submitted_time = submitted_time
        cursor = conn.cursor()
        
        # insert into ic history
        cursor.execute('''
                    insert into ic_hist(
                        ic_no,
                        ic_name,
                        role,
                        department,
                        bank,
                        status,
                        
                        account_no,
                        lei_no,
                        gst_no,
                        pan_no,
                        branch,
                        ifsc_code,
                        
                        address1,
                        address2,
                        address3,
                        city,
                        pin_code,
                        
                        name1,
                        designation1,
                        phone1,
                        email1,
                        
                        name2,
                        designation2,
                        phone2,
                        email2,
                        
                        name3,
                        designation3,
                        phone3,
                        email3,
                        submitted_by,
                        submitted_at,
                        reviewed_by,
                        reviewed_at,
                        action
                        
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (
                        
                            self.data["ic_no"],
                            self.data["ic_name"],
                            self.data["role"],
                            self.data["department"],
                            self.data["status"],
                            self.data["bank"],

                            self.data["account_no"],
                            self.data["lei_no"],
                            self.data["gst_no"],
                            self.data["pan_no"],
                            self.data["branch"],
                            self.data["ifsc_code"],

                            self.data["address1"],
                            self.data["address2"],
                            self.data["address3"],
                            self.data["city"],
                            self.data["pin_code"],

                            self.data["name1"],
                            self.data["designation1"],
                            self.data["phone1"],
                            self.data["email1"],

                            self.data["name2"],
                            self.data["designation2"],
                            self.data["phone2"],
                            self.data["email2"],

                            self.data["name3"],
                            self.data["designation3"],
                            self.data["phone3"],
                            self.data["email3"],
                            self.submitted_name,
                            self.submitted_time,
                            self.role,
                            datetime.datetime.now(),
                            'Create'
                    )
                    )

    def insert_(self):
        conn = sqlite3.connect('ic_master.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        
        
        cursor.execute(f'''
                       select * from ic_pending where ic_no=?
                        ''', (self.ic_number, ))

        row = cursor.fetchone()
        self.insert_ic()
    
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
            self.ic_window.submitbutton_ic.setText('Approve')
            self.ic_window.submitbutton_ic.clicked.connect(self.insert_)
            self.ic_window.cancelbutton.setText('Reject')
            self.ic_window.cancelbutton.setMaximumWidth(140)
            self.ic_window.cancelbutton.setStyleSheet('background-color: red;')
            for i in self.findChildren(QLineEdit):
                i.setReadOnly(True)
            for i in self.findChildren(QComboBox):
                i.setEnabled(False)
                
            self.ic_window.setStyleSheet('''
                               QLineEdit{
                                   background-color: grey;
                                   }
                                QComboBox{
                                    background-color: grey;
                                    }''')
        
            self.ic_window.show()
            self.close()


        
        # self.ic_window = ICSetup(parent_window=self, function=self.function, role = self.role)
        # self.ic_window.show()
        # self.close()
        
    # def closeEvent(self, a0):
    #     self.parent_window.show()
    #     self.close()
    #     return super().closeEvent(a0)
        
        
        
# app = QApplication([])
# window = pending_queue()
# window.show()
# sys.exit(app.exec_())







