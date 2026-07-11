from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QLineEdit, QComboBox, QPushButton
import sqlite3
class ICSetup(QMainWindow):
    def __init__(self, function):
        super().__init__()
        self.setWindowTitle('Investor Master')
        self.setGeometry(360, 100, 1500, 900)
        self.function = function
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
               
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        grid = QGridLayout()
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(2)
        grid.setContentsMargins(10, 10, 10, 10)
        
        heading1 = QLabel('IC Setup Prompt & Detail')
        heading1.setObjectName('header')
        heading1.setFixedHeight(30)
        
        heading2 = QLabel('Static Details of IC')
        heading2.setObjectName('header')
        heading2.setFixedHeight(30)
        
        heading3 = QLabel('Contact Details')
        heading3.setObjectName('header')
        heading3.setFixedHeight(30)
        
        
        functionlabel = QLabel('Function')
        self.function_selection = QLineEdit(self.function)

        rolelabel = QLabel('Role')
        role_options = ['blank', '1.ARC-9999', '2.Seller', '3.Non-Seller', '4.Government Agency']
        self.roledropdown = QComboBox(self)
        self.roledropdown.addItems(role_options)

        statuslabel = QLabel('Status')
        status_options = ['A:Active(Default Value)', 'I:Inactive']
        self.statusdropdown = QComboBox(self)
        self.statusdropdown.addItems(status_options)

        designation1label = QLabel('Designation')
        designation_options = ['a. Credit Officer', 'b. Funds in-charge', 'c. SPOC']
        self.designation1dropdown = QComboBox(self)
        self.designation1dropdown.addItems(designation_options)

        designation2label = QLabel('Designation')
        self.designation2dropdown = QComboBox(self)
        self.designation2dropdown.addItems(designation_options)

        designation3label = QLabel('Designation')
        self.designation3dropdown = QComboBox(self)
        self.designation3dropdown.addItems(designation_options)

        ic_number = QLabel('IC No.')
        self.ic_number_text = QLineEdit('')
        
        conn = sqlite3.connect('ic_master.db')
        cursor = conn.cursor()
        
        cursor.execute('''
                        select max(ic_no) from ic_master    
                       ''')
        
        number = cursor.fetchone()
        print(f'the larget number is {number}')
        if number[0] is None:
            self.ic_number_text.setText('1000')
        else:
            self.ic_number_text.setText(str(number[0]+1))
        conn.commit()
        conn.close()
        
        # self.ic_number_text.setReadOnly(True)
        # self.ic_number_text.setStyleSheet("""
        #     QLineEdit {
        #         color: white;
        #         background-color: grey;
        #     }
        # """)

        ic_name = QLabel('IC Name')
        self.ic_name_text = QLineEdit()

        bank = QLabel('Bank')
        self.bank_text = QLineEdit()

        department = QLabel('Department')
        self.department_text = QLineEdit()

        account_no = QLabel("Account No.")
        self.account_no_text = QLineEdit()

        lei_no = QLabel("LEI No.")
        self.lei_no_text = QLineEdit()

        address1 = QLabel("Address1")
        self.address1_text = QLineEdit()

        city = QLabel("City")
        self.city_text = QLineEdit()

        pan_no = QLabel("PAN No.")
        self.pan_no_text = QLineEdit()

        branch = QLabel("Branch")
        self.branch_text = QLineEdit()

        address2 = QLabel("Address2")
        self.address2_text = QLineEdit()

        pin_code = QLabel("PIN Code")
        self.pin_code_text = QLineEdit()

        gst_no = QLabel("GST No.")
        self.gst_no_text = QLineEdit()

        ifsc_code = QLabel("IFSC Code")
        self.ifsc_code_text = QLineEdit()

        address3 = QLabel("Address3")
        self.address3_text = QLineEdit()

        contact_name1 = QLabel("Name")
        self.contact_name1_text = QLineEdit()

        phone1 = QLabel("Phone")
        self.phone1_text = QLineEdit()

        email1 = QLabel("E-Mail ID")
        self.email1_text = QLineEdit()

        contact_name2 = QLabel("Name")
        self.contact_name2_text = QLineEdit()

        phone2 = QLabel("Phone")
        self.phone2_text = QLineEdit()

        email2 = QLabel("E-Mail ID")
        self.email2_text = QLineEdit()

        contact_name3 = QLabel("Name")
        self.contact_name3_text = QLineEdit()

        phone3 = QLabel("Phone")
        self.phone3_text = QLineEdit()

        email3 = QLabel("E-Mail ID")
        self.email3_text = QLineEdit()

        submitbutton_ic = QPushButton("Submit")
        cancelbutton = QPushButton("Cancel")
        grid.addWidget(heading1, 0, 0, 1, 4)
        grid.addWidget(functionlabel, 1, 0)
        grid.addWidget(self.function_selection, 1, 1)
        grid.addWidget(rolelabel, 2, 0)
        grid.addWidget(self.roledropdown, 2, 1)
        grid.addWidget(ic_number, 1, 2)
        grid.addWidget(self.ic_number_text, 1, 3)
        grid.addWidget(department, 2, 2)
        grid.addWidget(self.department_text, 2, 3)
        grid.addWidget(ic_name, 1, 4)
        grid.addWidget(self.ic_name_text, 1, 5)
        grid.addWidget(bank, 2, 4)
        grid.addWidget(self.bank_text, 2, 5)
        grid.addWidget(statuslabel, 3, 4)
        grid.addWidget(self.statusdropdown, 3, 5)
        
        grid.addWidget(heading2, 4, 0, 1, 4)
        grid.addWidget(account_no, 5, 0)
        grid.addWidget(self.account_no_text, 5, 1)
        grid.addWidget(lei_no, 6, 0)
        grid.addWidget(self.lei_no_text, 6, 1)
        grid.addWidget(address1, 7, 0)
        grid.addWidget(self.address1_text, 7, 1)
        grid.addWidget(city, 8, 0)
        grid.addWidget(self.city_text, 8, 1)
        grid.addWidget(pan_no, 5, 2)
        grid.addWidget(self.pan_no_text, 5, 3)
        grid.addWidget(branch, 6, 2)
        grid.addWidget(self.branch_text, 6, 3)
        grid.addWidget(address2, 7, 2)
        grid.addWidget(self.address2_text, 7, 3)
        grid.addWidget(pin_code, 8, 2)
        grid.addWidget(self.pin_code_text, 8, 3)
        grid.addWidget(gst_no, 5, 4)
        grid.addWidget(self.gst_no_text, 5, 5)
        grid.addWidget(ifsc_code, 6, 4)
        grid.addWidget(self.ifsc_code_text, 6, 5)
        grid.addWidget(address3, 7, 4)
        grid.addWidget(self.address3_text, 7, 5)

        grid.addWidget(heading3, 9, 0, 1, 4)
        grid.addWidget(contact_name1, 10, 0)
        grid.addWidget(self.contact_name1_text, 10, 1)
        grid.addWidget(contact_name2, 11, 0)
        grid.addWidget(self.contact_name2_text, 11, 1)
        grid.addWidget(contact_name3, 12, 0)
        grid.addWidget(self.contact_name3_text, 12, 1)
        grid.addWidget(designation1label, 10, 2)
        grid.addWidget(self.designation1dropdown, 10, 3)
        grid.addWidget(designation2label, 11, 2)
        grid.addWidget(self.designation2dropdown, 11, 3)
        grid.addWidget(designation3label, 12, 2)
        grid.addWidget(self.designation3dropdown, 12, 3)
        grid.addWidget(phone1, 10, 4)
        grid.addWidget(self.phone1_text, 10, 5)
        grid.addWidget(phone2, 11, 4)
        grid.addWidget(self.phone2_text, 11, 5)
        grid.addWidget(phone3, 12, 4)
        grid.addWidget(self.phone3_text, 12, 5)
        grid.addWidget(email1, 10, 6)
        grid.addWidget(self.email1_text, 10, 7)
        grid.addWidget(email2, 11, 6)
        grid.addWidget(self.email2_text, 11, 7)
        grid.addWidget(email3, 12, 6)
        grid.addWidget(self.email3_text, 12, 7)
        grid.addWidget(submitbutton_ic, 13, 6)
        grid.addWidget(cancelbutton, 13, 7)

        central_widget.setLayout(grid)

        
        
        submitbutton_ic.clicked.connect(self.insert_ic)
        
  
        
    def insert_ic(self):
        self.data = {
            "ic_no": self.ic_number_text.text(),
            "ic_name": self.ic_name_text.text(),
            "role": self.roledropdown.currentText(),
            "department": self.department_text.text(),
            "bank": self.bank_text.text(),
            "status": self.statusdropdown.currentText(),

            "account_no": self.account_no_text.text(),
            "lei_no": self.lei_no_text.text(),
            "pan_no": self.pan_no_text.text(),
            "gst_no": self.gst_no_text.text(),
            "branch": self.branch_text.text(),
            "ifsc_code": self.ifsc_code_text.text(),

            "address1": self.address1_text.text(),
            "address2": self.address2_text.text(),
            "address3": self.address3_text.text(),
            "city": self.city_text.text(),
            "pin_code": self.pin_code_text.text(),

            "name1": self.contact_name1_text.text(),
            "designation1": self.designation1dropdown.currentText(),
            "phone1": self.phone1_text.text(),
            "email1": self.email1_text.text(),

            "name2": self.contact_name2_text.text(),
            "designation2": self.designation2dropdown.currentText(),
            "phone2": self.phone2_text.text(),
            "email2": self.email2_text.text(),

            "name3": self.contact_name3_text.text(),
            "designation3": self.designation3dropdown.currentText(),
            "phone3": self.phone3_text.text(),
            "email3": self.email3_text.text(),
        }
        conn = sqlite3.connect('ic_master.db')
        cursor = conn.cursor()
        
        cursor.execute('''
                    insert into ic_master(
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
                        email3
                        
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                            self.data["email3"]
                    )
                    )
        conn.commit()
        conn.close()
        
        

            
        
