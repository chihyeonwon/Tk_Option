# Tk_Option
tkinter와 Python으로 옵션 선택하는 위젯 다루기   
   
구체적으로는 Listbox, Checkbutton, Radiobutton, Combobox, Spinbox, Scale 6개를 다뤄보도록 하겠습니다.

## Listbox

### 리스트박스는 Listbox()함수를 이용해서 만들 수 있습니다. 마찬가지로 pack()함수로 배치를 해줍니다.

Listbox.py
```python
lb = Listbox(win)
lb.pack()
```   
   
### 리스트박스 안에 컨텐츠를 넣을 때는 insert(위치, "내용") 함수를 사용합니다. 위치는 위에서부터 0,1,2,3 순으로 오름차순으로 들어가게됩니다.
```python
lb = Listbox(win)
lb.insert(0, "1번")
lb.insert(1, "2번")
lb.insert(2, "3번")
lb.insert(3, "4번")
lb.insert(4, "5번")
lb.pack()
```

### 리스트 박스의 컨텐츠를 다중 선택을 하고 싶을 때는 config의 옵션으로 selectmode의 값을 multiple을 주면 됩니다.
```python
lb = Listbox(win)
lb.config(selectmode="multiple")
lb.insert(0, "1번")
lb.insert(1, "2번")
lb.insert(2, "3번")
lb.insert(3, "4번")
lb.insert(4, "5번")
lb.pack()
```   

다음으로 버튼과 라벨을 만들어서 옵션을 선택하고 버튼을 누르면 라벨에 몇번째 옵션인지 표시되도록 해 보겠습니다.   
   
버튼과 라벨을 하나씩 만들어줍니다.
```python
# Button
btn = Button(win)
btn.config(text="옵션 선택")
btn.pack()

# Label
lab = Label(win)
lab.pack()
```   

버튼을 클릭하면 click 함수가 실행되도록 하고 현재 선택되있는 옵션의 인덱스를 추출하는 함수를 사용해서 몇 번째 옵션인지 출력하도록 해 보겠습니다.
```python
# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    text = lb.curselection()[0]
    lab.config(text="{}번 째를 선택하셨습니다.".format(int(text)+1))


btn.config(command=click)
btn.pack()
```

### 최종 코드와 프로그램 실행 화면   
   
최종 코드는 다음과 같습니다.

Listbox.py
```pytohn
from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Listbox
lb = Listbox(win)
# lb.config(selectmode="multiple")
lb.insert(0, "1번")
lb.insert(1, "2번")
lb.insert(2, "3번")
lb.insert(3, "4번")
lb.insert(4, "5번")
lb.pack()

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
```
프로그램의 초기화면입니다.   
![Listbox_init](https://user-images.githubusercontent.com/58906858/152482708-da76f81a-9d17-4c2e-9516-7083325db36d.png)   
   
2번째 옵션을 선택하고 옵션선택 버튼을 누르면 다음과 같이 몇번 째를 선택했는지 출력해줍니다.
![Listbox_use](https://user-images.githubusercontent.com/58906858/152482832-cc1e026d-51a0-4efe-b856-9fab29358fda.png)






## Chec kbutton

## Radiobutton

## Combobox

## Spinbox

## Scale
