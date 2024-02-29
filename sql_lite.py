import sqlite3
from sqlite3 import Error
def connection(db):
    conn = None
    
    try:
        conn = sqlite3.connect(db)
        print(conn)
        conn.execute('''CREATE TABLE USER
        (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        EMAIL            TEXT     NOT NULL,
        USERNAME           TEXT    NOT NULL,
        PASSWORD           TEXT    NOT NULL,
        ROLE           INT         NOT NULL);''')
        return conn
        
    except Error as e:
        print(e)
        
    # finally:
    #     if conn:
    #         conn.close()
        



def addToDB (id, name, email, usr, pwd, role, conn):
    conn.execute("INSERT INTO USER (ID,NAME,EMAIL,USERNAME,PASSWORD,ROLE) VALUES (?,?,?,?,?,?)", (id, name, email, usr, pwd, role))
    conn.commit()
    
    
def viewDB(conn):
    conn.execute('SELECT * FROM USER')
    conn.commit()


        
if __name__ == '__main__':
    conn = connection('.\\sqlite\\db\\pythonsqlite.db')
    
    addToDB(1, "Andrew", "jelson9854vt.edu", 'andrew', 'pwd1', 1, conn)
    
    viewDB(conn)
    
    conn.close()