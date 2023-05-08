
import tkinter as tk 
from tkinter import *
import os 
from time import strftime

root = tk.Tk()
root.title('My Clock')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background = '#008080')


def get_greetings():
    name_user = os.getlogin()
    greetings.config(text = 'Hello! ' + name_user )

def get_date():
    current_date = strftime(' %a, %d %b %Y')
    date.config(text = current_date)

def get_time():
    current_time = strftime('%H:%M:%S')
    time.config(text = current_time)
    time.after(1000, get_time)


screen = tk.Canvas(root, width=600, height=60, bg='#008080', bd=0, highlightthickness=0, relief='ridge')
screen.pack()

greetings = Label(root, bg='#008080', fg='#1C1C1C', font=('Bauhau 93 Regular', 16))
greetings.pack()

date = Label(root, bg='#008080', fg='#1C1C1C', font=('Bauhau 93 Regular', 14))
date.pack(pady=2)

time = Label(root, bg='#008080', fg='#1C1C1C', font=('Bauhau 93 Regular', 70))
time.pack(pady=2)

get_greetings()
get_date()
get_time()
root.mainloop()