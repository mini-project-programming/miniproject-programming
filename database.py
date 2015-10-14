__author__ = 'gebruiker'

import sqlite3,config

class sqllite_database:
    def __init__(self):
        self.connection = sqlite3.connect(config.database_file)
    def query(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor
    def fetchAll(self,cursor):
        return cursor.fetchall()
    def fetchOne(self,cursor):
        return cursor.fetchone()

database = sqllite_database()