__author__ = 'Merlijn'

import sqlite3,qrcode
import tkinter as tk
from tkinter import *

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
    window.title('Voltooid')
    window.configure(background='yellow')
    w = Label(window, text="Uw opdracht is voltooid!", font=('Arial', 20), bg= 'yellow')
    w.pack()
    w.place(x=170, y=150)
    print(E2.get())


# genereer eenmalig de gegevens die in de database staan zodat er makkelijk meer gewerkt kan worden
station_lijst = genereer_stationlijst()
ovnummer_lijst = genereer_ovnummerlijst()

window = tk.Tk()
window.geometry('600x400')
window.title('Ns overzicht')
window.configure(background='yellow')

T = Label(window, text="Welkom bij NS reis-database", font=('Arial', 20), bg= 'yellow')
B = tk.Button(window, text ="Continue", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = windows, state = 'disabled')

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

E1 = tk.Label(window, text="OV-nummer", bg = 'yellow')
E2 = tk.Entry(window, textvariable=sv)

option1 = window
variable = StringVar(option1)
variable.set('Beginstation')
om1 = OptionMenu(option1, variable, *station_lijst)

option2 = window
variable = StringVar(option2)
variable.set("Eindstation")
om2 = OptionMenu(option2, variable, *station_lijst)

def callback(sv):
    try:
        if int(E2.get()) in ovnummer_lijst:
            print('Correct')
            if E2.get():
                B.config(state = 'normal')
        else:
            B.config(state = 'disabled')
    except:
        print('Retry')




T.pack()
E1.pack()
E2.pack()
B.pack()
om1.pack()
om2.pack()
T.place(x = 140)
E1.place(x = 130, y = 200)
E2.place(x = 210, y = 200)
B.place(x = 130, y = 300)
om1.place(x = 100, y = 100)
om2.place(x = 100, y = 150)
window.mainloop()


#qr code genereren
img = qrcode.make("123")
 