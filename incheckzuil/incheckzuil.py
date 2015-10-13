__author__ = 'Merlijn'

import sqlite3

#verbinding maken met de database
conn = sqlite3.connect("")
#shortcut voor de database
c = conn.cursor()

ov_nummer = 0
gebruiker_ID = 0


c.execute("SELECT gebruikerID FROM gebruikers WHERE ovnummer=ov_nummer")
c.execute("SELECT * FROM reisgegevens WHERE gebruikerID=gebruiker_ID")