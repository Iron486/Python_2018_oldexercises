import matplotlib.pyplot as plt
from math import floor,degrees,atan2
from tkinter import *
from tkinter import messagebox
def exit():
    risposta=messagebox.askyesno(title="Exit",message="Do you really want to exit?")
    if risposta:
        root.destroy()
def init():
    def data():
        def data2():
            def data3():
                summa=sum(integral_list)
                effective_value=(summa-(height1*sup_area))/1000
                print(effective_value)
                medium_altitude=(effective_value/sup_area)*1000+height1
                print(medium_altitude)
                title1=var4.get()
                y.insert(0,heigh)
                a=0
                x_truly.insert(0,a)
                plt.title(title1)
                plt.plot(x_truly,y)
                plt.xlabel("Superficie")
                plt.ylabel("Altitudine")
                plt.yticks(y)
                plt.show()
            try:
                labelz=Label(root,text="                                                                                                                         ",fg='red',font=("Helvetica",11))
                labelz.grid(row=2,column=0)
                labelk.destroy()
                global k
                heigh=start_height
                height=(floor(heigh/equidistance))*equidistance #very useful algorithm
                height1=height-(equidistance*k)
                area=var3.get()   
                #integral of ipsographic curve.
                if len(integral_list)==0:
                    piece11= area*height1
                    piece22=(area*(heigh-height))/2
                    tot_piece=piece11+piece22
                    integral_list.append(tot_piece)
                elif len(integral_list)>=1:
                    piece1=area*(height1)
                    piece2=(area*equidistance)/2
                    piece_tot=piece1+piece2
                    integral_list.append(piece_tot)
                x.append(area)
                sup_area=sum(x)
                x_truly.append(sup_area)
                curva_ipsografica=Button(root,text="Traccia il grafico",fg='violet',font=("Helvetica",18),command=data3,borderwidth='3',relief='solid')
                curva_ipsografica.grid(row=1,column=2)
                y.append(height1)
                k+=1
                equidistance_entry.destroy()
            except TclError:
                labelz=Label(root,text=" Non si possono inserire nella casella numeri interi,lettere o caratteri speciali ",fg='red',font=("Helvetica",11))
                labelz.grid(row=2,column=0)
            except NameError:
                labelz=Label(root,text=" Clicca sul pulsante torna indietro ",fg='red',font=("Helvetica",11))
                labelz.grid(row=2,column=0)
        labelz=Label(root,text="                                                    ",fg='red',font=("Helvetica",11))
        labelz.grid(row=2,column=0)
        button1=Button(root,text="Premi per inserire i dati",fg='brown',font=("Helvetica",18),command=data2)
        button1.grid(row=5,column=1)
        try:
            labelk=Label(root,text="                                                                                                                         ",fg='red',font=("Helvetica",11))
            labelk.grid(row=4,column=0)
            superficie_entry2.destroy()
            height_entry.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            var3=DoubleVar()
            equidistance=var1.get()
            start_height=var2.get()
            superficie_entry=Entry(root,textvariable=var3,font=('Helvetica',15))
            superficie_entry.grid(row=1,column=1)
            labels=Label(root,text="Inserisci la superficie della zona tra le due isoipse in km^2",font=('Helvetica',15),fg='white',bg='navy')
            labels.grid(row=1,column=0)
            button.destroy()
        except TclError:
            button_init=Button(root,text="Torna indietro",fg='brown',font=("Helvetica",18),command=init)
            button_init.grid(row=6,column=1)
            button1.destroy
    button_init.destroy()
    button_init2.destroy()
    var1=IntVar()
    var2=IntVar()
    var4=StringVar()
    label=Label(root,text='GRAFICO DI UNA CURVA IPSOGRAFICA',font=('Helvetica',18),fg='navy',bg='white',borderwidth='2',anchor='e',padx=5,pady=3)
    label.grid(row=0,column=1)
    equidistance_entry=Entry(root,textvariable=var1,font=('Helvetica',15))#,justify='center')
    equidistance_entry.grid(row=1,column=1)
    height_entry=Entry(textvariable=var2,font=('Helvetica',15))#,justify='center')
    height_entry.grid(row=2,column=1)
    superficie_entry2=Entry(textvariable=var4,font=('Helvetica',15))
    superficie_entry2.grid(row=3,column=1)
    var1.set("100")
    superficie_entry=Entry(root,textvariable=var1,font=('Helvetica',15))
    superficie_entry.grid(row=1,column=1)
    button=Button(root,text="Premi per inserire i dati",fg='brown',font=("Helvetica",18),command=data)
    button.grid(row=5,column=1)
    label1=Label(root,text="Inserisci l'equidistanza tra le isoipse in metri",font=('Helvetica',15),fg='white',bg='navy')
    label1.grid(row=1,column=0)
    label2=Label(root,text="Inserisci l'altezza iniziale in metri",font=('Helvetica',15),fg='white',bg='navy')
    label2.grid(row=2,column=0)
    label3=Label(root,text="Inserisci un titolo per il grafico",font=('Helvetica',15),fg='white',bg='navy')
    label3.grid(row=3,column=0)
