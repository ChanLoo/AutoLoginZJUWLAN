#coding:utf-8
'''
author: ChanLo
e-mail: chanlo@protonmail.ch
------------------
Describtion:
This is a module used to save the username and password.
'''

import sqlite3

class UPSave(object):
    def __init__(self):
        pass

    def create_DB(self, name_DB):
        with sqlite3.connect(name_DB+'.db') as conn:
            c = conn.cursor()
            create_sql = '''CREATE TABLE IF NOT EXISTS user
                        (
                            ID INTEGER PRIMARY KEY,
                            username TEXT,
                            password TEXT
                        );
                        '''

            c.execute(create_sql)
            conn.commit()

    def insert_to_DB(self, name_DB, username, password):
        with sqlite3.connect(name_DB+'.db') as conn:
            c = conn.cursor()
            insert_sql = "INSERT INTO user (username, password) \
              VALUES ('%s', '%s')" % (username, password)   
            c.execute(insert_sql)
            conn.commit()

    def delete_DB(self, name_DB):
        with sqlite3.connect(name_DB+'.db') as conn:
            c = conn.cursor()
            delete_sql = 'DELETE FROM user'
            c.execute(delete_sql)
            conn.commit()

    def select_DB(self, name_DB, aim_id):
        with sqlite3.connect(name_DB+'.db') as conn:
            c = conn.cursor()
            delete_sql = 'SELECT username,password FROM user WHERE ID=%d' % aim_id
            cursor = c.execute(delete_sql)
            for row in cursor:
                username, password = row
            conn.commit()
            return username, password
    
    def print_DB(self, name_DB):
        with sqlite3.connect(name_DB+'.db') as conn:
            c = conn.cursor()
            cursor = c.execute('SELECT * FROM user')
            for row in cursor:
                print('ID = ', row[0])
                print('Username = ', row[1])
                print('Password = ', row[2])

if __name__ == '__main__':
    UPSave = UPSave()
    name_DB = 'test'
    UPSave.create_DB(name_DB)
    UPSave.insert_to_DB(name_DB, '1a', '123c')
    UPSave.insert_to_DB(name_DB, '2', '456')
    UPSave.print_DB(name_DB)
    username, password = UPSave.select_DB(name_DB, 1)
    print(username)
    print(password)