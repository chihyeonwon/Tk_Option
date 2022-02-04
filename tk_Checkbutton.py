from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")

# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    text = lb.curselection()[0]
    lab.config(text="{}번 째를 선택하셨습니다.".format(int(text)+1))


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
