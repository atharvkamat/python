from tkinter import *
root = Tk()
root.title("CALCULATOR")
e =Entry(root,width=35,borderwidth = 5)
e.grid(row =0,column = 0,columnspan = 3,padx = 19,pady = 19)

def btadd(num):
    i = e.get()
    e.delete(num,END)
    e.insert(0,str(i)+str(num))
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
    e.delete(0)
def add():
    i =e.get()
    e.delete(0,END)
    e.insert(0,str(i)+"+")
def eqq():
    i =e.get()
    e.delete(0,END)
    r = len(i)
    i = r- 1
    if r[-1]=='+':
        print("outlook")


def create_buttons(buttons):
    for ( i in range (0,num)):
        print("creating button {0}".format(i))
        bt['name'] = str(i)
        bt['btn'] = Button(root,text = str(i),padx = 40,pady=20,command = btadd(i))
        buttons.append(i,bt)
    bt['name'] = "add"
    bt['btn'] = Button(root,text = str(i),padx = 40,pady=20,command = btadd(i))
    

'''         
bt0 = Button(root,text = '0',padx = 40,pady=20,command = btadd(0))
bt1 = Button(root,text = '1',padx = 40,pady=20,command = btadd(1))
bt2 = Button(root,text = '2',padx = 40,pady=20,command = btadd(2))
bt3 = Button(root,text = '3',padx = 40,pady=20,command = btadd(3))
bt4 = Button(root,text = '4',padx = 40,pady=20,command = btadd(4))
bt5 = Button(root,text = '5',padx = 40,pady=20,command = btadd(5))
bt6 = Button(root,text = '6',padx = 40,pady=20,command = btadd(6))
bt7 = Button(root,text = '7',padx = 40,pady=20,command = btadd(7))
bt8 = Button(root,text = '8',padx = 40,pady=20,command = btadd(8))
bt9 = Button(root,text = '9',padx = 40,pady=20,command = btadd(9))
'''
btadd = Button(root,text='+',padx=39,pady=20,command = add)
bteq = Button(root,text = '=',padx=90,pady = 20,command = eqq)
btcl=Button(root,text='CA',padx=85,pady=20,command = ca)

bt1.grid(row=3,column=0)
bt2.grid(row=3,column=1)
bt3.grid(row=3,column=2)

bt4.grid(row=2,column=0)
bt5.grid(row=2,column=1)
bt6.grid(row=2,column=2)

bt7.grid(row=1,column=0)
bt8.grid(row=1,column=1)
bt9.grid(row=1,column=2)

bt0.grid(row=4,column=0)
btadd.grid(row= 5,column = 0)
bteq.grid(row=4,column=1,columnspan = 2)
btcl.grid(row=5,column=1,columnspan = 2)
root.mainloop()
