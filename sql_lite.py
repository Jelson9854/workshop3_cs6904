import sqlite3
from sqlite3 import Error
import random 
import json 


def connection(db):
    conn = None
    
    try:
        conn = sqlite3.connect(db)
        print(conn)
        if not conn:
            conn.execute('''CREATE TABLE USER
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            EMAIL            TEXT     NOT NULL,
            USERNAME           TEXT    NOT NULL,
            PASSWORD           TEXT    NOT NULL,
            ROLE           INT         NOT NULL);''')
        return conn
        
        return conn 
    except Error as e:
        print(e)
        
    # finally:
    #     if conn:
    #         conn.close()
        


def update(id, name, email, usr, pwd, role, conn):
    conn.execute("UPDATE USER SET NAME=?,EMAIL=?,USERNAME=?,PASSWORD=?,ROLE=? WHERE ID=?", (name, email, usr, pwd, role, id))

    conn.commit() 


def delete_user(id, conn):
    conn.execute("DELETE FROM USER WHERE ID=?",(id,))
    conn.commit()

def addToDB (id, name, email, usr, pwd, role, conn):
    conn.execute("INSERT INTO USER (ID,NAME,EMAIL,USERNAME,PASSWORD,ROLE) VALUES (?,?,?,?,?,?)", (id, name, email, usr, pwd, role))
    conn.commit()
    
def viewDB(conn):
    cursor = conn.execute('SELECT * FROM USER')
    rows = cursor.fetchall()
    
    # Create a list of dictionaries, each representing a row in the USER table
    users = []
    for row in rows:
        user = {"ID": row[0], "NAME": row[1], "EMAIL": row[2], "USERNAME": row[3], "PASSWORD": row[4], "ROLE": row[5]}
        users.append(user)
    
    # Convert the list of dictionaries into a JSON string
    json_str = json.dumps(users, indent=4)  # `indent=4` for pretty printing
    print(json_str)
    return json_str

        
if __name__ == '__main__':
    conn = connection('sqlite/db/pyhonsqlite.db')
    
    addToDB(random.randint(3, 100), "Andrew", "jelson9854vt.edu", 'andrew', 'pwd1', 1, conn)
    
    print("Json " + str(viewDB(conn)) )
    
    delete_user(1, conn)

    viewDB(conn)

    update(2, "Ray", "updatedvt.edu", 'ray', 'pwd1', 1, conn)

    viewDB(conn)


    conn.close()