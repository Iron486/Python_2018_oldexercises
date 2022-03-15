from tkinter import *
from math import sqrt
from tkinter import messagebox
finestra=Tk()
finestra.geometry('900x700+150+100')
finestra.title('calcolo orizzonte e distanza tra due quote')
def init4():
    ciao2=IntVar()
    ciao3=IntVar()
    ciao4=IntVar()
    init3.destroy()
    init1.destroy()
    Label(finestra,text="INSERISCI L'ALTEZZA DELLE DUE QUOTE IN QUALSIASI UNITA' DI MISURA \n"
          "(PURCHE' SIA LA STESSA IN TUTTI GLI SPAZI)",fg='green',font=("Helvetica",12)).grid(row=0,column=1)
    Label(finestra,text=" Quota 1:",fg='brown').grid(row=1,column=0,sticky=E)
    Label(finestra,text=" Quota 2:",fg='brown').grid(row=2,column=0,sticky=E)
    Label(finestra,text=" Distanza tra le due quote:",fg='brown').grid(row=3,column=0,sticky=E)
    Label(finestra,text=" Pendenza del tratto considerato : \n (che inizia dalla quota più bassa e termina con quella più alta)",fg='brown').grid(row=4,column=0,sticky=E)    
    quota1=Entry(finestra,textvariable=ciao2)
    quota1.grid(row=1,column=1)
    quota2=Entry(finestra,textvariable=ciao3)
    quota2.grid(row=2,column=1)
    dist=Entry(finestra,textvariable=ciao4)
    dist.grid(row=3,column=1)
    Label(finestra,text=" Inserendo dati decimali, il risultato che viene fuori \n è lo stesso di quello che "
          "si ottiene scrivendo l'intero \n del numero decimale inserito, approssimato per difetto",fg='brown',font=("Helvetica",8)).grid(row=8,column=1)
    def calcolo1():
        try:
            val2=ciao2.get()
            val3=ciao3.get()
            val4=ciao4.get()
            dy=abs(val3-val2)
            dx=sqrt((val4)**2-dy**2)
            pen=str(round(abs(100*(dy/dx)),1))
            percen=" %"
            testo1=Label(finestra,text='                      ',fg='red')
            testo1.grid(row=4,column=1)
            testo1=Label(finestra,text=pen+percen,fg='red')
            testo1.grid(row=4,column=1)
            Label(finestra,text="                                                                                                               "
                  ,fg='red',font=("Helvetica",10)).grid(row=7,column=1)
            def cancella():
                testo1.grid_forget()
            z=Button(finestra,text="Cancella",command=cancella,fg="white",bg="black",font=("Helvetica",12)).grid(row=6,column=1) 
        except ZeroDivisionError:
            error=Label(finestra,text="             |Quota1-Quota2|= Distanza, inserisci correttamente i dati               "
                  ,fg='red',font=("Helvetica",10))
            error.grid(row=7,column=1)
            testo1=Label(finestra,text='                      ',fg='red')
            testo1.grid(row=4,column=1)
            if val4==0:
                error.grid_forget()
                Label(finestra,text="La distanza deve essere diversa da 0, inserisci correttamente i dati",fg='red',font=("Helvetica",10)).grid(row=7,column=1)
        except ValueError:
            error=Label(finestra,text="              |Quota1-Quota2|< Distanza, inserisci correttamente i dati              "
                  ,fg='red',font=("Helvetica",10))
            error.grid(row=7,column=1)
            testo1=Label(finestra,text='                      ',fg='red')
            testo1.grid(row=4,column=1)
        except TclError:
            error=Label(finestra,text="  Non è permesso inserire lettere o caratteri speciali al posto di numeri            "
                  ,fg='red',font=("Helvetica",10))
            error.grid(row=7,column=1)
            testo1=Label(finestra,text='                      ',fg='red')
            testo1.grid(row=4,column=1)
    Pulsante2=Button(finestra,text='Calcola',command=calcolo1,fg="white",bg="black",font=("Helvetica",12)).grid(row=5,column=1)     
