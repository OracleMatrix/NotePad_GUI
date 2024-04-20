from customtkinter import *
from tkinter import messagebox, Menu
from tkinter import filedialog

root = CTk()
root.title('NotePad')
root.geometry('600x600')


def change_theme():
    global theme
    if theme == 0:
        set_appearance_mode("dark")
        theme += 1
    else:
        set_appearance_mode("light")
        theme -= 1


theme_switch = CTkSwitch(root, text='Theme', command=change_theme)
theme_switch.pack(padx=10, pady=10)

text_box = CTkTextbox(root, corner_radius=15, width=570, height=570)
text_box.pack(fill='both', expand=True, padx=10, pady=10)
theme = 0


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_box.delete(1.0, END)
            text_box.insert(END, text)
    else:
        messagebox.showerror('Error', 'Please select a text file')


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            text_content = text_box.get(1.0, END)
            file.write(text_content)
    else:
        messagebox.showerror('Error', 'Please select a path to save the text file')


menubar = Menu(root)
root.config(menu=menubar)

optionmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Options', menu=optionmenu)

optionmenu.add_command(label='Open File', command=open_file)
optionmenu.add_separator()
optionmenu.add_command(label='Save File', command=save_file)

root.mainloop()
