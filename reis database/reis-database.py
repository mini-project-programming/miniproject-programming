__author__ = 'Merlijn'

import sqlite3,qrcode
import tkinter as tk

database_file = "../reis-database.db"


def genereer_stationlijst():
    with sqlite3.connect(database_file) as conn:
        stationlijst = []
        c = conn.cursor()

        c.execute("SELECT naam FROM stations ORDER BY naam ASC")

        for row in c.fetchall():
            for row2 in row:
                stationlijst.append(row2)

        return stationlijst


def genereer_ovnummerlijst():
    with sqlite3.connect(database_file) as conn:
        ovnummerlijst = []
        c = conn.cursor()

        c.execute("SELECT ovnummer FROM gebruikers")

        for row in c.fetchall():
            for row2 in row:
                ovnummerlijst.append(row2)

        return ovnummerlijst


def windows():
    window = tk.Tk()
    window.geometry('600x400')
    print(E2.get())


# genereer eenmalig de gegevens die in de database staan zodat er makkelijk meer gewerkt kan worden
station_lijst = genereer_stationlijst()
ovnummer_lijst = genereer_ovnummerlijst()

window = tk.Tk()
window.geometry('600x400')
window.title('Ns overzicht')
window.configure(background='yellow')

T = tk.Text(window, height=2, width = 30, bg = 'yellow')
T.insert('end', 'Dit is tekst :D')
B = tk.Button(window, text ="Continue", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = windows, state = 'disabled')

def callback(sv):
    print(E2.get())
    if E2.get():
        B.config(state = 'normal')
        if E2.get() == ovnummer_lijst:
            print('sdaf')
    else:
        B.config(state = 'disabled')


sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))


E1 = tk.Label(window, text="OV-nummer", bg = 'yellow')
E2 = tk.Entry(window, textvariable=sv)



T.pack()
E1.pack()
E2.pack()
B.pack()
T.place(x = 190)
E1.place(x = 130, y = 200)
E2.place(x = 210, y = 200)
B.place(x = 130, y = 300)
window.mainloop()


#qr code genereren
img = qrcode.make("123")
 