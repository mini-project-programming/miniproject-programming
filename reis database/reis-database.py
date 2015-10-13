__author__ = 'Merlijn'

import sqlite3,qrcode
import tkinter as tk

def windows():
    window = tk.Tk()
    window.geometry('600x400')
    print(E2.get())

window = tk.Tk()
window.geometry('600x400')
window.title('Ns overzicht')
window.configure(background='yellow')

T = tk.Text(window, height=2, width = 30, bg = 'yellow')
T.insert('end', 'Dit is tekst :D')

def callback(sv):
    print(E2.get())
sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

E1 = tk.Label(window, text="UserID", bg = 'yellow')
E2 = tk.Entry(window, textvariable=sv)

B = tk.Button(window, text ="Continue", bd = 5, width = 50, height = 4, bg = 'yellow', activebackground = 'yellow', command = windows, state = 'disabled')


T.pack()
E1.pack()
E2.pack()
B.pack()
T.place(x = 190)
E1.place(x = 150, y = 200)
E2.place(x = 190, y = 200)
B.place(x = 130, y = 300)
window.mainloop()


#qr code genereren
img = qrcode.make("123")
 