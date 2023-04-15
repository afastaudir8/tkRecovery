# made bu 0x3ff and a fast audi r8

import tkinter
import subprocess
import platform

from tkinter import *
from tkinter import Tk, font
from tkinter import Menu

import time

from scripts import *


rootWin = Tk()
font.families()


# checkstatus = 1
# while checkstatus == 1:
#     devicestatus = deviceconnected()
# 
rootWin.title('tkRecovery (0x3ff, a fast audi r8)')
rootWin.geometry('500x175')

# tk gui defined items


def openNewWindow():
    infoWin = Toplevel(rootWin)
    infoWin.title("iDevice information")
    infoWin.geometry("250x175")
    label = Label(infoWin, text="iDevice information", font=('System', 16))
    label.pack()
    devicename = Label(infoWin, text="DEVICE_NAME", font=('System', 14))
    devicename.pack()
    model = Label(infoWin, text="iPhone model:", font=('System', 12))
    model.pack()
    modeln = Label(infoWin, text="MODEL", font=('System', 9))
    modeln.pack()
    serial = Label(infoWin, text="Serial Number:", font=('System', 12))
    serial.pack()
    serialn = Label(infoWin, text="SERIAL_NUM", font=('System', 9))
    serialn.pack()
    ios = Label(infoWin, text="iOS:", font=('System', 12))
    ios.pack()
    iosv = Label(infoWin, text="IOS_VERSION", font=('System', 9))
    iosv.pack()

def updatestatus():
    log.config(text=f'Status: {deviceconnected()}')
    rootWin.after(1000, updatestatus)

# tk gui
label = Label(rootWin, text="tkRecovery", font=('System', 24))
label.pack()
desc = Label(rootWin, text="Easy tool to make your iDevice enter/exit recovery.", font=('System', 13))
desc.pack()
desc2 = Label(rootWin, text="(Use it when restoring or jailbreaking your iDevice)", font=('System', 10))
desc2.pack()
log = Label(rootWin, text=f"Status: {deviceconnected()}", font=('System', 12))
log.pack()

EnterButton = Button(rootWin, text="Enter Recovery", command=enterrecovery)
EnterButton.pack()
ExitButton = Button(rootWin, text="Exit Recovery", command=exitrecovery)
ExitButton.pack()

menubar = Menu(rootWin)
rootWin.config(menu=menubar)

deviceinfo_menu = Menu(menubar)

deviceinfo_menu.add_command(
    label='Show iDevice information',
    command=openNewWindow
)

quit.add_command(
    label='Quit',
    command=rootWin.destroy
)

# cascade buttons
menubar.add_cascade(
    label="File",
    menu=quit
)

menubar.add_cascade(
    label="Tool",
    menu=deviceinfo_menu
)

updatestatus()
rootWin.mainloop()