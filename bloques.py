from tkinter import Frame, Label, Entry, Menu, filedialog
from editor import *
import json
import os

code = []

# Entry 

def setEntry(event):
    entry = event.widget
    entry.config(width=max(3, len(entry.get())))


def entrynum(texto):
    if texto in ("", "."):
        return True
    try:
        return float(texto) >= 0
    except ValueError:
        return False


def create_entry(parent, numeric=False):
    if numeric:
        validacion = parent.register(entrynum)
        entry = Entry(
            parent,
            width=3,
            validate="key",
            validatecommand=(validacion, "%P")
        )
    else:
        entry = Entry(parent, width=3)

    entry.bind("<KeyRelease>", setEntry)
    return entry


# Bloques

def clone_block(blockConsole, block_counter, block_info, value=""):
    block_counter["i"] += 1

    block = Frame(blockConsole, bg=block_info["color"])
    block.grid(row=block_counter["i"], column=0, padx=5, sticky="w")

    Label(
        block,
        text=block_info["type"],
        bg=block_info["color"]
    ).grid(row=0, column=0, padx=5, pady=5)

    entry = None

    if block_info["entry"]:
        entry = create_entry(block, numeric=block_info["numeric"])
        entry.insert(0, value)
        entry.grid(row=0, column=1, padx=5)

    block_data = (block_info, entry)
    code.append(block_data)

    # Click Izquierdo

    menu = Menu(block, tearoff=0)

    def delete_block():
        if block_data in code:
            code.remove(block_data)
        block.destroy()

    menu.add_command(label="Eliminar", command=delete_block)

    def show_menu(event):
        menu.tk_popup(event.x_root, event.y_root)

    block.bind("<Button-3>", show_menu)

    for widget in block.winfo_children():
        widget.bind("<Button-3>", show_menu)




def createBlocks(paleta, blockConsole, block_counter):

    for i, block in enumerate(BLOCKS):

        frame = Frame(paleta, bg=block["color"])
        frame.place(x=20, y=20 + i * 60)

        label = Label(frame, text=block["type"], bg=block["color"])
        label.grid(row=0, column=0, padx=5, pady=5)

        entry = None

        if block["entry"]:
            entry = create_entry(frame, block["numeric"])
            entry.grid(row=0, column=1, padx=5)

        label.bind("<Button-1>", lambda e, b=block, ent=entry: clone_block(blockConsole, block_counter, b, ent.get() if ent else ""))


# Save System

file_name = "untitled"


def New(blockConsole):
    global file_name
    for widget in blockConsole.winfo_children(): 
        widget.destroy()
    code.clear()
    file_name = "untitled"


def Save(VERSION):
    global file_name
    data = []
    for block_info, entry in code: 
        data.append({"type": block_info["type"], "value": entry.get() if entry else ""})
    file_path = filedialog.asksaveasfilename(initialfile=file_name, defaultextension=".bx", filetypes=[("BlockX", "*.bx")], title="Guardar como")
    if not file_path: return
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    project = {"file_name": file_name,"version": VERSION,"blocks": data}
    with open(file_path, "w", encoding="utf-8") as file: 
        json.dump(project, file)
    print("Saved proyect")


def Open(blockConsole, block_counter):
    global file_name

    # Ask file
    file_path = filedialog.askopenfilename(filetypes=[("BlockX", "*.bx")], title="Abrir")
    if not file_path: return

    #Open it
    for widget in blockConsole.winfo_children(): 
        widget.destroy()
    code.clear()

    with open(file_path, "r", encoding="utf-8") as file: 
        project = json.load(file)

    file_name = project["file_name"]
    data = project["blocks"]

    for bloque in data:
        for info in BLOCKS:
            if info["type"] == bloque["type"]:
                clone_block(blockConsole, block_counter, info, bloque["value"])
