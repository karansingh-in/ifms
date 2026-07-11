import sqlite3
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QWidget, QGridLayout
from utils.message import message
from pages.ic_setup import ICSetup

class search(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lookup')
        self.setGeometry(760, 480, 500, 200)
        self.initUI()

    def initUI(self):
        self.searchbar = QLineEdit()
        searchbutton = QPushButton('Search')
        searchbutton.clicked.connect(self.see)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid = QGridLayout()

        grid.addWidget(self.searchbar, 0, 0)
        grid.addWidget(searchbutton, 1, 0)

        central_widget.setLayout(grid)

    def see(self):
        entry = self.searchbar.text()
        conn = sqlite3.connect('ic_master.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(f'''
                       select * from ic_master where ic_name='{entry}'

                        ''')
        
        row = cursor.fetchone()
        if row is None:
            self.msg = message('Entry not found')
            self.msg.show()
            
            self.close()
        else:
            print(tuple(row))
            self.ic_window = ICSetup('A:Amend')
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
            self.ic_window.show()
            self.close()

