import sqlite3

conn = sqlite3.connect('ic_master.db')
cursor = conn.cursor()

cursor.execute('''
               create table if not exists ic_master(
                id integer primary key autoincrement,
                ic_no integer,
                ic_name text,
                role text,
                department text,
                status text,
                bank text,

                account_no integer ,
                lei_no text ,
                gst_no text ,
                pan_no text unique,
                branch text,
                ifsc_code text ,

                address1 text,
                address2 text,
                address3 text,
                city text,
                pin_code text,

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

cursor.execute('''
               create table if not exists ic_hist(
                id integer primary key autoincrement,
                ic_no integer,
                ic_name text,
                role text,
                department text,
                status text,
                bank text,

                account_no integer ,
                lei_no text ,
                gst_no text ,
                pan_no text unique,
                branch text,
                ifsc_code text ,

                address1 text,
                address2 text,
                address3 text,
                city text,
                pin_code text,

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
                email3 text,
                datetime timestamp,
                action text,
                submitted_by text,
                submitted_at timestamp,
                reviewed_by text,
                reviewed_at timestamp
                )''')

cursor.execute('''
               create table if not exists ic_pending(
                ic_no integer,
                ic_name text,
                role text,
                department text,
                status text,
                bank text,

                account_no integer ,
                lei_no text ,
                gst_no text ,
                pan_no text unique,
                branch text,
                ifsc_code text ,

                address1 text,
                address2 text,
                address3 text,
                city text,
                pin_code text,

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
                email3 text,
                action text,
                request_status text,
                request_id integer primary key autoincrement,
                submitted_by text,
                reviewed_by text,
                submitted_at timestamp,
                reviewed_at timestamp,
                feedback text
                )''')


conn.commit()
conn.close()


