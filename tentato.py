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
Labeln=Label(finestra,text=' ',fg='red',bg="black",font=("Helvetica",15))
n=Labeln.grid(row=x,column=y)

button1=Label(finestra,text='1',fg='red',bg="black",font=("Helvetica",15))
b1=button1.grid(row=cc1,column=dd1)

button2=Label(finestra,text='2',fg='red',bg="black",font=("Helvetica",15))
b2=button2.grid(row=cc2,column=dd2)

button3=Label(finestra,text='3',fg='red',bg="black",font=("Helvetica",15))
b3=button3.grid(row=cc3,column=dd3)

button4=Label(finestra,text='4',fg='red',bg="black",font=("Helvetica",15))
b4=button4.grid(row=cc4,column=dd4)

button5=Label(finestra,text='5',fg='red',bg="black",font=("Helvetica",15))
b5=button5.grid(row=cc5,column=dd5)

button6=Label(finestra,text='6',fg='red',bg="black",font=("Helvetica",15))
b6=button6.grid(row=cc6,column=dd6)

button7=Label(finestra,text='7',fg='red',bg="black",font=("Helvetica",15))
b7=button7.grid(row=cc7,column=dd7)

button8=Label(finestra,text='8',fg='red',bg="black",font=("Helvetica",15))
b8=button8.grid(row=cc8,column=dd8)
def boh(event):
    print("hello world")
def bohh(event):
    print("hello1")
def bohhh(event):
    print("hello world2")
def bohhhh(event):
    print("hello world3")
    
finestra.bind("<Up>",boh)
finestra.bind("<Down>",bohh)
finestra.bind("<Right>",bohhh)
finestra.bind("<Left>",bohhhh)




finestra.mainloop()   
