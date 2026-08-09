from tkinter import Tk, Frame, Button, Menu
import tkinter as tk
from bloques import createBlocks, code, Play, Save, New, Open
import os


VERSION = "0.2.2"

# ======== Window ======== #

window = Tk()
window.title("BlockX")
window.geometry("800x500")
icon = tk.PhotoImage(file="imgs/logo2.png")
window.iconphoto(True, icon)

# ======== Menu ======== #

barMenu = Menu(window)
window.config(menu=barMenu)

# File
fileMenu = Menu(barMenu, tearoff=0)
fileMenu.add_command(label="New", command=lambda:New(blockConsole))
fileMenu.add_command(label="Save as", command=lambda:Save(VERSION))
fileMenu.add_command(label="Open", command=lambda:Open(blockConsole, block_counter))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=lambda:window.quit())
# Info
infoMenu = Menu(barMenu, tearoff=0)
infoMenu.add_command(label="Version", command=lambda:print(VERSION))
infoMenu.add_command(label="Credits", command=lambda:print("Amadeo Malko Rivadeneira"))
infoMenu.add_command(label="License", command=lambda:print("Mozilla Public License, v. 2.0"))
# Console
consoleMenu = Menu(barMenu, tearoff=0)
def Clear():
    if os.name == "nt": #Windows
        os.system("cls")
    elif os.name == "posix": #Linux/Mac
        os.system("clear")
consoleMenu.add_command(label="Clear", command=lambda:Clear())

barMenu.add_cascade(label="File", menu=fileMenu)
barMenu.add_cascade(label="Info", menu=infoMenu)
barMenu.add_cascade(label="Console", menu=consoleMenu)

# ======== Paleta ======== #

paleta = Frame(window, bg="grey", width=200)
paleta.place(x=0, y=0, relheight=1.0)
paleta.config(borderwidth=10, relief="raised")
paleta.grid_propagate(False)
blockConsole = Frame(window, bg="white")
blockConsole.place(x=200, y=0, relwidth=1.0, relheight=1.0, anchor="nw")

block_counter = {"i": 0}
createBlocks(paleta, blockConsole, block_counter)

play = Button(window, text="▶️", command=lambda:Play(code), bg="grey")
play.pack(anchor="ne")

window.mainloop()
