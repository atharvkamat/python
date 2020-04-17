from tkinter import *
root = Tk()
root.title("CALCULATOR")
e =Entry(root,width=35,borderwidth = 5,justify=LEFT)
e.grid(row =0,column = 0,columnspan = 3,padx = 19,pady = 19)
def btadd0():
    i = e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(0))
def btadd1():
    i = e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(1))
def btadd2():
    i = e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(2))
def btadd3():
    i = e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(3))
def btadd4():
    i = e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(4))
def btadd5():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(5))
def btadd6():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(6))
def btadd7():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(7))
def btadd8():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(8))
def btadd9():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+str(9))
def ca():
    e.delete(0,END)
def add():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+"+")
def multi():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+"x")
def sub():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+"-")
def divi():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+"÷")
def eqq():
    i =e.get()
    t= i.find('+')
    yyt = '+'in i
    mm=i.find('x')
    mi='x' in i
    x='÷'in i
    xi=i.find('÷')
    subt='-' in i
    subti=i.find('-')
    z = len(i)
    yr= z+1
    if  i[-1]=='+':
        e.delete(0,END)
        e.insert(0,'Error')
    else:
        if yyt==True:
            e.delete(0,END)
            yi=t-1
            xi=t+1
            yiii=int(i[0:t])
            xiii =int(i[xi:yr])
            too= xiii+yiii
            print(too)
            e.insert(0,str(too))
        else:
            ititit=0

bt0 = Button(root,text = '0',padx = 40,pady=20,command = btadd0)
bt1 = Button(root,text = '1',padx = 40,pady=20,command = btadd1)
bt2 = Button(root,text = '2',padx = 40,pady=20,command = btadd2)
bt3 = Button(root,text = '3',padx = 40,pady=20,command = btadd3)
bt4 = Button(root,text = '4',padx = 40,pady=20,command = btadd4)
bt5 = Button(root,text = '5',padx = 40,pady=20,command = btadd5)
bt6 = Button(root,text = '6',padx = 40,pady=20,command = btadd6)
bt7 = Button(root,text = '7',padx = 40,pady=20,command = btadd7)
bt8 = Button(root,text = '8',padx = 40,pady=20,command = btadd8)
bt9 = Button(root,text = '9',padx = 40,pady=20,command = btadd9)

btadd = Button(root,text='+',padx=40,pady=20,command = add)
bteq = Button(root,text = '=',padx=90,pady = 20,command = eqq)
btcl=Button(root,text='AC',padx=85,pady=20,command = ca)
mx= Button(root,text ='x',padx=40,pady=20,command=multi)
subi= Button(root,text ='-',padx=40,pady=20,command=sub)
div= Button(root,text ='÷',padx=40,pady=20,command=divi)

bt1.grid(row=4,column=0)
bt2.grid(row=4,column=1)
bt3.grid(row=4,column=2)

bt4.grid(row=3,column=0)
bt5.grid(row=3,column=1)
bt6.grid(row=3,column=2)

bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)

bt0.grid(row=5,column=0)
btadd.grid(row= 6,column = 0)
bteq.grid(row=5,column=1,columnspan = 2)
btcl.grid(row=6,column=1,columnspan = 2)
#btdel.grid(row=1,column=0,columnspan= 3)
mx.grid(row=7,column=1)
subi.grid(row=7,column=0)
div.grid(row=7,column = 2)
root.mainloop()
