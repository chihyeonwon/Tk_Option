from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Scale
scale = Scale(win)
scale.config(from_=50, to=0)
scale.pack()

# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    lab_text = sb.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
