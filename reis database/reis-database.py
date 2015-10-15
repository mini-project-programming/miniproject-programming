__author__ = 'Merlijn'

import qrcode
import tkinter as tk
from tkinter import *
from database import *

TITLE_FONT = ("Helvetica", 18, "bold")
beginstation = ""
eindstation = ""
ovnummer = 0


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


class reisDatabase(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (loginFrame, beginstationFrame, eindstationFrame, voltooidFrame):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(loginFrame)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class loginFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ovnummer_lijst = genereer_ovnummerlijst()

        T = Label(self, text="Welkom bij NS reis-database", font=('Arial', 20))
        B = tk.Button(self, text ="Volgende", bd = 5, width = 50, height = 4, command = lambda: controller.show_frame(beginstationFrame), state = 'disabled')

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

        E1 = tk.Label(self, text="OV-nummer")
        E2 = tk.Entry(self, textvariable=sv)

        def callback(sv):
            global ovnummer
            try:
                if int(E2.get()) in ovnummer_lijst:
                    print('Correct')
                    B.config(state = 'normal')
                    ovnummer = int(E2.get())
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


class beginstationFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        station_lijst = genereer_stationlijst()

        def option_changed(a):
            global beginstation
            print(variable)
            beginstation = variable.get()
            B.config(state='normal')

        variable = StringVar(self)
        variable.set('Beginstation')

        om1 = OptionMenu(self, variable, *station_lijst, command=option_changed)

        B = tk.Button(self, text ="Volgende", bd = 5, width = 50, height = 4, command = lambda: controller.show_frame(eindstationFrame), state = 'disabled')
        w = Label(self, text="Kies uw beginstation", font=('Arial', 20))

        w.pack()
        om1.place(x = 100, y = 100)
        om1.pack()
        B.place(x = 130, y = 300)
        B.pack()


class eindstationFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def option_changed(a):
            global eindstation,beginstation
            eindstation = variable.get()
            print(a,beginstation)
            if a != beginstation:
                B.config(state="normal")
            else:
                B.config(state="disabled")

        def save_and_show_voltooid():
            save_reisgegevens(beginstation,eindstation)
            controller.show_frame(voltooidFrame)
        def save_reisgegevens(beginstation,eindstation):
            global ovnummer
            beginstationID = database.fetchOne(database.query("SELECT stationID FROM stations WHERE naam=\'%s\'" % beginstation))
            eindstationID = database.fetchOne(database.query("SELECT stationID FROM stations WHERE naam=\'%s\'" % eindstation))
            gebruikerID = database.fetchOne(database.query("SELECT gebruikerID FROM gebruikers WHERE ovnummer=%d" % ovnummer))
            print(beginstation,eindstation,beginstationID,eindstationID,gebruikerID)
            database.query("INSERT INTO reisgegevens(gebruikerID,beginstationID,eindstationID) VALUES ({0},{1},{2})".format(gebruikerID[0], beginstationID[0], eindstationID[0]))
            database.save()
        variable = StringVar(self)
        variable.set('Eindstation')
        station_lijst = genereer_stationlijst()
        om1 = OptionMenu(self, variable, *station_lijst, command=option_changed)
        B = tk.Button(self, text ="Volgende", bd = 5, width = 50, height = 4, command = save_and_show_voltooid, state = 'disabled')
        w = Label(self, text="Kies uw eindstation", font=('Arial', 20))

        w.pack()
        om1.place(x = 100, y = 100)
        om1.pack()
        B.place(x = 130, y = 300)
        B.pack()


class voltooidFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        w = Label(self, text="Uw reisgegevens is opgeslagen!", font=('Arial', 20))
        w.pack()
        w.place(x=170, y=150)

        #qr code genereren
        def generate_and_show_qr_code():
            img = qrcode.make("123")
            img.show()

        B = tk.Button(self, text ="Bekijk qr code", bd = 5, width = 50, height = 4, command = generate_and_show_qr_code)
        B.place(x = 130, y = 300)
        B.pack()

        # w = Label(self, image=img, font=('Arial', 20))
        # w.pack()
        # w.place(x=170, y=150)


app = reisDatabase()
app.geometry('600x400')
app.title('Ns overzicht')
app.mainloop()