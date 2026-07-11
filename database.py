import sqlite3

conn = sqlite3.connect('ic_master.db')
cursor = conn.cursor()

cursor.execute('''
               create table ic_master(
                ic_no integer primary key autoincrement,
                
                ic_name text,
                role text,
                city text,
                department text,
                bank text,
                status text,
                pin_code text,
                account_no integer ,
                pan_no text unique,
                gst_no text ,
                lei_no text ,
                branch text,
                ifsc_code text ,
                address1 text,
                address2 text,
                address3 text,
                name1 text,
                name2 text,
                name3 text,
                designation1 text,
                designation2 text,
                designation3 text,
                phone1 text,
                phone2 text,
                phone3 text,
                email1 text,
                email2 text,
                email3 text
               )
               ''')

conn.commit()
conn.close()


