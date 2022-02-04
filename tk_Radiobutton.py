from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Radiobutton
rv = IntVar()
rb = Radiobutton(win, text="1번", variable=rv)
rb.pack()

# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    text = cv.get()
    print(text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
