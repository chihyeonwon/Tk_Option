from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Radiobutton
rv = IntVar()
rb1 = Radiobutton(win, text="1번", variable=rv)
rb2 = Radiobutton(win, text="2번", variable=rv)
rb3 = Radiobutton(win, text="3번", variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()

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
