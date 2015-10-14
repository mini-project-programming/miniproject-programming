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

def window2():
    window = tk.Tk()
    window.geometry('400x200')
    window.title("Beginstation")
    window.configure(background='yellow')
    option1 = window

    def option_changed(a):
        if a != 'Beginstation':
            B.config(state='normal')
        else:
            B.config(state='disabled')

    variable1 = StringVar()
    variable1.set('default')

    variable = StringVar(option1)
    variable.set('Beginstation')
    om1 = OptionMenu(option1, variable, *station_lijst, command=option_changed)

    B = tk.Button(window, text ="Volgende", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = window3, state = 'disabled')
    w = Label(window, text="Kies uw beginstation", font=('Arial', 20), bg= 'yellow')

    w.pack()
    om1.place(x = 100, y = 100)
    om1.pack()
    B.place(x = 130, y = 300)
    B.pack()


def window3():
    window = tk.Tk()
    window.geometry('400x200')
    window.title("Beginstation")
    window.configure(background='yellow')

    option1 = window

    def option_changed(a):
        if a != 'Beginstation':
            B.config(state='normal')
        else:
            B.config(state='disabled')

    variable1 = StringVar()
    variable1.set('default')

    variable = StringVar(option1)
    variable.set('Eindstation')
    om1 = OptionMenu(option1, variable, *station_lijst, command=option_changed)
    B = tk.Button(window, text ="Volgende", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = window4, state = 'disabled')
    w = Label(window, text="Kies uw eindstation", font=('Arial', 20), bg= 'yellow')

    w.pack()
    om1.place(x = 100, y = 100)
    om1.pack()
    B.place(x = 130, y = 300)
    B.pack()

def window4():

    window = tk.Tk()
    window.geometry('600x400')
    window.title('Voltooid')
    window.configure(background='yellow')


    w = Label(window, text="Uw opdracht is voltooid!", font=('Arial', 20), bg= 'yellow')
    w.pack()
    w.place(x=170, y=150)


# genereer eenmalig de gegevens die in de database staan zodat er makkelijk meer gewerkt kan worden
station_lijst = genereer_stationlijst()
ovnummer_lijst = genereer_ovnummerlijst()

window = tk.Tk()
window.geometry('600x400')
window.title('Ns overzicht')
window.configure(background='yellow')

T = Label(window, text="Welkom bij NS reis-database", font=('Arial', 20), bg= 'yellow')
B = tk.Button(window, text ="Volgende", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = window2, state = 'disabled')

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

E1 = tk.Label(window, text="OV-nummer", bg = 'yellow')
E2 = tk.Entry(window, textvariable=sv)

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
T.place(x = 140)
E1.place(x = 130, y = 200)
E2.place(x = 210, y = 200)
B.place(x = 130, y = 300)
window.mainloop()


#qr code genereren
img = qrcode.make("123")
 