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
            button.config(state='normal')
        else:
            button.config(state='disabled')

    variable1 = StringVar()
    variable1.set('default')

    variable = StringVar(option1)
    variable.set('Beginstation')
    om = OptionMenu(option1, variable, *station_lijst, command=option_changed)

    button = tk.Button(window, text ="Volgende", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = window3, state = 'disabled')
    w = Label(window, text="Kies uw beginstation", font=('Arial', 20), bg= 'yellow')

    w.pack()
    om.place(x = 100, y = 100)
    om.pack()
    button.place(x = 130, y = 300)
    button.pack()


def window3():
    window = tk.Tk()
    window.geometry('400x200')
    window.title("Beginstation")
    window.configure(background='yellow')

    option1 = window

    def option_changed(a):
        if a != 'Beginstation':
            button.config(state='normal')
        else:
            button.config(state='disabled')

    variable1 = StringVar()
    variable1.set('default')

    variable = StringVar(option1)
    variable.set('Eindstation')
    om = OptionMenu(option1, variable, *station_lijst, command=option_changed)
    button = tk.Button(window, text ="Volgende", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = window4, state = 'disabled')
    w = Label(window, text="Kies uw eindstation", font=('Arial', 20), bg= 'yellow')

    w.pack()
    om.place(x = 100, y = 100)
    om.pack()
    button.place(x = 130, y = 300)
    button.pack()

def window4():

    window = tk.Tk()
    window.geometry('600x400')
    window.title('Voltooid')
    window.configure(background='yellow')


    Text = Label(window, text="Uw opdracht is voltooid!", font=('Arial', 20), bg= 'yellow')
    Text.pack()
    Text.place(x=170, y=150)


# genereer eenmalig de gegevens die in de database staan zodat er makkelijk meer gewerkt kan worden
station_lijst = genereer_stationlijst()
ovnummer_lijst = genereer_ovnummerlijst()

window = tk.Tk()
window.geometry('600x400')
window.title('Ns overzicht')
window.configure(background='yellow')

text = Label(window, text="Welkom bij NS reis-database", font=('Arial', 20), bg= 'yellow')
button = tk.Button(window, text ="Volgende", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = window2, state = 'disabled')

kt = tk.StringVar()
kt.trace("w", lambda name, index, mode, kt=kt: knop_toegang(kt))

labelnaam = tk.Label(window, text="OV-nummer", bg = 'yellow')
input1 = tk.Entry(window, textvariable=kt)

def knop_toegang(kt):
    try:
        if int(input1.get()) in ovnummer_lijst:
            print('Correct')
            if input1.get():
                button.config(state = 'normal')
        else:
            button.config(state = 'disabled')
    except:
        print('Retry')

text.pack()
labelnaam.pack()
input1.pack()
button.pack()
text.place(x = 140)
labelnaam.place(x = 130, y = 200)
input1.place(x = 210, y = 200)
button.place(x = 130, y = 300)
window.mainloop()


#qr code genereren
img = qrcode.make("123")
 