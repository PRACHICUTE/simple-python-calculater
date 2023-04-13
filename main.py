from tkinter import*

window = Tk()
window.geometry("400x400")
window.title("simple calculator")

lbl1 =Label(window,text="enter 1st Number:")
lbl1.place(x=50,y=50)
          
lbl2 =Label(window,text="enter 2st Number:")
lbl2.place(x=50,y=100)

lbl3 =Label(window,text="Result:")
lbl3.place(x=70,y=150)

t1 =Entry()
t1.place(x=180,y=50)

t2 =Entry()
t2.place(x=180,y=100)

t3 =Entry()
t3.place(x=180,y=150)

def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum = num1+num2
t3.insert(END,str(sum))

b1 =Button(window, text="Add",command=add)
b1.place(x=50,y=200)


def sub():
  num1=int(t1.get())
  num2=int(t2.get())
  sub = num1+num2
t3.insert(END,str(sub))

b2 =Button(window, text="Subtract",command=sub)
b2.place(x=120,y=200)

def mul():
  num1=int(t1.get())
  num2=int(t2.get())
  mul = num1+num2
t3.insert(END,str(mul))

b3 =Button(window, text="Multiply",command=mul)
b3.place(x=220,y=200)

def div():
  num1=int(t1.get())
  num2=int(t2.get())
  div = num1+num2
t3.insert(END,str(div))

b4 =Button(window, text="Divide",command=div)
b4.place(x=320,y=200)

def clear():
  t1.delete(0,END)
  t2.delete(0,END)
  t3.delete(0,END)

b5 =Button(window, text="clear",command=clear)
b5.place(x=180,y=250)