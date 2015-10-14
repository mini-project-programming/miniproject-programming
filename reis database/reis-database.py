__author__ = 'Merlijn'

import qrcode
import tkinter as tk
from tkinter import *
from database import *

TITLE_FONT = ("Helvetica", 18, "bold")


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


class SampleApp(tk.Tk):

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
        for F in (StartPage, beginstationFrame, eindstationFrame, voltooidFrame):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):

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


class beginstationFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        station_lijst = genereer_stationlijst()

        def option_changed(a):
            if a != 'Beginstation':
                B.config(state='normal')
            else:
                B.config(state='disabled')

        variable1 = StringVar()
        variable1.set('default')

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
            if a != 'Beginstation':
                B.config(state='normal')
            else:
                B.config(state='disabled')

        variable1 = StringVar()
        variable1.set('default')

        variable = StringVar(self)
        variable.set('Eindstation')
        station_lijst = genereer_stationlijst()
        om1 = OptionMenu(self, variable, *station_lijst, command=option_changed)
        B = tk.Button(self, text ="Volgende", bd = 5, width = 50, height = 4, command = lambda: controller.show_frame(voltooidFrame), state = 'disabled')
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


app = SampleApp()
app.geometry('600x400')
app.title('Ns overzicht')
app.mainloop()