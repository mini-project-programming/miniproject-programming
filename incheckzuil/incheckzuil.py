__author__ = 'Merlijn'

import sqlite3
import tkinter

database_file = "../reis-database.db"

window = tkinter.Tk()
window.geometry("1000x600")
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


def haal_station_gegevens():
    with sqlite3.connect(database_file) as conn:
        stationdict = {}
        c = conn.cursor()

        c.execute("SELECT stationID, naam FROM stations ORDER BY stationID ASC")

        for row in c.fetchall():
            stationdict[row[0]] = row[1]

        return stationdict


def print_reisgegevens():
    pass


stations = haal_station_gegevens()
ov_nummer = input("Wat is uw OV nummer?")
reisgegevens = haal_reis_gegevens(haal_gebruiker_id(ov_nummer))

lbl_ov_nummer = tkinter.Label(window, text="Voer uw ov nummer in:")
ent_ov_nummer = tkinter.Entry(window)
btn_start = tkinter.Button(window, command="print_reisgegevens")
ent_uitvoer_vak = tkinter.Text(window, width=100)

lbl_ov_nummer.pack()
ent_ov_nummer.pack()
ent_uitvoer_vak.pack()

for row in reisgegevens:
    reis_id = row[0]
    begin_station = stations[row[2]]
    eind_station = stations[row[3]]

    uitvoer_regel = "Reis ID: {0:3s} Beginstation: {1:25s} Eindstation: {2:25s} \n".format(str(reis_id), str(begin_station), str(eind_station))
    ent_uitvoer_vak.insert("end", uitvoer_regel)

window.mainloop()
