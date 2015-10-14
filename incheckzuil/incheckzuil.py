__author__ = 'Merlijn'

import sqlite3
import tkinter

database_file = "../reis-database.db"

window = tkinter.Tk()
window.geometry("600x600")
window.title("Incheckzuil")


def haal_gebruiker_id(ovnummer):
    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()

        c.execute("SELECT gebruikerID FROM gebruikers WHERE ovnummer=%d" % int(ovnummer))

        return c.fetchone()


def haal_reis_gegevens(gebruikerid):
    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()

        c.execute("SELECT * FROM reisgegevens WHERE gebruikerID=%d" % gebruikerid)
        return c.fetchall()

ov_nummer = input("Wat is uw OV nummer?")
reisgegevens = haal_reis_gegevens(haal_gebruiker_id(ov_nummer))

lbl_ov_nummer = tkinter.Label(window, text="Voer uw ov nummer in:")
ent_ov_nummer = tkinter.Entry(window)
ent_uitvoer_vak = tkinter.Text(window)

lbl_ov_nummer.pack()
ent_ov_nummer.pack()
ent_uitvoer_vak.pack()

for row in reisgegevens:
    uitvoer_regel = str(row) + "\n"
    ent_uitvoer_vak.insert("end", uitvoer_regel)

window.mainloop()
