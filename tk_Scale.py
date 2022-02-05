from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Scale
scale = Scale(win)
scale.config(length=1000, tickinterval=10, from_=0, to=50, orient="horizontal")
scale.pack()

# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    lab_text = scale.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
