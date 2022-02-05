from tkinter import *
from tkinter .ttk import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Combobox
cb_list = ["1", "2", "3"]
cb = Combobox(win)
cb.config(values=cb_list)
cb.pack()

# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    lab_text = rv.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
