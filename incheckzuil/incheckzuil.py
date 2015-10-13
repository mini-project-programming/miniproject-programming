__author__ = 'Merlijn'

import sqlite3

database_file = "../reis-database.db"


def haal_gebruiker_id(ovnummer):
    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()

        c.execute("SELECT gebruikerID FROM gebruikers WHERE ovnummer=%d" % int(ovnummer))

        return c.fetchone()


def haal_reis_gegevens(gebruikerid):
    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()

        c.execute("SELECT * FROM reisgegevens WHERE gebruikerID=%d" % gebruikerid)
        print(c.fetchall())

ov_nummer = 0

ov_nummer = input("Wat is uw OV nummer?")
haal_reis_gegevens(haal_gebruiker_id(ov_nummer))