def init2():
    init1.destroy()
    init3.destroy()
    ciao=IntVar()
    ciao1=IntVar()
    Label(finestra,text="INSERISCI L'ALTEZZA DELLE DUE QUOTE IN METRI",fg='green',font=("Helvetica",15)).grid(row=0,column=1)
    Label(finestra,text=" Quota 1:",fg='brown').grid(row=1,column=0,sticky=E)
    Label(finestra,text=" Quota 2:",fg='brown').grid(row=2,column=0,sticky=E)    
    quota1=Entry(finestra,textvariable=ciao)
    quota1.grid(row=1,column=1)
    quota2=Entry(finestra,textvariable=ciao1)
    quota2.grid(row=2,column=1)
    Label(finestra,text="Distanza tra le due quote:",fg='brown').grid(row=3,column=0,sticky=E)
    Label(finestra,text="Distanza tra la prima quota e l'orizzonte:",fg='brown').grid(row=4,column=0,sticky=E)
    Label(finestra,text="Distanza tra la seconda quota e l'orizzonte:",fg='brown').grid(row=5,column=0,sticky=E)
    Label(finestra,text=" Inserendo dati decimali, il risultato che viene fuori \n è lo stesso di quello che "
          "si ottiene scrivendo l'intero \n del numero decimale inserito, approssimato per difetto",fg='brown',font=("Helvetica",8)).grid(row=9,column=1)
    def calcolo():
        try:
            error=Label(finestra,text="                                                                                                         "
            ,fg='red',font=("Helvetica",10))
            error.grid(row=8,column=1)
            a=ciao.get()
            b=ciao1.get()
            r=6371000
            km=" km"
            dist=int((sqrt((r+a)**2-r**2)+sqrt((r+b)**2-r**2))/1000)
            distanza=str(dist)
            distor1=int((sqrt((r+a)**2-r**2))/1000)
            distanzaorizzonte1=str(distor1)
            distor2=dist-distor1
            distanzaorizzonte2=str(distor2)
            testo1=Label(finestra,text='                    ',fg='red')
            testo1.grid(row=3,column=1)
            testo1=Label(finestra,text=distanza+km,fg='red')
            testo1.grid(row=3,column=1)
            testo2=Label(finestra,text='                    ',fg='red')
            testo2.grid(row=4,column=1)
            testo2=Label(finestra,text=distanzaorizzonte1+km,fg='red')
            testo2.grid(row=4,column=1)
            testo3=Label(finestra,text='                    ',fg='red')
            testo3.grid(row=5,column=1)
            testo3=Label(finestra,text=distanzaorizzonte2+km,fg='red')
            testo3.grid(row=5,column=1)
            def cancella():
                testo1.grid_forget()
                testo2.grid_forget()
                testo3.grid_forget()        
            z=Button(finestra,text="Cancella",command=cancella,fg="white",bg="black",font=("Helvetica",12)).grid(row=7,column=1)
        except TclError:
            error=Label(finestra,text="Non è permesso inserire lettere o caratteri speciali al posto di numeri"
                  ,fg='red',font=("Helvetica",10))
            error.grid(row=8,column=1)           
    def rilievo1():      
        e=Label(finestra,text="Aconcagua=6962 m").grid(row=10+1,column=0,sticky=W)
        f=Label(finestra,text="Everest=8848 m").grid(row=11+1,column=0,sticky=W)
        g=Label(finestra,text="Kilimangiaro=5895 m").grid(row=12+1,column=0,sticky=W)
        h=Label(finestra,text="Kungur=7719 m").grid(row=13+1,column=0,sticky=W)
        i=Label(finestra,text="K2=8611 m").grid(row=14+1,column=0,sticky=W)
        j=Label(finestra,text="M.Denali=6190 m").grid(row=15+1,column=0,sticky=W)
        k=Label(finestra,text="M.Elbrus=5642 m").grid(row=16+1,column=0,sticky=W)
        l=Label(finestra,text="M.Kenya=5199 m").grid(row=17+1,column=0,sticky=W)
    def rilievo2():      
        e=Label(finestra,text="Bernina=3996 m").grid(row=10+1,column=1,sticky=W)
        f=Label(finestra,text="Cervino=4478 m").grid(row=11+1,column=1,sticky=W)
        g=Label(finestra,text="Gran Paradiso= 4061 m").grid(row=12+1,column=1,sticky=W)
        h=Label(finestra,text="Marmolada=3342 m").grid(row=13+1,column=1,sticky=W)
        i=Label(finestra,text="M.Bianco=4810 m").grid(row=14+1,column=1,sticky=W)
        j=Label(finestra,text="M.Etna=3323 m").grid(row=15+1,column=1,sticky=W)
        k=Label(finestra,text="M.Rosa=4609 m").grid(row=16+1,column=1,sticky=W)
        l=Label(finestra,text="Monviso=3842 m").grid(row=17+1,column=1,sticky=W)
    def rilievo3():
        e=Label(finestra,text="Corno Grande=2912 m").grid(row=10+1,column=2,sticky=W)
        f=Label(finestra,text="M.Amaro=2793 m").grid(row=11+1,column=2,sticky=W)
        g=Label(finestra,text="M.Greco= 2285 m").grid(row=12+1,column=2,sticky=W)
        h=Label(finestra,text="M.Morrone=2061 m").grid(row=13+1,column=2,sticky=W)
        i=Label(finestra,text="M.Petroso=2247 m").grid(row=14+1,column=2,sticky=W)
        j=Label(finestra,text="M.Porrara=2137 m").grid(row=15+1,column=2,sticky=W)
        k=Label(finestra,text="M.Sirente=2348 m").grid(row=16+1,column=2,sticky=W)
        l=Label(finestra,text="M.Velino=2487 m").grid(row=17+1,column=2,sticky=W)        
    Pulsante=Button(finestra,text='Calcola',command=calcolo,fg="white",bg="black",font=("Helvetica",12)).grid(row=6,column=1)
    c=Button(finestra,text="Principali rilievi del pianeta",command=rilievo1)
    c.grid(row=10,column=0,sticky=W)
    d=Button(finestra,text="Principali rilievi italiani",command=rilievo2)
    d.grid(row=10,column=1,sticky=W)
    e=Button(finestra,text="Principali rilievi abruzzesi",command=rilievo3)
    e.grid(row=10,column=2,sticky=W)
init1=Button(finestra,text="CALCOLO ORIZZONTE E DISTANZA TRA DUE QUOTE",command=init2,fg="blue",font=("Helvetica",30))
init1.pack(fill=X)
init3=Button(finestra,text="CALCOLO PENDENZA MEDIA TRA DUE QUOTE",command=init4,fg="orange",font=("Helvetica",30))
init3.pack(fill=X)
def uscita():
    risposta=messagebox.askyesno(title="Uscita",message="Vuoi davvero uscire ?")
    if risposta:
        finestra.destroy()
barra_menu=Menu(finestra)
menu_file=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="File",menu=menu_file)
menu_file.add_command(label="Esci",command=uscita)
finestra.config(menu=barra_menu)

finestra.mainloop()



