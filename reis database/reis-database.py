__author__ = 'Merlijn'

import qrcode
import tkinter as tk
from tkinter import *
from database import *

TITLE_FONT = ("Helvetica", 18, "bold")
beginstation = ""
eindstation = ""
ovnummer = 0


# kleuren
ns_geel = "#FFCC33"
ns_blauw = "#010066"
tekst_kleur = "white"


def genereer_stationlijst():
    stationlijst = []

    cursor = database.query("SELECT naam FROM stations ORDER BY naam ASC")

    for row in database.fetchAll(cursor):
        for row2 in row:
            stationlijst.append(row2)

    return stationlijst


def genereer_ovnummerlijst():
    ovnummerlijst = []

    cursor = database.query("SELECT ovnummer FROM gebruikers")

    for row in database.fetchAll(cursor):
        for row2 in row:
            ovnummerlijst.append(row2)

    return ovnummerlijst


class Reisdatabase(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Loginframe, Beginstationframe, Eindstationframe, Voltooidframe):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Loginframe)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()


class Loginframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=ns_geel)

        ovnummer_lijst = genereer_ovnummerlijst()

        welkom = Label(self, text="Welkom bij NS reis-database", background=ns_geel, font=('Arial', 20))

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

        ovnummer = tk.Label(self, background=ns_geel, text="OV-nummer (8 cijfers)")
        input_ovnummer = tk.Entry(self, textvariable=sv)

        def button_pressed():
            controller.show_frame(Beginstationframe)
            input_ovnummer.delete(0, END)
            button.config(state='disabled')

        button = tk.Button(self, text="Volgende", bd=5, width=50, height=4, background="#010066", fg=tekst_kleur,
                           activebackground=ns_blauw, activeforeground=tekst_kleur, command=lambda: button_pressed(),
                           state='disabled')

        def callback(sv):
            global ovnummer
            try:
                if int(input_ovnummer.get()) in ovnummer_lijst:
                    print('Correct')
                    button.config(state='normal')
                    ovnummer = int(input_ovnummer.get())
                else:
                    button.config(state='disabled')
            except:
                print('Empty')

        welkom.pack()
        ovnummer.pack()
        input_ovnummer.pack()
        button.pack()
        welkom.place(x=140)
        ovnummer.place(x=180, y=200)
        input_ovnummer.place(x=310, y=200)
        button.place(x=130, y=300)


class Beginstationframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=ns_geel)

        station_lijst = genereer_stationlijst()

        def option_changed(a):
            global beginstation
            print(sv)
            beginstation = sv.get()
            button.config(state='normal')

        sv = StringVar(self)
        sv.set('Beginstation')

        optionmenu = OptionMenu(self, sv, *station_lijst, command=option_changed)
        optionmenu.config(bg=ns_blauw, fg=tekst_kleur, activebackground=ns_blauw, activeforeground=tekst_kleur)

        def button_pressed():
            controller.show_frame(Eindstationframe)
            sv.set('Beginstation')
            button.config(state='disabled')

        button = tk.Button(self, text="Volgende", bd=5, width=50, height=4, background=ns_blauw, fg="white",
                           activebackground=ns_blauw, activeforeground=tekst_kleur, command=lambda: button_pressed(),
                           state='disabled')
        begin_station = Label(self, text="Kies uw beginstation", background=ns_geel, font=('Arial', 20))

        begin_station.pack()
        optionmenu.place(x=100, y=100)
        optionmenu.pack()
        button.place(x=130, y=300)
        button.pack()


class Eindstationframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=ns_geel)

        def option_changed(a):
            global eindstation, beginstation
            eindstation = sv.get()
            print(a, beginstation)
            if a != beginstation:
                button.config(state="normal")
            else:
                button.config(state="disabled")

        def save_and_show_voltooid():
            save_reisgegevens(beginstation, eindstation)
            controller.show_frame(Voltooidframe)

        def save_reisgegevens(beginstation, eindstation):
            global ovnummer
            beginstationID = database.fetchOne(
                database.query("SELECT stationID FROM stations WHERE naam=\'%s\'" % beginstation))
            eindstationID = database.fetchOne(
                database.query("SELECT stationID FROM stations WHERE naam=\'%s\'" % eindstation))
            gebruikerID = database.fetchOne(
                database.query("SELECT gebruikerID FROM gebruikers WHERE ovnummer=%d" % ovnummer))
            print(beginstation, eindstation, beginstationID, eindstationID, gebruikerID)
            database.query(
                "INSERT INTO reisgegevens(gebruikerID,beginstationID,eindstationID) VALUES ({0},{1},{2})".format(
                    gebruikerID[0], beginstationID[0], eindstationID[0]))
            database.save()

        sv = StringVar(self)
        sv.set('Eindstation')
        station_lijst = genereer_stationlijst()

        optionmenu = OptionMenu(self, sv, *station_lijst, command=option_changed)
        optionmenu.config(bg=ns_blauw, fg=tekst_kleur, activebackground=ns_blauw, activeforeground=tekst_kleur)

        def button_pressed():
            save_and_show_voltooid()
            sv.set('Eindstation')
            button.config(state='disabled')

        button = tk.Button(self, text="Volgende", bd=5, width=50, height=4, background=ns_blauw, fg=tekst_kleur,
                           activebackground=ns_blauw, activeforeground=tekst_kleur, command=button_pressed,
                           state='disabled')
        eind_station = Label(self, text="Kies uw eindstation", background=ns_geel, font=('Arial', 20))

        eind_station.pack()
        optionmenu.place(x=100, y=100)
        optionmenu.pack()
        button.place(x=130, y=300)
        button.pack()


class Voltooidframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=ns_geel)

        opgeslagen = Label(self, text="Uw reisgegevens zijn opgeslagen!", background=ns_geel, font=('Arial', 20))
        opgeslagen.pack()
        opgeslagen.place(x=170, y=150)

        # qr code genereren
        def generate_and_show_qr_code():
            img = qrcode.make(
                database.fetchOne(database.query("SELECT reisID FROM reisgegevens ORDER BY reisID desc"))[0])
            img.show()

        button = tk.Button(self, text="Bekijk qr code", bd=5, width=50, height=4, background=ns_blauw, fg=tekst_kleur,
                           activebackground=ns_blauw, activeforeground=tekst_kleur, command=generate_and_show_qr_code)
        button2 = tk.Button(self, text='Terug naar beginscherm', bd=5, width=50, height=4, background=ns_blauw,
                            fg=tekst_kleur, activebackground=ns_blauw, activeforeground=tekst_kleur,
                            command=lambda: controller.show_frame(Loginframe))
        button2.place(x=130, y=350)
        button2.pack()
        button.place(x=130, y=300)
        button.pack()

        # w = Label(self, image=img, font=('Arial', 20))
        # w.pack()
        # w.place(x=170, y=150)


app = Reisdatabase()
app.geometry('600x400')
app.title('Ns overzicht')
app.mainloop()