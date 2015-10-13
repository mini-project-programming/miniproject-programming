__author__ = 'Merlijn'

import sqlite3,qrcode

#verbinding maken met de database
conn = sqlite3.connect("../reis-database.db")

#shortcut voor de database
c = conn.cursor()

#qr code genereren
img = qrcode.make("123")
