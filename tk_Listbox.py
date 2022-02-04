from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Listbox
lb = Listbox(win)
lb.config(selectmode="multiple")
lb.insert(0, "1번")
lb.insert(1, "2번")
lb.insert(2, "3번")
lb.insert(3, "4번")
lb.insert(4, "5번")
lb.pack()

# Button
btn = Button(win)
btn.config(text="옵션 선택")
btn.pack()

win.mainloop()
