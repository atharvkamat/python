
from tkinter import *
import tkinter.font as font
root = Tk()
root.title("CALCULATOR")
myfont = font.Font(size = 30)
e =Entry(root,width=20,borderwidth = 4,bg='red',fg='#ffffff')
e['font']=myfont
e.grid(row =0,column = 0,columnspan = 4,padx =40 ,pady = 19)
def btdt():
    i = e.get()
    e.delete(0,END)
    e.insert(0,str(i)+".")
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
def ce():
    i = e.get()
    e.delete(0,END)
    y=len(i)-1
    r= slice(y)
    e.insert(0,i[r])
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
def delall():
    e.delete(0,END)
def eqq():
    i =e.get()
    z = len(i)
    mi='x' in i
    x='÷'in i
    yyt = '+'in i
    subt='-' in i
    mm=i.find('x')
    xio=i.find('÷')
    subti=i.find('-')
    t=i.find('+')
    deti='.'in i
    dot=i.find('.')
    yr= z+1
    if  i[-1]=='+':
        e.delete(0,END)
        e.insert(0,'Error')
    elif i[0]=='+':
        e.delete(0,END)
        e.insert(0,'Error')
    else:
        if yyt==True:
            e.delete(0,END)
            xi=t+1
            if deti==True:
                yiii=float(i[0:t])
                xiii =float(i[xi:yr])
                too= yiii+xiii
                print(too)
                e.insert(0,str(too))
            else:
                yiii=int(i[0:t])
                xiii =int(i[xi:yr])
                too= yiii+xiii
                print(too)
                e.insert(0,str(too))
        else:
            ititit=0

    if i[-1]=='-':
        e.delete(0,END)
        e.insert(0,'Error')
    elif i[0]=='-':
        e.delete(0,END)
        e.insert(0,'Error')
    else:
        if subt==True:
            e.delete(0,END)
            xi=subti
            if deti==True:
                yiii=float(i[0:t])
                xiii =float(i[xi:yr])
                too= yiii-xiii
                print(too)
                e.insert(0,str(too))
            else:
                yiii=int(i[0:t])
                xiii =int(i[xi:yr])
                too= yiii-xiii
                print(too)
                e.insert(0,str(too))
        else:
            aitiitrt=0
    if i[-1]=='x':
        e.delete(0,END)
        e.insert(0,'Error')
    elif i[0]=='x':
        e.delete(0,END)
        e.insert(0,'Error')
    else:
        if mi==True:
            e.delete(0,END)
            xi=mm+1
            if deti==True:
                yiii=float(i[0:t])
                xiii =float(i[xi:yr])
                too= yiii*xiii
                print(too)
                e.insert(0,str(too))
            else:
                yiii=int(i[0:t])
                xiii =int(i[xi:yr])
                too= yiii*xiii
                print(too)
                e.insert(0,str(too))
        else:
            vaitiitrt=0

    if i[-1]=='÷':
        e.delete(0,END)
        e.insert(0,'Error')
    elif i[0]=='÷':
        e.delete(0,END)
        e.insert(0,'Error')
    else:
        if x==True:
            e.delete(0,END)
            xi=xio+1
            if deti==True:
                yiii=float(i[0:t])
                xiii =float(i[xi:yr])
                too= yiii/xiii
                print(too)
                e.insert(0,str(too))
            else:
                yiii=int(i[0:t])
                xiii =int(i[xi:yr])
                too= yiii/xiii
                print(too)
                e.insert(0,str(too))
        else:
            aittiitrt=0

bt0 = Button(root,text = '0',padx = 40,pady=20,command = btadd0,bg='red',fg='#ffffff')
bt1 = Button(root,text = '1',padx = 40,pady=20,command = btadd1,bg='red',fg='#ffffff')
bt2 = Button(root,text = '2',padx = 40,pady=20,command = btadd2,bg='red',fg='#ffffff')
bt3 = Button(root,text = '3',padx = 40,pady=20,command = btadd3,bg='red',fg='#ffffff')
bt4 = Button(root,text = '4',padx = 40,pady=20,command = btadd4,bg='red',fg='#ffffff')
bt5 = Button(root,text = '5',padx = 40,pady=20,command = btadd5,bg='red',fg='#ffffff')
bt6 = Button(root,text = '6',padx = 40,pady=20,command = btadd6,bg='red',fg='#ffffff')
bt7 = Button(root,text = '7',padx = 40,pady=20,command = btadd7,bg='red',fg='#ffffff')
bt8 = Button(root,text = '8',padx = 40,pady=20,command = btadd8,bg='red',fg='#ffffff')
bt9 = Button(root,text = '9',padx = 40,pady=20,command = btadd9,bg='red',fg='#ffffff')

btadd = Button(root,text='+',padx=38,pady=20,command = add,bg='red',fg='#ffffff')
bteq = Button(root,text = '=',padx=40,pady = 20,command = eqq,bg='red',fg='#ffffff')
btcl=Button(root,text='AC',padx=90,pady=10,command = delall,bg='red',fg='#ffffff')
btpl=Button(root,text='CE',padx=90,pady=10,command = ce,bg='red',fg='#ffffff')
mx= Button(root,text ='x',padx=40,pady=20,command=multi,bg='red',fg='#ffffff')
subi= Button(root,text ='-',padx=45,pady=20,command=sub,bg='red',fg='#ffffff')
div= Button(root,text ='÷',padx=40,pady=20,command=divi,bg='red',fg='#ffffff')
dotti = Button(root,text = '.',padx = 45,pady=20,command = btdt,bg='red',fg='#ffffff')


btcl['font']=myfont
btpl['font']=myfont
bt0['font']=myfont
bt1['font']=myfont
bt2['font']=myfont
bt3['font']=myfont
bt4['font']=myfont
bt5['font']=myfont
bt6['font']=myfont
bt7['font']=myfont
bt8['font']=myfont
bt9['font']=myfont
dotti['font']=myfont
bteq['font']=myfont
mx['font']=myfont
subi['font']=myfont
div['font']=myfont
btadd['font']=myfont
btcl.grid(row = 1,column =0,columnspan = 2)
btpl.grid(row = 1,column =2,columnspan = 2)

bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)
btadd.grid(row=2,column = 3)

bt4.grid(row=3,column=0)
bt5.grid(row=3,column=1)
bt6.grid(row=3,column=2)
subi.grid(row=3,column=3)

bt1.grid(row=4,column=0)
bt2.grid(row=4,column=1)
bt3.grid(row=4,column=2)
div.grid(row = 4,column= 3)

bt0.grid(row = 5,column=0)
dotti.grid(row=5,column=1)
bteq.grid(row = 5,column =2)
mx.grid(row =5,column= 3)




root.mainloop()
