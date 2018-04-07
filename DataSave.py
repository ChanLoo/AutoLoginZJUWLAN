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
                            username BLOB NOT NULL UNIQUE ON    \
                              CONFLICT IGNORE,
                            password BLOB NOT NULL
                        );
                        '''
            cu.execute(create_sql)
            conn.commit()

    def insert_to_DB(self, name_DB, username, password):
        with sqlite3.connect(Name_DB+'.db') as conn:
            c = conn.cursor()
            insert_sql = 'INSERT INTO user (username, password) \
              VALUES (?,?)', (buffer(username), buffer(password))
            cu.execute(insert_sql)
            conn.commit()

    def delete_DB(self, name_DB):
        with sqlite3.connect as conn:
            c = conn.cursor()
            delete_sql = 'DELETE FROM user'
            cu.execute(delete_sql)
            conn.commit()
    

