# Tk_Option
tkinter와 Python으로 옵션 선택하는 위젯 다루기   
   
구체적으로는 Listbox, Checkbutton, Radiobutton, Combobox, Spinbox, Scale 6개를 다뤄보도록 하겠습니다.

## Listbox

### 리스트박스는 Listbox()함수를 이용해서 만들 수 있습니다.   
   
마찬가지로 pack()함수로 배치를 해줍니다.

Listbox.py
```python
lb = Listbox(win)
lb.pack()
```   
   
### 리스트박스 안에 컨텐츠를 넣을 때는 insert(위치, "내용") 함수를 사용합니다.   
   
위치는 위에서부터 0,1,2,3 순으로 오름차순으로 들어가게됩니다.
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

## Checkbutton

### CheckButton는 CheckButton 함수를 이용해서 만들 수 있습니다.
```python
cb = CheckBox(win)
cb.config(text="1번")
cb.pack()
```   
### CheckButton은 Listbox와는 다르게 변수하나에 하나의 위젯(옵션)을 저장할 수 있습니다.
체크버튼을 3개를 만들려면 변수 3개를 선언해서 각각 체크버튼을 생성해줘야합니다.
```python
cb1 = CheckBox(win, text="1번")
cb2 = CheckBox(win, text="1번")
cb3 = CheckBox(win, text="1번")
cb1.pack()
cb2.pack()
cb3.pack()
```  

### CheckButton의 체크유무를 구분해주는 함수 IntVar()를 사용합니다.

cv 변수에 IntVar() 함수를 저장하고 get 함수로 cv 클래스 안의 값을 꺼내오기 위해 get 함수로 출력을 해봅니다.
```python
# Checkbutton
cv = IntVar() # 클릭한상태를 정수의 형태로 저장합니다.
cb = Checkbutton(win, text="1번", variable=cv)
cb.pack()

# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    text = cv.get() # cv 클래스 안의 값을 꺼내오기위해 get 함수를 사용
    print(text) # 꺼내온 값을 출력


btn.config(command=click)
btn.pack()
```
옵션을 클릭하지 않았을 때 0을 옵션을 클릭했을 때 1을 출력하는 것을 알 수 있습니다.

### 최종코드와 프로그램 실행화면

최종코드는 다음과 같습니다.

tk_Checkbutton.py
```python
from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Checkbutton
cv = IntVar()
cb = Checkbutton(win, text="1번", variable=cv)
cb.pack()

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
```

프로그램 실행화면은 다음과 같습니다.