def init2():
    def list_append():
        labeln1=Label(root,text="                                                                                         \n                                           "
                                 "                                                 \n                                                                                     ",fg='grey',font=("Helvetica",11))
        labeln1.grid(row=2,column=0)
        var3=DoubleVar()
        label1.destroy()
        label2.destroy()
        button.destroy()    
        var4=StringVar()
        equidistance_entry.destroy()
        start_height_entry.destroy()
        def list_list():
            label3=Label(root,text="Inserire le distanze \n in millimetri  tra le due isoipse."
                             " \n Se l'isoipsa che viene prima è maggiore della seconda,\n inserire "
                               "un meno nella seconda casella,\n altrimenti inserire un più. \n Se sono alla stessa quota,inserire il simbolo di uguale",fg='green',font=("Helvetica",18))
            label3.grid(row=1,column=0)
            distance_mm_entry=Entry(root,textvariable=var3,font=("Helvetica",18))
            distance_mm_entry.grid(row=1,column=1)
            plus_minus_equal_entry=Entry(root,textvariable=var4,font=("Helvetica",18))
            plus_minus_equal_entry.grid(row=2,column=1)
            def algorithm():
                try:
                    label3=Label(root,text=" Non si possono scrivere distanze uguali a 0 ",fg='grey',font=("Helvetica",11))
                    label3.grid(row=2,column=0)
                    labeln1=Label(root,text="                                                                                                                                             \n                                                 "
                                 "                         "
                                  "                                                                                    \n                                                                                                                                                  ",fg='grey',font=("Helvetica",11))
                    labeln1.grid(row=2,column=0)
                    equidistance=var1.get()
                    start_height=var2.get()
                    distance_mm=var3.get()
                    plus_minus_equal=var4.get()
                    if len(x_list)==0:
                        x_coordinates.append(0)
                    distance=distance_mm*25
                    x_list.append(distance)
                    sum_list_x=sum(x_list)
                    x_coordinates.append(sum_list_x)
                    if '+' == plus_minus_equal:
                        z=equidistance
                    elif '-' == plus_minus_equal:
                        z=-equidistance
                    elif '=' == plus_minus_equal:
                        z=0
                    atan2(z,distance)
                    init_y_coordinates.append(z)
                    lenght=len(pendence_list)+1
                    lenght_list.append(lenght)
                    len_list.append(lenght)
                    tract='tratto '+str(lenght)+' : '
                    pendence_degrees=int(degrees(abs(atan2(z,distance))))
                    pendence=int(abs(z/distance)*100)
                    pendence_list.append(tract+str(pendence_degrees)+'°')
                    sum_list_y=sum(init_y_coordinates)
                    y_coordinates.append(sum_list_y)
                    pendence_graph.append(pendence)
                    def new(): #Draw the graphs
                        try:
                            x_coordinates=[]
                            y_other=[]
                            init_y_coordinates=[]
                            x_list=[]
                            pendence_graph=[]    
                            lenght_list=[]
                            len_list=[]
                            pendence_list=[]
                            y_coordinates=[]
                            button_new.destroy()
                            button1.destroy()
                            distance_mm_entry.destroy()
                            plus_minus_equal_entry.destroy()
                            list_list()
                        except NameError:
                            label3.destroy()
                    def list_append_truly():
                        try:
                            plt.clf()
                            def list_pendence_append_truly():
                                plt.clf()
                                plt.title('Variazione delle pendenze')
                                plt.xlabel('Tratto')
                                plt.ylabel('Pendenza (percentuale)')
                                plt.bar(lenght_list,pendence_graph,align='center')
                                plt.xticks(len_list)
                                print(pendence_list)
                                plt.show()
                            for y in y_coordinates:
                                y=y+start_height
                                y_other.append(y)
                            y_other.insert(0,start_height)
                            plt.title('Profilo Topografico',fontsize=15)
                            plt.xlabel('Distanza (metri)',fontsize=12)
                            plt.ylabel('Quota (metri)',fontsize=12)
                            plt.plot(x_coordinates,y_other)        
                            button3=Button(root,text="Grafico della variazione delle pendenze",fg='brown',font=("Helvetica",18),command=list_pendence_append_truly)
                            button3.grid(row=6,column=1)
                            plt.show()
                        except ValueError:
                            label_error33=Label(root,text="Per calcolare nuovamente il grafico,\n riavviare il programma e reinserire i dati",fg='grey',font=("Helvetica",18))
                            label_error33.grid(row=3,column=0)
                    #button_new=Button(root,text="Traccia nuovo profilo",fg='brown',font=("Helvetica",18),command=new)
                    #button_new.grid(row=5,column=1)         
                    button1=Button(root,text="Premi per ottenere il grafico",fg='brown',font=("Helvetica",18),command=list_append_truly)
                    button1.grid(row=4,column=1)
                except TclError:
                    label3=Label(root,text=" Non si possono scrivere all'interno delle caselle con scrittura '0.0', numeri interi,lettere \n o caratteri speciali "
                                 "e non si possono scrivere all'interno di caselle con scrittura '0' \n numeri decimali,lettere o caratteri speciali",fg='grey',font=("Helvetica",11))
                    label3.grid(row=2,column=0)
                except ZeroDivisionError:
                    label3=Label(root,text=" Non si possono scrivere distanze uguali a 0 ",fg='grey',font=("Helvetica",11))
                    label3.grid(row=2,column=0)
                
                
            button2=Button(root,text="Premi per inserire nuovi dati",fg='brown',font=("Helvetica",18),command=algorithm)
            button2.grid(row=3,column=1)
        list_list()
    button_init.destroy()
    button_init2.destroy()
    var1=IntVar()
    var2=DoubleVar()
    equidistance_entry=Entry(root,textvariable=var1,font=("Helvetica",18))
    equidistance_entry.grid(row=1,column=1)
    start_height_entry=Entry(root,textvariable=var2,font=("Helvetica",18))
    start_height_entry.grid(row=2,column=1)
    label_init=Label(root,text="PROGRAMMA PER TRACCIARE UN PROFILO TOPOGRAFICO",fg='blue',font=("Helvetica",18),bd='2',relief='solid')#relief=flat, groove, raised, ridge, solid, or sunken
    label_init.grid(row=0,column=1)
    label1=Label(root,text="Inserire l'equidistanza tra le isoipse",fg='green',font=("Helvetica",18))
    label1.grid(row=1,column=0)
    label2=Label(root,text="Inserire l'altezza minima",fg='green',font=("Helvetica",18))
    label2.grid(row=2,column=0)
    button=Button(root,text="Premi per inserire i dati",fg='brown',font=("Helvetica",18),command=list_append)
    button.grid(row=3,column=1)   
root=Tk()
root.title('GRAFICO DI UNA CURVA IPSOGRAFICA')
root.geometry('800x800+700+120')
#1
k=0
y=[]
x=[]
x_truly=[]
y_coordinates=[]
integral_list=[]
#2
x_coordinates=[]
y_other=[]
init_y_coordinates=[]
x_list=[]
pendence_graph=[]    
lenght_list=[]
len_list=[]
pendence_list=[]
y_coordinates=[]

button_init=Button(root,text="Grafico di una curva ipsografica",fg='lime green',bg='RoyalBlue4',font=("Helvetica",30),borderwidth='20',relief='groove',command=init)
button_init.grid(row=0,column=1)
button_init2=Button(root,text="Grafico di un profilo topografico ",fg='dark turquoise',bg='dark violet',font=("Helvetica",30),borderwidth='20',relief='groove',command=init2)
button_init2.grid(row=1,column=1)
barra_menu=Menu(root)
menu_file=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="File",menu=menu_file)
menu_file.add_command(label="Exit",command=exit)
root.config(menu=barra_menu)


root.mainloop()

  
      
