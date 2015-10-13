__author__ = 'Merlijn'

import sqlite3

#verbinding maken met de database
conn = sqlite3.connect("../reis-database.db")

#shortcut voor de database
c = conn.cursor()

