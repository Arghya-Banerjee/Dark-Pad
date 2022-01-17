from mmap import mmap
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("960x540")
main_application.title("Dark Pad")

main_menu = tk.Menu()

file = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label= "File", menu= file)


# Adding File Menu drop-down list

file.add_command(label= "New File", compound= tk.LEFT, accelerator= "Ctrl+N")
file.add_command(label= "Open File", compound= tk.LEFT, accelerator= "Ctrl+O")
file.add_command(label= "Save File", compound= tk.LEFT, accelerator= "Ctrl+S")
file.add_command(label= "Save File As", compound= tk.LEFT, accelerator= "Ctrl+Alt+S")
file.add_command(label= "Exit File", compound= tk.LEFT, accelerator= "Alt+F4")


edit = tk.Menu(main_menu, tearoff= False)
main_menu.add_cascade(label= "Edit", menu= edit)


# Adding Edit Menu drop-down list

edit.add_command(label= "Copy", compound= tk.LEFT, accelerator= "Ctrl+C")
edit.add_command(label= "Cut", compound= tk.LEFT, accelerator= "Ctrl+X")
edit.add_command(label= "Paste", compound= tk.LEFT, accelerator= "Ctrl+V")
edit.add_command(label= "Clear All", compound= tk.LEFT)
edit.add_command(label= "Find", compound= tk.LEFT, accelerator= "Ctrl+F")





main_application.config(menu= main_menu)



main_application.mainloop()