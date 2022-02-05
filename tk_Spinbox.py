from tkinter import *
from tkinter .ttk import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Spinbox
sb = Spinbox(win)
sb.config(from_=-1, to=1)
sb.pack()
# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    lab_text = cb.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
