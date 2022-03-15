from sympy.plotting import plot
from sympy.core.sympify import SympifyError
from tkinter import *
from sympy import Symbol,sympify,pprint,solve,exp
import warnings
def past():
    pass
def exit():
    risposta=messagebox.askyesno(title="Exit",message="Do you really want to exit?")
    if risposta:
        root.destroy()
def plot_the_graph():
    label_n1=Label(text='                                                                          ',font=('Helvetica',12),fg='brown')
    label_n1.grid(row=4,column=0)
    label_n=Label(text='                                 ',font=('Helvetica',15))
    label_n.grid(row=4,column=1)
    y=Symbol('y')
    try:
        a=varq.get()
        b=varw.get()
        expr1=var1.get()
        expr3=expr1+'-y'
        sym1=sympify(expr1)
        sym3=sympify(expr3)
        funct='y ='+ str(sym1)
        #s1=solve(sym1,dict=True)
        labelsol=Label(text='                                                                                                    ',font=('Helvetica',15))
        labelsol.grid(row=8,column=0)
        #labelsol=Label(text=s1,font=('Helvetica',15),fg='navy')
        #labelsol.grid(row=8,column=0)
        p1=plot(sym1,title= funct,xlabel='x',ylabel='y',xlim=(a,b))
    except SympifyError:
        label_n=Label(text='Funzione non valida',font=('Helvetica',12),fg='red')
        label_n.grid(row=4,column=0)
    except UserWarning:
        label_n=Label(text='Funzione non valida',font=('Helvetica',12),fg='red')
        label_n.grid(row=4,column=0)
    except TypeError:
        label_n=Label(text='Non si possono inserire funzioni costanti o non esistenti',font=('Helvetica',12),fg='red')
        label_n.grid(row=4,column=0)
def add():
    f2=Entry(textvariable=var2,font=('Helvetica',15))
    f2.grid(row=2,column=1)
    inp_list.append(f2)
    label2=Label(text='Inserisci la seconda funzione da rappresentare in forma implicita',font=('Helvetica',15),fg='white',bg='navy')
    label2.grid(row=2,column=0)
    def plot_the_graph1():
        label_n=Label(text='                                                                          ',font=('Helvetica',15),fg='brown')
        label_n.grid(row=4,column=0) 
        expr1=var1.get()
        expr2=var2.get()
        try:
            a=varq.get()
            b=varw.get()
            label_n=Label(text='                                 ',font=('Helvetica',15))
            label_n.grid(row=4,column=1)
            y=Symbol('y')
            expr3=expr1+'-y'
            expr4=expr2+'-y'
            sym1=sympify(expr1)
            sym2=sympify(expr2)
            sym3=sympify(expr3)
            sym4=sympify(expr4)
            funct='y ='+ str(sym1)
            funct1='y ='+ str(sym2)
            #s1=solve((sym1,sym2),dict=True)
            labelsol=Label(text='                                                                                                    ',font=('Helvetica',15))
            labelsol.grid(row=8,column=0)
            #labelsol=Label(text=s1,font=('Helvetica',15),fg='navy')
            #labelsol.grid(row=8,column=0)
            p1=plot(sym1,sym2,title=funct+','+funct1,xlabel='x',ylabel='y',xlim=(a,b),legend=True,show=False)
            p1[1].line_color='r'
            p1.show()
        except SympifyError:
            label_n=Label(text='Funzioni non valide',font=('Helvetica',12),fg='red')
            label_n.grid(row=4,column=0)
        except ValueError:
            label_n=Label(text='Funzioni non valide',font=('Helvetica',12),fg='red')
            label_n.grid(row=4,column=0)
        except UserWarning:
            label_n=Label(text="Scrivi in modo corretto l'intervallo da considerare",font=('Helvetica',12),fg='red')
            label_n.grid(row=4,column=0)
        except TypeError:
            label_n=Label(text='Non si possono inserire funzioni costanti o non esistenti',font=('Helvetica',12),fg='red')
            label_n.grid(row=4,column=0)
    def add2():
        f3=Entry(textvariable=var3,font=('Helvetica',15))
        f3.grid(row=3,column=1)
        inp_list.append(f3)
        label3=Label(text='Inserisci la terza funzione da rappresentare in forma implicita',font=('Helvetica',15),fg='white',bg='navy')
        label3.grid(row=3,column=0)
        add1=Button(root,text='Si possono inserire al massimo 3 funzioni ',command=past,font=('Helvetica',15),fg='grey',bd='1',relief='solid')
        add1.grid(row=6,column=1)
        def plot_the_graph2():
            label_n=Label(text='                                                                          ',font=('Helvetica',15),fg='brown')
            label_n.grid(row=4,column=0) 
            expr1=var1.get()
            expr2=var2.get()
            expr3=var3.get()
            try:
                a=varq.get()
                b=varw.get()
                label_n=Label(text='                                 ',font=('Helvetica',15))
                label_n.grid(row=4,column=1)
                y=Symbol('y')
                expr4=expr1+'-y'
                expr5=expr2+'-y'                      
                expr6=expr3+'-y'
                sym1=sympify(expr1)
                sym2=sympify(expr2)
                sym3=sympify(expr3)
                sym4=sympify(expr4)
                sym5=sympify(expr5)
                sym6=sympify(expr6)
                funct='y ='+ str(sym1)
                funct1='y ='+ str(sym2)
                func2='y ='+ str(sym3)
                #s1=solve((sym1,sym2,sym3),dict=True)
                labelsol=Label(text='                                                                                                    ',font=('Helvetica',15))
                labelsol.grid(row=8,column=0)
                #labelsol=Label(text=s1,font=('Helvetica',15),fg='navy')
                #labelsol.grid(row=8,column=0)
                p1=plot(sym1,sym2,sym3,title=funct+','+funct1,xlabel='x',ylabel='y',xlim=(a,b),legend=True,show=False)
                p1[1].line_color='r'
                p1[2].line_color='g'
                p1.show()
            except SympifyError:
                label_n=Label(text='Funzioni non valide',font=('Helvetica',12),fg='red')
                label_n.grid(row=4,column=0)
            except ValueError:
                label_n=Label(text='Funzioni non valide',font=('Helvetica',12),fg='red')
                label_n.grid(row=4,column=0)
            except UserWarning:
                label_n=Label(text="Scrivi in modo corretto l'intervallo da considerare",font=('Helvetica',12),fg='red')
                label_n.grid(row=4,column=0)
            except TypeError:
                label_n=Label(text='Non si possono inserire funzioni costanti o non esistenti',font=('Helvetica',12),fg='red')
                label_n.grid(row=4,column=0)
        b=Button(root,text='Prosegui',command=plot_the_graph2,font=('Helvetica',15),bd='2',relief='solid')
        b.grid(row=1,column=2)
    add1=Button(root,text='Aggiungi una funzione',command=add2,font=('Helvetica',15),bd='1',relief='solid')
    add1.grid(row=6,column=1)
    b=Button(root,text='Prosegui',command=plot_the_graph1,font=('Helvetica',15),bd='2',relief='solid')
    b.grid(row=1,column=2)
    
