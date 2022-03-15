from time import clock
from tkinter import*
from tkinter import messagebox
from statistics import mean
finestra=Tk()
finestra.geometry('700x700+150+200')
label_init=Label(finestra,text="To have a 3x3x3 timer, click <<3x3x3>>,2x2x2 <<2x2x2>>,\n pyraminx <<pyraminx>>, skewb <<skewb>>, megaminx <<megaminx>>")
label_init.pack()
x=0
av=[]
def tre():
    pulsante2.destroy()
    pulsante4.destroy()
    pulsantes.destroy()
    pulsantep.destroy()
    pulsantem.destroy()
    pulsante3.destroy()
    label_init.destroy()
    Statistics=Label(finestra,text='           History:',fg='blue violet',font=("Helvetica",20))
    Statistics.grid(row=0,column=1,sticky=W)
    from random import choice # Algorithm of scramble
    s=('FRUBLD')
    a=choice(s)
    aa=choice("'2 ") 
    bb=choice("'2 ") 
    cc=choice("'2 ")
    dd=choice("'2 ")
    ee=choice("'2 ")    
    ff=choice("'2 ")
    gg=choice("'2 ")
    hh=choice("'2 ")
    ii=choice("'2 ")
    jj=choice("'2 ")
    kk=choice("'2 ")
    ll=choice("'2 ")
    mm=choice("'2 ")    
    nn=choice("'2 ")
    oo=choice("'2 ")
    pp=choice("'2 ")
    qq=choice("'2 ")
    rr=choice("'2 ")
    tt=choice("'2 ")    
    uu=choice("'2 ")
    u=" "
    aq=choice(s)
    while aq==a:
        aq=choice(s)       
    aw=choice(s)
    while aq==aw:
        aw=choice(s)        
    ae=choice(s)
    while ae==aw:
        ae=choice(s)        
    ar=choice(s)
    while ar==ae:
        ar=choice(s)        
    ad=choice(s)
    while ad==ar:
        ad=choice(s)
    af=choice(s)
    while af==ad:
        af=choice(s)        
    ag=choice(s)
    while af==ag:
        ag=choice(s)        
    aj=choice(s)
    while ag==aj:
        aj=choice(s)       
    ak=choice(s)
    while ak==aj:
        ak=choice(s)        
    al=choice(s)
    while al==ak:
        al=choice(s)       
    az=choice(s)
    while az==al:
        az=choice(s)       
    ax=choice(s)
    while az==ax:
        ax=choice(s)        
    ac=choice(s)
    while ax==ac:
        ac=choice(s)        
    av=choice(s)
    while ac==av:
        av=choice(s)        
    ab=choice(s)
    while av==ab:
        ab=choice(s)        
    an=choice(s)
    while ab==an:
        an=choice(s)        
    am=choice(s)
    while an==am:
        am=choice(s)        
    bq=choice(s)
    while am==bq:
        bq=choice(s)        
    bw=choice(s)
    while bq==bw:
        bw=choice(s)
    label3=Label(finestra,text=a+aa+u+aq+bb+u+aw+cc+u+ae+dd+u+ar+ee+u+ad+ff+u+af+gg+u+ag+hh+u+aj+ii+u+ak+jj+u+al+kk+u+az+ll+u+ax+mm+u
                 +ac+nn+u+av+oo+u+ab+pp+u+an+qq+u+am+rr+u+bq+tt+u+bw+uu,font=("Helvetica",17))
    label3.grid(row=0,column=0)
    label33=Label(finestra,text="Press <Enter key> to start the timer and <space> to stop the timer",fg='green',font=("Helvetica",13))
    label33.grid(row=1,column=0)
    def bohh(event):
        testo_n=Label(finestra,text='                          ',fg='red',font=("Helvetica",32))
        testo_n.grid(row=2,column=0)
        a=clock()
        def bohhh(event):               
            b=clock()
            c=b-a
            d=round(c,3)
            label3.destroy()
            label33.destroy()
            def go(d):
                def DNF():
                    d=10000000000000
                    labeldnf=Label(finestra,text='                               ',fg='red',font=("Helvetica",32))
                    labeldnf.grid(row=2,column=0)
                    labeldnf01=Label(finestra,text='DNF',fg='red',font=("Helvetica",32))
                    labeldnf01.grid(row=2,column=0)
                    labeldnf1=Label(finestra,text='                              ',fg='red',font=("Helvetica",12))
                    labeldnf1.grid(row=1,column=1)
                    labeldnf2=Label(finestra,text='Mean: DNF',fg='red',font=("Helvetica",12))
                    labeldnf2.grid(row=1,column=1)
                    labeldnf3=Label(finestra,text='                              ',fg='red',font=("Helvetica",12))
                    labeldnf3.grid(row=1,column=2)
                    labeldnf4=Label(finestra,text='Worst solve: DNF',fg='red',font=("Helvetica",12))
                    labeldnf4.grid(row=1,column=2)    
                    labello4nnt=Label(finestra,text='                              ',fg='blue',font=("Helvetica",12))
                    labello4nnt.grid(row=x+2,column=1)
                    labello5=Label(finestra,text='DNF',fg='blue',font=("Helvetica",12))
                    labello5.grid(row=x+2,column=1)
                    return d
                labelPenalties=Label(finestra,text='Penalties :',fg='red',font=("Helvetica",12))
                labelPenalties.grid(row=3,column=0)
                pulsanteDNF= Button(finestra,text="DNF",command=DNF,bg='black',fg='white',font=("Helvetica",10))
                pulsanteDNF.grid(row=4,column=0)
                global x
                x+=1 #time
                if d >=100000:
                    DNF()                    
                elif d >= 3600.000:
                    minutis= int(d//60)
                    secondi=round(d%60,3)
                    ore= int(minutis//60)
                    minuti= d%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    testo2=Label(finestra,text=f,fg='red',font=("Helvetica",32))
                    testo2.grid(row=2,column=0)
                    testo5=Label(finestra,text=f,fg='blue',font=("Helvetica",10))
                    testo5.grid(row=x+2,column=1)
                elif d >= 60.000:
                    minuti= int(d//60)
                    secondi= round(d%60,3)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    testo1=Label(finestra,text=e,fg='red',font=("Helvetica",32))
                    testo1.grid(row=2,column=0)
                    testo4=Label(finestra,text=e,fg='blue',font=("Helvetica",10))
                    testo4.grid(row=x+2,column=1)
                else:
                    testo=Label(finestra,text=d,fg='red',font=("Helvetica",32))
                    testo.grid(row=2,column=0)
                    testo3=Label(finestra,text=d,fg='blue',font=("Helvetica",10))
                    testo3.grid(row=x+2,column=1)
                global av
                av.append(d)
                amd2=round(mean(av),3) #mean
                testo_niente=Label(finestra,text='                              ',font=("Helvetica",12))
                testo_niente.grid(row=1,column=1)
                if amd2 >= 3600.000: 
                    minutis1= int(amd2//60)
                    secondi1=round(amd2%60,3)
                    ore1= int(minutis//60)
                    minuti1= amd2%60
                    if minuti1 <10 and ore1 >=1:
                        sgonz1=str(minuti1)
                        minuti1='0'+sgonz1
                    if secondi1 <10 and minuti1 >= 1:
                        sgond1=str(secondi1)
                        secondi1='0'+sgond1
                    i=f"Mean: {ore1}:{minuti1}:{secondi1}"
                    mean2=Label(finestra,text=g,fg='red',font=("Helvetica",12))
                    mean2.grid(row=1,column=1)
                elif amd2 >= 60.000:
                    minuti1= int(amd2//60)
                    secondi1= round(amd2%60,3)
                    if secondi1 <10 and minuti1 >= 1:
                        sgond1=str(secondi1)
                        secondi1='0'+sgond1
                    h=f"Mean: {minuti1}:{secondi1}"
                    mean1=Label(finestra,text=h,fg='red',font=("Helvetica",12))
                    mean1.grid(row=1,column=1)
                else:
                    g=f"Mean: {amd2}"
                    mean100=Label(finestra,text=g,fg='red',font=("Helvetica",12))
                    mean100.grid(row=1,column=1)
                max_num=max(av)
                Max_num=f"Worst solve: {max_num}"
                N=av.index(max_num)
                min_num=min(av)
                Min_num=f"Best solve: {min_num}"
                n=av.index(min_num)
                niente1=Label(finestra,text='                              ',font=("Helvetica",12))
                niente1.grid(row=1,column=2)
                niente2=Label(finestra,text='                              ',font=("Helvetica",12))
                niente2.grid(row=2,column=2)                               
                if max_num >= 3600.000: #max value
                    minutis2= int(max_num//60)
                    secondi2=round(max_num%60,3)
                    ore2= int(minutis//60)
                    minuti2= max_num%60
                    if minuti2 <10 and ore2 >=1:
                        sgonz2=str(minuti2)
                        minuti2='0'+sgonz2
                    if secondi2 <10 and minuti2 >= 1:
                        sgond=str(secondi2)
                        secondi2='0'+sgond
                    j=f"Worst solve: {ore2}:{minuti2}:{secondi2}"
                    Worst1=Label(finestra,text=j,fg='red',font=("Helvetica",12))
                    Worst1.grid(row=1,column=2)
                elif max_num >= 60.000:
                    minuti2= int(max_num//60)
                    secondi2= round(max_num%60,3)
                    if secondi2 <10 and minuti2 >= 1:
                        sgond=str(secondi2)
                        secondi2='0'+sgond
                    k=f"Worst solve: {minuti2}:{secondi2}"
                    Worst2=Label(finestra,text=k,fg='red',font=("Helvetica",12))
                    Worst2.grid(row=1,column=2)
                else:
                    l=f"Worst solve: {max_num}"
                    Worst3=Label(finestra,text=l,fg='red',font=("Helvetica",12))
                    Worst3.grid(row=1,column=2)
                if min_num >= 3600.000: #minimal value
                    minutis3= int(min_num//60)
                    secondi3=round(min_num%60,3)
                    ore3= int(minutis//60)
                    minuti3= min_num%60
                    if minuti3 <10 and ore3 >=1:
                        sgonz3=str(minuti3)
                        minuti3='0'+sgonz3
                    if secondi3 <10 and minuti3 >= 1:
                        sgond2=str(secondi3)
                        secondi3='0'+sgond2
                    m=f"Best solve: {ore3}:{minuti3}:{secondi3}"
                    Best=Label(finestra,text=m,fg='red',font=("Helvetica",12))
                    Best.grid(row=2,column=2)
                elif min_num >= 60.000:
                    minuti3= int(min_num//60)
                    secondi3= round(min_num%60,3)
                    if secondi3 <10 and minuti3 >= 1:
                        sgond2=str(secondi3)
                        secondi3='0'+sgond2
                    n=f"Best solve: {minuti3}:{secondi3}"
                    Best=Label(finestra,text=n,fg='red',font=("Helvetica",12))
                    Best.grid(row=2,column=2)
                else:
                    o=f"Best solve: {min_num}"
                    Best=Label(finestra,text=o,fg='red',font=("Helvetica",12))
                    Best.grid(row=2,column=2)
                niente3=Label(finestra,text='                              ',font=("Helvetica",12))
                niente3.grid(row=2,column=1)
                if x<=2:               
                    labello3=Label(finestra,text='Average: X.XXX',fg='red',font=("Helvetica",12))
                    labello3.grid(row=2,column=1)
                if x>2: 
                    av.remove(max(av))
                    av.remove(min(av))
                    amd3=round(mean(av),3) #average
                    if amd3 >= 3600.000:
                        minutis4= int(amd3//60)
                        secondi4=round(amd3%60,3)
                        ore4= int(minutis//60)
                        minuti4= amd3%60
                        if minuti4 <10 and ore4 >=1:
                            sgonz4=str(minuti4)
                            minuti4='0'+sgonz4
                        if secondi4 <10 and minuti4 >= 1:
                            sgond4=str(secondi4)
                            secondi4='0'+sgond4
                        p=f"Average: {ore4}:{minuti4}:{secondi4}"
                        labello=Label(finestra,text=p,fg='red',font=("Helvetica",12))
                        labello.grid(row=2,column=1)
                    elif amd3 >= 60.000:
                        minuti4= int(amd3//60)
                        secondi4= round(amd3%60,3)
                        if secondi4 <10 and minuti4 >= 1:
                            sgond4=str(secondi4)
                            secondi4='0'+sgond4
                        q=f"Average: {minuti4}:{secondi4}"
                        labello1=Label(finestra,text=q,fg='red',font=("Helvetica",12))
                        labello1.grid(row=2,column=1)
                    else:
                        r=f"Average: {amd3}"
                        labello2=Label(finestra,text=r,fg='red',font=("Helvetica",12))
                        labello2.grid(row=2,column=1)
                    av.insert(N,max_num)
                    av.insert(n,min_num)
            go(d)
            tre()
            return x,av
        finestra.bind("<space>",bohhh)
    finestra.bind("<Return>",bohh)

def due():
    pulsante2.destroy()
    pulsante4.destroy()
    pulsantes.destroy()
    pulsantep.destroy()
    pulsantem.destroy()
    pulsante3.destroy()
    label_init.destroy()
def quattro():
    pulsante2.destroy()
    pulsante4.destroy()
    pulsantes.destroy()
    pulsantep.destroy()
    pulsantem.destroy()
    pulsante3.destroy()
    label_init.destroy()
def s():
    pulsante2.destroy()
    pulsantes.destroy()
    pulsante4.destroy()
    pulsantep.destroy()
    pulsantem.destroy()
    pulsante3.destroy()
    label_init.destroy()
def p():
    pulsante2.destroy()
    pulsante4.destroy()
    pulsantes.destroy()
    pulsantep.destroy()
    pulsantem.destroy()
    pulsante3.destroy()
    label_init.destroy()
def m():
    pulsante2.destroy()
    pulsante4.destroy()
    pulsantes.destroy()
    pulsantep.destroy()
    pulsantem.destroy()
    pulsante3.destroy()
    label_init.destroy()
pulsante3=Button(finestra,text="3x3x3",command=tre,bg='white',font=("Helvetica",20))
pulsante3.pack(fill=X)
pulsante2=Button(finestra,text="2x2x2",command=due,bg='gray95',font=("Helvetica",20))
pulsante2.pack(fill=X)
pulsante4=Button(finestra,text="4x4x4",command=quattro,bg='gray90',font=("Helvetica",20))
pulsante4.pack(fill=X)
pulsantes=Button(finestra,text="skewb",command=s,bg='gray85',font=("Helvetica",20))
pulsantes.pack(fill=X)
pulsantep=Button(finestra,text="pyraminx",command=p,bg='gray80',font=("Helvetica",20))
pulsantep.pack(fill=X)
pulsantem=Button(finestra,text="megaminx",command=m,bg='gray75',font=("Helvetica",20))
pulsantem.pack(fill=X)
def uscita():
    risposta=messagebox.askyesno(title="Exit",message="Do you really want to exit?")
    if risposta:
        finestra.destroy()
barra_menu=Menu(finestra)
menu_file=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="File",menu=menu_file)
menu_file.add_command(label="Exit",command=uscita)
finestra.config(menu=barra_menu)
finestra.mainloop()

                

