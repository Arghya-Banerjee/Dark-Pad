import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import font, colorchooser, filedialog, messagebox

main_application = tk.Tk()
main_application.geometry("960x540")
main_application.title("Dark Pad")

main_menu = tk.Menu()

# Adding File Menu drop-down list

file = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label= "File", menu= file)


file.add_command(label= "New File", compound= tk.LEFT, accelerator= "Ctrl+N")
file.add_command(label= "Open File", compound= tk.LEFT, accelerator= "Ctrl+O")
file.add_command(label= "Save File", compound= tk.LEFT, accelerator= "Ctrl+S")
file.add_command(label= "Save File As", compound= tk.LEFT, accelerator= "Ctrl+Alt+S")
file.add_command(label= "Exit File", compound= tk.LEFT, accelerator= "Alt+F4")


# Adding Edit Menu drop-down list


edit = tk.Menu(main_menu, tearoff= False)
main_menu.add_cascade(label= "Edit", menu= edit)

edit.add_command(label= "Copy", compound= tk.LEFT, accelerator= "Ctrl+C")
edit.add_command(label= "Cut", compound= tk.LEFT, accelerator= "Ctrl+X")
edit.add_command(label= "Paste", compound= tk.LEFT, accelerator= "Ctrl+V")
edit.add_command(label= "Clear All", compound= tk.LEFT)
edit.add_command(label= "Find", compound= tk.LEFT, accelerator= "Ctrl+F")


# Adding View Menu
 
view = tk.Menu(main_menu, tearoff= False)
main_menu.add_cascade(label= "View", menu= view)

view.add_checkbutton(label= "Tool Bar", onvalue = True, offvalue = 0,compound= tk.LEFT)
view.add_checkbutton(label= "Status Bar", onvalue = True, offvalue = 0,compound= tk.LEFT)


# Adding Color Themes Menu

color_theme = tk.Menu(main_menu, tearoff= False)
main_menu.add_cascade(label = "Color Theme", menu = color_theme)

light_color_theme = tk.PhotoImage(file = "icon/White_ico.png")
dark_color_theme = tk.PhotoImage(file = "icon/Black_ico.png")


color_icons = (light_color_theme, dark_color_theme)

color_dict = {
    "Light" : {'#000000', '#ffffff'},
    "Dark" : {'#363630', '#000000'}
}

count = 0

for i in color_dict:

    color_theme.add_radiobutton(label = i, image = color_icons[count], compound= tk.LEFT)
    count =+ 1


# tool bar

tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP, fill = tk.X)


# font box

font_tuple = tk.font.families()
font_family = tk.StringVar
font_box = ttk.Combobox(tool_bar_label, width = 30, textvariable= font_family, state= 'readonly')
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Times New Roman"))
font_box.grid(row= 0, column= 0, padx = 5)


# size box

size_variables = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width = 20, textvariable= size_variables, state= 'readonly')
font_size["values"] = tuple(range(8,100,2))
font_size.current(14)
font_size.grid(row= 0, column= 0, padx = 5)



main_application.config(menu= main_menu)

main_application.mainloop()