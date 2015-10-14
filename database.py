__author__ = 'gebruiker'

import sqlite3,config

class sqllite_database:
    """
    Een sqllite database class om hergebruik te stimuleren.
    """

    def __init__(self):
        self.connection = sqlite3.connect(config.database_file)
    def query(self,query):
        """
        :param query: string
        :returns cursor Object
        """

        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor
    def fetchAll(self,cursor):
        """
        :param cursor: cursor Object
        :returns tuple
        """

        return cursor.fetchall()
    def fetchOne(self,cursor):
        """
        :param cursor: cursor Object
        :returns string
        """

        return cursor.fetchone()

database = sqllite_database()