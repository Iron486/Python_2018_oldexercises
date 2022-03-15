from matplotlib import pyplot as plt
from math import degrees,atan2
def exit():
    risposta=messagebox.askyesno(title="Exit",message="Do you really want to exit?")
    if risposta:
        root.destroy()
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
                        plt.plot(x_coordinates,y_other,marker='o')        
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
        
if __name__=='__main__':
    from tkinter import *
    from tkinter import messagebox
    x_coordinates=[]
    y_other=[]
    init_y_coordinates=[]
    x_list=[]
    pendence_graph=[]    
    lenght_list=[]
    len_list=[]
    pendence_list=[]
    y_coordinates=[]                       
    root=Tk()
    root.geometry('700x700+150+200')
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
    barra_menu=Menu(root)
    menu_file=Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label="File",menu=menu_file)
    menu_file.add_command(label="Exit",command=exit)
    root.config(menu=barra_menu)
        
    root.mainloop()
