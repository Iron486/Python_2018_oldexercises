from tkinter import *
finestra = Tk()
finestra.geometry('600x600+100+100')
cc1=0
dd1=0
cc2=0
dd2=1
cc3=0
dd3=2
cc4=1
dd4=0
cc5=1
dd5=1
cc6=1
dd6=2
cc7=2
dd7=0
cc8=2
dd8=1
x=2
y=2
Labeln=Label(finestra,text=' ',fg='red',font=("Helvetica",15))
n=Labeln.grid(row=x,column=y)
def button1_change():
    global x,y,cc1,dd1,n
    if (x==cc1+1 and y==dd1) or (x==cc1-1 and dd1==k) or (x==cc1 and y==dd1-1) or (x==cc1 and y==dd1+1):
        b1=button1.grid(row=x,column=y)
        n=Labeln.grid(row=cc1,column=dd1)
        x=cc1
        y=dd1
        cc1=x
        dd1=y
        return x,y,cc1,dd1,n

def button2_change():
    global x,y,cc2,dd2,n    
    if (x==cc2+1 and y==dd2) or (x==cc2-1 and y==dd2) or (x==cc2 and y==dd2-1) or (x==cc2 and y==dd2+1):
        b2=button2.grid(row=x,column=y)
        n=Labeln.grid(row=cc2,column=dd2)
        x=cc2
        y=dd2
        cc1=x
        dd1=y
        return x,y,cc2,dd2,n

def button3_change():
    global x,y,cc3,dd3,n
    if (x==cc3+1 and y==dd3) or (x==cc3-1 and y==dd3) or (x==cc3 and y==dd3-1) or (x==cc3 and y==dd3+1):
        b3=button3.grid(row=x,column=y)
        n=Labeln.grid(row=cc3,column=dd3)
        x=cc3
        y=dd3
        cc3=x
        dd3=y
        return x,y,cc3,dd3,n

def button4_change():
    global x,y,cc4,dd4,n
    if (x==cc4+1 and y==dd4) or (x==cc4-1 and y==dd4) or (x==cc4 and y==dd4-1) or (x==cc4 and y==dd4+1):
        b4=button4.grid(row=x,column=y)
        n=Labeln.grid(row=cc4,column=dd4)
        x=cc4
        y=dd4
        cc4=x
        dd4=y
        return x,y,cc4,dd4,n

def button5_change():
    global x,y,cc5,dd5,n
    if (x==cc5+1 and y==dd5) or (x==cc5-1 and y==dd5) or (x==cc5 and y==dd5-1) or (x==cc5 and y==dd5+1):
        b5=button5.grid(row=x,column=y)
        n=Labeln.grid(row=cc5,column=dd5)
        x=cc5
        y=dd5
        cc5=x
        dd5=y
        return x,y,cc5,dd5,n

def button6_change():
    global x,y,cc6,dd6,n
    if (x==cc6+1 and y==dd6) or (x==cc6-1 and y==dd6) or (x==cc6 and y==dd6-1) or (x==cc6 and y==dd6+1):
        b6=button6.grid(row=x,column=y)
        n=Labeln.grid(row=cc6,column=dd6)
        x=cc6
        y=dd6
        cc6=x
        dd6=y
        return x,y,cc6,dd6,n

def button7_change():
    global x,y,cc7,dd7,n
    if (x==cc7+1 and y==dd7) or (x==cc7-1 and y==dd7) or (x==cc7 and y==dd7-1) or (x==cc7 and y==dd7+1):
        b7=button7.grid(row=x,column=y)
        n=Labeln.grid(row=cc7,column=dd7)
        x=cc7
        y=dd7
        cc7=x
        dd7=y
        return x,y,cc7,dd7,n

def button8_change():
    global x,y,cc8,dd8,n
    if (x==cc8+1 and y==dd8) or (x==cc8-1 and y==dd8) or (x==cc8 and y==dd8-1) or (x==cc8 and y==dd8+1):
        b8=button8.grid(row=x,column=y)
        n=Labeln.grid(row=cc8,column=dd8)
        x=cc8
        y=dd8
        cc8=x
        dd8=y
        return x,y,cc8,dd8,n          
button1=Button(finestra,text='1',command=button1_change,fg='red',font=("Helvetica",15))
b1=button1.grid(row=cc1,column=dd1)

button2=Button(finestra,text='2',command=button2_change,fg='red',font=("Helvetica",15))
b2=button2.grid(row=cc2,column=dd2)

button3=Button(finestra,text='3',command=button3_change,fg='red',font=("Helvetica",15))
b3=button3.grid(row=cc3,column=dd3)

button4=Button(finestra,text='4',command=button4_change,fg='red',font=("Helvetica",15))
b4=button4.grid(row=cc4,column=dd4)

button5=Button(finestra,text='5',command=button5_change,fg='red',font=("Helvetica",15))
b5=button5.grid(row=cc5,column=dd5)

button6=Button(finestra,text='6',command=button6_change,fg='red',font=("Helvetica",15))
b6=button6.grid(row=cc6,column=dd6)

button7=Button(finestra,text='7',command=button7_change,fg='red',font=("Helvetica",15))
b7=button7.grid(row=cc7,column=dd7)

button8=Button(finestra,text='8',command=button8_change,fg='red',font=("Helvetica",15))
b8=button8.grid(row=cc8,column=dd8)
finestra.mainloop()    
    

