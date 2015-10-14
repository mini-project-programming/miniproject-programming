__author__ = 'Merlijn'

import sqlite3
import tkinter

database_file = "../reis-database.db"

window = tkinter.Tk()
window.geometry("900x600")
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


def start_printen(nummer):
    reisgegevens = haal_reis_gegevens(haal_gebruiker_id(nummer))

    for row in reisgegevens:
        reis_id = row[0]
        begin_station = stations[row[2]]
        eind_station = stations[row[3]]

        uitvoer_regel = "Reis ID: {0:3s} Beginstation: {1:25s} Eindstation: {2:25s} \n".format(str(reis_id), str(begin_station), str(eind_station))
        ent_uitvoer_vak.insert("end", uitvoer_regel)

lbl_ov_nummer = tkinter.Label(window, text="Voer uw ov nummer in:")
ent_ov_nummer = tkinter.Entry(window)
btn_start = tkinter.Button(window, text="Haal reisgegevens op", command=lambda: start_printen(ent_ov_nummer.get()))
ent_uitvoer_vak = tkinter.Text(window, width=100)

lbl_ov_nummer.grid(row=0, column=0)
ent_ov_nummer.grid(row=0, column=1)
btn_start.grid(row=0, column=3)
ent_uitvoer_vak.grid(row=1, columnspan=16)

stations = haal_station_gegevens()
ov_nummer = ent_ov_nummer.get()

window.mainloop()