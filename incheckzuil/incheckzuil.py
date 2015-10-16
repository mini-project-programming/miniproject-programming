__author__ = 'Merlijn, Ismael'

import tkinter
from tkinter import messagebox

from database import *


window = tkinter.Tk()
window.geometry("850x500")
window.title("Incheckzuil")

# kleuren
ns_geel = "#FFCC33"
ns_blauw = "#010066"
tekst_kleur = "white"


def haal_gebruiker_id(ovnummer):
    """Returned een gebruikerID op basis van de ingevoerde OV nummer."""
    query = database.query("SELECT gebruikerID FROM gebruikers WHERE ovnummer=%d" % int(ovnummer))
    return database.fetchOne(query)


def haal_reis_gegevens(gebruikerid):
    """Returned een list van alle reisgegevens op basis van de gebruikerID"""
    query = database.query("SELECT * FROM reisgegevens WHERE gebruikerID=%d" % gebruikerid)
    return database.fetchAll(query)


def haal_station_gegevens():
    """Alle stationsgegevens worden opgehaald en in een dictionary gezet om stationID en naam te koppelen."""
    stationdict = {}

    query = database.query("SELECT stationID, naam FROM stations ORDER BY stationID ASC")
    for row in database.fetchAll(query):
        stationdict[row[0]] = row[1]

    return stationdict


def start_printen(nummer):
    """Check of de input correct is.
    Print daarnaalle verzamelde gegevens in het tekstvak op een leesbare manier.
    """
    try:
        int(nummer)
    except ValueError:
        messagebox.showinfo("Error", "Voer een ovnummer in")
        return
    if len(ent_uitvoer_vak.get("1.0", "end")) > 0:
        ent_uitvoer_vak.delete("1.0", "end")
    if str(haal_gebruiker_id(nummer)) == "None":
        messagebox.showinfo("Error", "Het opgegeven ovnummer is niet gevonden in de database.")
        return

    stations = haal_station_gegevens()
    reisgegevens = haal_reis_gegevens(haal_gebruiker_id(nummer))

    for row in reisgegevens:
        reis_id = row[0]
        begin_station = stations[row[2]]
        eind_station = stations[row[3]]

        uitvoer_regel = "Reis ID: {0:3s} Beginstation: {1:25s} Eindstation: {2:25s} \n".format(str(reis_id),
                                                                                               str(begin_station),
                                                                                               str(eind_station))
        ent_uitvoer_vak.insert("end", uitvoer_regel)


lbl_ov_nummer = tkinter.Label(window, bg=ns_geel, text="Voer uw ov nummer in:")
ent_ov_nummer = tkinter.Entry(window)
btn_start = tkinter.Button(window, text="Haal reisgegevens op", state="normal", bg=ns_blauw, fg=tekst_kleur,
                           activebackground=ns_blauw, activeforeground=tekst_kleur,
                           command=lambda: start_printen(ent_ov_nummer.get()))
ent_uitvoer_vak = tkinter.Text(window, width=100)

lbl_ov_nummer.grid(row=0, column=0)
ent_ov_nummer.grid(row=0, column=1)
btn_start.grid(row=0, column=3)
ent_uitvoer_vak.grid(row=1, columnspan=16)

ov_nummer = ent_ov_nummer.get()

window.config(background=ns_geel)
window.mainloop()