if __name__=='__main__':
    root=Tk()
    root.geometry('1000x1000+150+110')
    root.title('Rappresentazione grafica di funzioni')
    inp_list=[]
    var1=StringVar()
    var2=StringVar()
    var3=StringVar()
    varq=IntVar()
    varw=IntVar()
    x=Symbol('x')
    warnings.filterwarnings("error")
    label_init=Label(text='Rappresentazione di funzioni',font=('Helvetica',35),fg='SteelBlue1',bg='black',bd='3',relief='solid')#relief=flat(default), groove, raised, ridge, solid, or sunken
    label_init.grid(row=0,column=0)
    label1=Label(text='Inserisci la prima funzione da rappresentare in forma implicita',font=('Helvetica',15),fg='white',bg='navy')
    label1.grid(row=1,column=0)
    labellim=Label(text="Inserisci gli estremi dell'intervallo da considerare",font=('Helvetica',15),fg='navy')
    labellim.grid(row=5,column=0)
    f1=Entry(textvariable=var1,font=('Helvetica',15))
    f1.grid(row=1,column=1)
    flimx=Entry(textvariable=varq,font=('Helvetica',15))
    flimx.grid(row=6,column=0)
    flimxx=Entry(textvariable=varw,font=('Helvetica',15))
    flimxx.grid(row=7,column=0)
    varq.set('-10')
    varw.set('10')
    inp_list.append(f1)
    add1=Button(root,text='Aggiungi una funzione',command=add,font=('Helvetica',15),bd='1',relief='solid')
    add1.grid(row=6,column=1)
    b=Button(root,text='Prosegui',command=plot_the_graph,font=('Helvetica',15),bd='2',relief='solid')
    b.grid(row=1,column=2)
    labelzz=Label(text="I valori dell'intervallo devono obbligatoriamente essere inseriti",font=('Helvetica',12),fg='grey')
    labelzz.grid(row=10,column=0)
    barra_menu=Menu(root)
    menu_file=Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label="File",menu=menu_file)
    menu_file.add_command(label="Exit",command=exit)
    root.config(menu=barra_menu)


    
    root.mainloop()
    
    
