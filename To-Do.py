import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x780")
root.configure(background = "white")

main = ttk.Frame(root)
main.grid()

title = tk.StringVar()
title.set("To-Do list:")

list = tk.StringVar()
list.set("")

t = tk.Label(textvariable = title, background = "white", foreground = "black", font = ("Helvetica", 20), pady=16, padx=16)
t.grid(column = 0, row = 0, columnspan = 1)

items = []

tk.inputtxt = tk.Text(root, height =1,
                   width = 25,
                   bg = "light grey")
tk.inputtxt.grid(column = 1, row = 0)

def addItem():
    input = tk.inputtxt.get("1.0", "end-1c")
    items.append(input)
    print(items)
    for x in items:
        pass
    tk.inputtxt.delete('1.0' ,tk.END)

blank = tk.Label(background = "white", pady=16, padx=16)
blank.grid(column = 2, row = 0)

addButton = tk.Button(text = "Add new item", command = addItem, bg = "white", fg = "black"
                   , activebackground = "gray", activeforeground = "black"
                   , font = ("Helvetica", 16)
                   , pady=10, padx=15)
addButton.grid(column = 3, row = 0)

root.mainloop()