![Checkbutton](https://user-images.githubusercontent.com/58906858/152485445-8dfcb0a8-2459-47db-aba8-6ead4c57bae4.png)   
반환되는 값 0과 1을 사용해서 다양한 응용이 가능합니다.   

## Radiobutton

### 라디오버튼은 체크버튼과 만드는 방법은 유사하나 여러가지 옵션이 있을 때 그 중 하나를 선택한다는 차이가 있습니다.   

Radiobutton을 생성하고 Checkbutton과 마찬가지로 IntVar()함수를 사용해서 cv에 저장한후 variable옵션으로 줍니다.
```python
# Radiobutton
rv = IntVar()
rb = Radiobutton(win, text="1번", variable=rv)
rb.pack()
```   
   
변수 3개에 각각 다른 라디오버튼을 생성해줍니다.
```python
# Radiobutton
rv = IntVar()
rb1 = Radiobutton(win, text="1번", variable=rv)
rb2 = Radiobutton(win, text="2번", variable=rv)
rb3 = Radiobutton(win, text="3번", variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()
```

하지만 이렇게 구성하면 겉보기로는 구분이 되어있지만 내부적으로는 구분이 되어있지않아 옵션하나를 선택하면 모두 선택이 됩니다.   
   
변수는 rv 하나만 사용해서 같은 항목으로 묶고 각각의 옵션을 구분하기 위해서 value옵션의 값을 다르게 줍니다.
```python
# Radiobutton
rv = IntVar()
rb1 = Radiobutton(win, text="1번", value=0, variable=rv)
rb2 = Radiobutton(win, text="2번", value=1, variable=rv)
rb3 = Radiobutton(win, text="3번", value=2, variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()
```

버튼을 눌렀을 때 라벨에 반환값을 출력하도록 해보면
```python
# Button
btn = Button(win)
btn.config(text="옵션 선택")


def click():
    lab_text = rv.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()
```
RadioButton함수의 value옵션 값으로 지정한 값이 출력되는 것을 알 수 있습니다.

### 최종코드와 프로그램 실행

최종코드는 다음과 같습니다.
```python
from tkinter import *
win = Tk()
win.geometry("500x500")
win.option_add("*Font", "Arial, 20")
# Radiobutton
rv = IntVar()
rb1 = Radiobutton(win, text="1번", value=0, variable=rv)
rb2 = Radiobutton(win, text="2번", value=1, variable=rv)
rb3 = Radiobutton(win, text="3번", value=2, variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()

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
```
   
프로그램 실행 초기화면은 다음과 같습니다.   
![Radiobutton_init](https://user-images.githubusercontent.com/58906858/152487429-bdd77fff-3da1-47b4-9bef-1347cb8f581d.png)

옵션을 선택하고 옵션선택을 누르면 다음과 같이 value옵션에 저장한 값이 출력되는 것을 알 수 있습니다.
![Radiobutton_value](https://user-images.githubusercontent.com/58906858/152487573-c5229c2e-28ab-4f3d-ae81-cd882b8ca4bf.png)

## Combobox
   
### 콤보박스는 tkinter의 세부적인 .ttk 안에 있으므로 이를 import를 해줍니다.
```python
from tkinter .ttk import *
```
   
콤보박스를 생성하기 위해 Combobox 함수를 이용하고 배치해줍니다.
```python
cb = Combobox(win)
cb.pack()
```

### 콤보 박스에 내용을 넣을 때는 리스트를 사용합니다.
  
리스트를 만들고 config의 values 옵션으로 만든 리스트를 넣어줍니다.
```python
cb_list = ["1", "2", "3"]
cb = Combobox(win)
cb.config(values=cb_list)
cb.pack()
```
### 콤보 박스의 어떤 내용이 클릭됬는 지 알아보기 위해서는 get 함수를 사용합니다.
   
옵션 선택 버튼의 함수안에 위젯(cb)에 get 함수를 사용해서 리스트에 넣은 내용을 출력할 수 있습니다.
```python
def click():
    lab_text = cb.get()
    lab.config(text=lab_text)
```

### 최종 코드와 프로그램 실행 화면

최종 코드는 다음과 같습니다.
```python
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
    lab_text = cb.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
```
프로그램 실행 초기화면은 다음과 같습니다.   
   
![Combobox_init](https://user-images.githubusercontent.com/58906858/152632475-e4f22993-8c5e-49a4-a723-e36cfee12b34.png)   
   
클릭하여 옵션 1을 선택하고 옵션선택 버튼을 누르면 버튼 밑에 1이 정상적으로 출력되는 것을 알 수 있습니다.
![Combobox_use](https://user-images.githubusercontent.com/58906858/152632478-17ab3f18-45e4-4cdf-93f4-48f97432ae6e.png)

## Spinbox

### Spinbox 함수를 사용해서 위젯을 만들고 배치합니다.
```python
sb = Spinbox(win)
sb.pack()
```

### 만들기만 하면 아무내용이 없으므로 최대치와 최소치를 config의 from_, to 옵션으로 설정합니다.
```python
sb = Spinbox(win)
sb.config(from_=-1, to=1)
sb.pack()
```

### 선택한 수치를 출력하는 것은 get함수를 사용합니다.
   
get 함수를 사용해서 선택한 수치를 라벨에 출력합니다.
```python
def click():
    lab_text = sb.get()
    lab.config(text=lab_text)
```

### 최종코드와 프로그램 실행 화면

최종코드는 다음과 같습니다.
```python
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
    lab_text = sb.get()
    lab.config(text=lab_text)


btn.config(command=click)
btn.pack()

# Label
lab = Label(win)
lab.pack()
win.mainloop()
```

프로그램 초기 실행 화면은 다음과 같습니다.   
   
![Spinbox_init](https://user-images.githubusercontent.com/58906858/152632760-415fb41f-221a-4ee9-b789-95310a56a798.png)
   
옵션을 -1로 선택하고 옵션선택 버튼을 클릭하면 밑에 위치한 라벨에 정상적으로 출력되는 것을 알 수 있습니다.
![Spinbox_use](https://user-images.githubusercontent.com/58906858/152632779-92af64f3-c9d5-4223-8293-a59d0595de77.png)

## Scale
   
### Scale 함수를 사용해서 생성하고 배치합니다.
```python
scale=Scale(win)
scale.pack()
```

### Scale안의 수치의 범위는 from_, to 를 사용해서 바꿀 수 있습니다.
```python
# Scale
scale = Scale(win)
scale.config(from_=50, to=0)
scale.pack()
```
### Scale의 방향을 수평으로 바꾸려면 orient옵션을 "horizontal"로 설정합니다.

Scale은 기본적으로는 수직으로 배치되어있습니다.   
   
수평으로 바꾸려면 config 옵션의 orient 값을 "horizontal"로 설정하면 됩니다.
```python
# Scale
scale = Scale(win)
scale.config(from_=0, to=50, orient="horizontal")
scale.pack()
```
### 특정 수치를 표시할 때는 tickinterval 옵션을 설정합니다.

0부터 100까지 10 간격으로 수치를 표시하려면 다음과 같습니다.
```python
scale.config(length=1000, tickinterval=10, from_=0, to=50, orient="horizontal")
```
실행화면은 다음과 같습니다.
![Scale_tickinterval](https://user-images.githubusercontent.com/58906858/152633130-eb52d57e-89ab-48f2-bc27-d3bde3108d08.png)   
   
### 선택한 수치를 출력하기 위해서 get 함수를 사용합니다.

옵션 버튼을 클릭했을 때 선택한 수치를 클릭하기 위해서 get함수를 사용합니다.
```python
def click():
    lab_text = scale.get()
    lab.config(text=lab_text)
```

### 최종코드와 프로그램 실행 화면
  
최종코드는 다음과 같습니다.
```python
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
```
   
프로그램 실행 화면은 다음과 같습니다.   
   
   
![Scale_init](https://user-images.githubusercontent.com/58906858/152633220-3590b87d-b744-4b54-b309-e7f67d0017e9.png)   
   
수치를 지정하고 옵션버튼을 누르면 라벨에 지정한 수치가 정상적으로 출력됩니다.
![Scale_use](https://user-images.githubusercontent.com/58906858/152633227-43448c1f-149f-474d-979d-9f4d78c6bc90.png)


#### 이렇게 6개의 옵션을 지정하는 위젯들에 대해서 정리해보았습니다. 최종 수정 2022-02-05
