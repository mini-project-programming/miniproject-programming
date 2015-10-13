__author__ = 'Merlijn'

import sqlite3

database_file = "../reis-database.db"
ov_nummer = 0
gebruiker_ID = 0


def haal_gegevens(ovnummer):
    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()

        c.execute("SELECT gebruikerID FROM gebruikers WHERE ovnummer=%d" % int(ovnummer))

        for row in c.fetchone():
            gebruiker_ID = row
            print(row)

        c.execute("SELECT * FROM reisgegevens WHERE gebruikerID=%d" % gebruiker_ID)
        print(c.fetchall())


ov_nummer = input("Wat is uw OV nummer?")
haal_gegevens(ov_nummer)