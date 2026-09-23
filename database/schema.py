from .connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# ic master
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
                email3 text,
                cgl1 integer,
                cgl2 integer
               )
               ''')

# ic history
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

# ic pending
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
                pan_no text ,
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

# users
cursor.execute('''
               create table if not exists users(
                   id integer primary key autoincrement,
                   username text UNIQUE,
                   password_hash text,
                   full_name text,
                   email text unique,
                   role text,
                   created_at datetime,
                   phone_number text,
                   status TEXT NOT NULL DEFAULT 'ACTIVE'
               )
               ''')

# permissions
cursor.execute("""
CREATE TABLE IF NOT EXISTS permissions (
    permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    permission_name TEXT NOT NULL UNIQUE,
    module TEXT NOT NULL
)
""")

# user permissions
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    permission_id INTEGER NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (permission_id) REFERENCES permissions(permission_id),

    UNIQUE(user_id, permission_id)
)
""")

conn.commit()
conn.close()


