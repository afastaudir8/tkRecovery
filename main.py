import tkinter
import subprocess

from tkinter import *
from tkinter import Tk, font
rootWin = Tk()
font.families()

rootWin.title('tkRecovery (0x3ff, a fast audi r8)')
rootWin.geometry('500x175')

def enter1():
    log["text"] = "Status: ENTER_STATUS"

def exit1():
    log["text"] = "Status: EXIT_STATUS"

def enter():
    log['text'] = 'Status: Performing action...'
    rootWin.after(2000, enter1)
    log.config( fg= "green")

def exit():
    log['text'] = 'Status: Performing action...'
    rootWin.after(2000, exit1)
    log.config( fg= "red")

label = Label(rootWin, text="tkRecovery", font=('System', 24))
label.pack()
desc = Label(rootWin, text="Easy tool to make your iDevice enter/exit recovery.", font=('System', 13))
desc.pack()
desc2 = Label(rootWin, text="(Use it when restoring or jailbreaking your iDevice)", font=('System', 10))
desc2.pack()
log = Label(rootWin, text="Status: nil", font=('System', 12))
log.pack()
EnterButton = Button(rootWin, text="Enter Recovery", command=enter)
EnterButton.pack()
ExitButton = Button(rootWin, text="Exit Recovery", command=exit)
ExitButton.pack()

rootWin.mainloop()