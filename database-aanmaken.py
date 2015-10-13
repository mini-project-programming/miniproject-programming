__author__ = 'Merlijn'

import sqlite3
conn = sqlite3.connect("reis-database.db")

c = conn.cursor()

c.execute('''CREATE TABLE gebruikers
             (gebruikerID int primary key, naam text, ovnummer int)''')

c.execute('''CREATE TABLE reisgegevens
             (reisID int primary key, beginstation text, eindstation text)''')

c.execute('''CREATE TABLE stations
             (stationID int primary key, naam text)''')