from tkinter import *
from random import choice
from time import clock
def grid33():
    def Scramble():
        global x,y,x8,y8,x7,y7,x6,y6,x5,y5,x4,y4,x3,y3,x2,y2,x1,y1
        def Right(event):
            global time1,tempo,repeat,x,y,x8,y8,x7,y7,x6,y6,x5,y5,x4,y4,x3,y3,x2,y2,x1,y1,label8,label7,label6,label5,label4,label3,label2,label1,label
            if repeat==0:
                time1=clock()
            repeat+=1
            if x==x8 and y==y8+1:
                label8.destroy()
                label.destroy()
                y=y-1
                y8=y8+1
                label8=Label(root,text="8",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label8.grid(row=x8,column=y8)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x7 and y==y7+1:
                label7.destroy()
                label.destroy()
                y=y-1
                y7=y7+1
                label7=Label(root,text="7",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label7.grid(row=x7,column=y7)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x6 and y==y6+1:
                label6.destroy()
                label.destroy()
                y=y-1
                y6=y6+1
                label6=Label(root,text="6",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label6.grid(row=x6,column=y6)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x5 and y==y5+1:
                label5.destroy()
                label.destroy()
                y=y-1
                y5=y5+1
                label5=Label(root,text="5",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label5.grid(row=x5,column=y5)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x4 and y==y4+1:
                label4.destroy()
                label.destroy()
                y=y-1
                y4=y4+1
                label4=Label(root,text="4",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label4.grid(row=x4,column=y4)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x3 and y==y3+1:
                label3.destroy()
                label.destroy()
                y=y-1
                y3=y3+1
                label3=Label(root,text="3",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label3.grid(row=x3,column=y3)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x2 and y==y2+1:
                label2.destroy()
                label.destroy()
                y=y-1
                y2=y2+1
                label2=Label(root,text="2",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label2.grid(row=x2,column=y2)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x1 and y==y1+1:
                label1.destroy()
                label.destroy()
                y=y-1
                y1=y1+1
                label1=Label(root,text="1",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label1.grid(row=x1,column=y1)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            if x1==0 and x2==0 and x3==0 and x4==1 and x5==1 and x6==1 and x7==2 and x8==2 and x==2 and y1==0 and y2==1 and y3==2 and y4==0 and y5==1 and y6==2 and y7==0 and y8==1 and y==2:
                time2=clock()
                labelmoves=Label(root,text='                 ',font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                labeltime=Label(root,text='                              ',font=("Helvetica",17),bg='white')
                labeltime.grid(row=3,column=1,columnspan=2,sticky=W+E)
                delta_time=time2-time1
                rounded_time=round(delta_time,2)
                if  rounded_time>= 3600.000:
                    minutis= int(rounded_time//60)
                    secondi=round(rounded_time%60,2)
                    ore= int(minutis//60)
                    minuti= rounded_time%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeltime=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                elif rounded_time >= 60.000:
                    minuti= int(rounded_time//60)
                    secondi= round(rounded_time%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeltime=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                else:
                    labeltime=Label(root,text=rounded_time,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                labelmoves=Label(root,text=repeat,font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                repeat=0
                labelsolved=Label(root,text=" SOLVED !!! ",fg='red2',font=("Helvetica",17),bd=3,relief='solid',bg='white')
                labelsolved.grid(row=3,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
                labelmoves.grid(row=1,column=6)
                labela=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labela.grid(row=2,column=11)
                labelb=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelb.grid(row=1,column=11)
                labelc=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelc.grid(row=1,column=9)
                labeld=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labeld.grid(row=2,column=9)
                labelf=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelf.grid(row=2,column=5)
                time_list.append(rounded_time)     
                move_list.append(repeat)
                lenght_time_list=len(time_list)
                summa=sum(time_list)
                minimo=min(time_list)
                massimo=max(time_list)
                mean=round(summa/lenght_time_list,2)
                label_repeat=Label(root,text=len(move_list),fg='black',bg='white',font=("Helvetica",17))
                label_repeat.grid(row=2,column=5)
                if  massimo>= 3600.000:
                    minutis= int(massimo//60)
                    secondi=round(massimo%60,2)
                    ore= int(minutis//60)
                    minuti= massimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labela=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                elif massimo >= 60.000:
                    minuti= int(massimo//60)
                    secondi= round(massimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labela=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                else:
                    labela=Label(root,text=massimo,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                if  minimo>= 3600.000:
                    minutis= int(minimo//60)
                    secondi=round(minimo%60,2)
                    ore= int(minutis//60)
                    minuti= minimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labelb=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                elif minimo >= 60.000:
                    minuti= int(minimo//60)
                    secondi= round(minimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labelb=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                else:
                    labelb=Label(root,text=minimo,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                if len(time_list)>2:
                    summa2=summa-minimo-massimo
                    lenght_time_list_average=lenght_time_list-2
                    average= round(summa2/lenght_time_list_average,2)
                    if average>= 3600.000:
                        minutis= int(average//60)
                        secondi=round(average%60,2)
                        ore= int(minutis//60)
                        minuti= average%60
                        if minuti <10 and ore >=1:
                            sgonz=str(minuti)
                            minuti='0'+sgonz
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        f=f"{ore}:{minuti}:{secondi}"
                        labelc=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    elif average >= 60.000:
                        minuti= int(average//60)
                        secondi= round(average%60,2)
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        e=f"{minuti}:{secondi}"                  
                        labelc=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    else:
                        labelc=Label(root,text=average,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                if mean>= 3600.000:
                    minutis= int(mean//60)
                    secondi=round(mean%60,2)
                    ore= int(minutis//60)
                    minuti= mean%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeld=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                elif mean >= 60.000:
                    minuti= int(mean//60)
                    secondi= round(mean%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeld=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                else:
                    labeld=Label(root,text=mean,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                root.unbind("<Left>")
                root.unbind("<Right>")
                root.unbind("<Up>")
                root.unbind("<Down>")
        def Left(event):
            global time1,tempo,repeat,x,y,x8,y8,x7,y7,x6,y6,x5,y5,x4,y4,x3,y3,x2,y2,x1,y1,label8,label7,label6,label5,label4,label3,label2,label1,label
            if repeat==0:
                time1=clock()
            repeat+=1
            if x==x8 and y==y8-1:
                label8.destroy()
                label.destroy()
                y=y+1
                y8=y8-1
                label8=Label(root,text="8",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label8.grid(row=x8,column=y8)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x7 and y==y7-1:
                label7.destroy()
                label.destroy()
                y=y+1
                y7=y7-1
                label7=Label(root,text="7",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label7.grid(row=x7,column=y7)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x6 and y==y6-1:
                label6.destroy()
                label.destroy()
                y=y+1
                y6=y6-1
                label6=Label(root,text="6",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label6.grid(row=x6,column=y6)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x5 and y==y5-1:
                label5.destroy()
                label.destroy()
                y=y+1
                y5=y5-1
                label5=Label(root,text="5",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label5.grid(row=x5,column=y5)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x4 and y==y4-1:
                label4.destroy()
                label.destroy()
                y=y+1
                y4=y4-1
                label4=Label(root,text="4",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label4.grid(row=x4,column=y4)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x3 and y==y3-1:
                label3.destroy()
                label.destroy()
                y=y+1
                y3=y3-1
                label3=Label(root,text="3",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label3.grid(row=x3,column=y3)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x2 and y==y2-1:
                label2.destroy()
                label.destroy()
                y=y+1
                y2=y2-1
                label2=Label(root,text="2",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label2.grid(row=x2,column=y2)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x1 and y==y1-1:
                label1.destroy()
                label.destroy()
                y=y+1
                y1=y1-1
                label1=Label(root,text="1",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label1.grid(row=x1,column=y1)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            if x1==0 and x2==0 and x3==0 and x4==1 and x5==1 and x6==1 and x7==2 and x8==2 and x==2 and y1==0 and y2==1 and y3==2 and y4==0 and y5==1 and y6==2 and y7==0 and y8==1 and y==2:
                time2=clock()
                labelmoves=Label(root,text='                      ',font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                labeltime=Label(root,text='                              ',font=("Helvetica",17),bg='white')
                labeltime.grid(row=3,column=1,columnspan=2,sticky=W+E)
                delta_time=time2-time1
                rounded_time=round(delta_time,2)
                if  rounded_time>= 3600.000:
                    minutis= int(rounded_time//60)
                    secondi=round(rounded_time%60,2)
                    ore= int(minutis//60)
                    minuti= rounded_time%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeltime=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                elif rounded_time >= 60.000:
                    minuti= int(rounded_time//60)
                    secondi= round(rounded_time%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeltime=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                else:
                    labeltime=Label(root,text=rounded_time,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                labelmoves=Label(root,text=repeat,font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                repeat=0
                labelsolved=Label(root,text=" SOLVED !!! ",fg='red2',font=("Helvetica",17),bd=3,relief='solid',bg='white')
                labelsolved.grid(row=3,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
                labelmoves.grid(row=1,column=6)
                labela=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labela.grid(row=2,column=11)
                labelb=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelb.grid(row=1,column=11)
                labelc=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelc.grid(row=1,column=9)
                labeld=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labeld.grid(row=2,column=9)
                labelf=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelf.grid(row=2,column=5)
                time_list.append(rounded_time)     
                move_list.append(repeat)
                lenght_time_list=len(time_list)
                summa=sum(time_list)
                minimo=min(time_list)
                massimo=max(time_list)
                mean=round(summa/lenght_time_list,2)
                label_repeat=Label(root,text=len(move_list),fg='black',bg='white',font=("Helvetica",17))
                label_repeat.grid(row=2,column=5)
                if  massimo>= 3600.000:
                    minutis= int(massimo//60)
                    secondi=round(massimo%60,2)
                    ore= int(minutis//60)
                    minuti= massimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labela=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                elif massimo >= 60.000:
                    minuti= int(massimo//60)
                    secondi= round(massimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labela=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                else:
                    labela=Label(root,text=massimo,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                if  minimo>= 3600.000:
                    minutis= int(minimo//60)
                    secondi=round(minimo%60,2)
                    ore= int(minutis//60)
                    minuti= minimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labelb=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                elif minimo >= 60.000:
                    minuti= int(minimo//60)
                    secondi= round(minimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labelb=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                else:
                    labelb=Label(root,text=minimo,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                if len(time_list)>2:
                    summa2=summa-minimo-massimo
                    lenght_time_list_average=lenght_time_list-2
                    average= round(summa2/lenght_time_list_average,2)
                    if average>= 3600.000:
                        minutis= int(average//60)
                        secondi=round(average%60,2)
                        ore= int(minutis//60)
                        minuti= average%60
                        if minuti <10 and ore >=1:
                            sgonz=str(minuti)
                            minuti='0'+sgonz
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        f=f"{ore}:{minuti}:{secondi}"
                        labelc=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    elif average >= 60.000:
                        minuti= int(average//60)
                        secondi= round(average%60,2)
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        e=f"{minuti}:{secondi}"                  
                        labelc=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    else:
                        labelc=Label(root,text=average,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                if mean>= 3600.000:
                    minutis= int(mean//60)
                    secondi=round(mean%60,2)
                    ore= int(minutis//60)
                    minuti= mean%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeld=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                elif mean >= 60.000:
                    minuti= int(mean//60)
                    secondi= round(mean%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeld=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                else:
                    labeld=Label(root,text=mean,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                root.unbind("<Left>")
                root.unbind("<Right>")
                root.unbind("<Up>")
                root.unbind("<Down>")
        def Up(event):
            global time1,tempo,repeat,x,y,x8,y8,x7,y7,x6,y6,x5,y5,x4,y4,x3,y3,x2,y2,x1,y1,label8,label7,label6,label5,label4,label3,label2,label1,label
            if repeat==0:
                time1=clock()
            repeat+=1
            if x==x8-1 and y==y8:
                label8.destroy()
                label.destroy()
                x=x+1
                x8=x8-1
                label8=Label(root,text="8",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label8.grid(row=x8,column=y8)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x7-1 and y==y7:
                label7.destroy()
                label.destroy()
                x=x+1
                x7=x7-1
                label7=Label(root,text="7",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label7.grid(row=x7,column=y7)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x6-1 and y==y6:
                label6.destroy()
                label.destroy()
                x=x+1
                x6=x6-1
                label6=Label(root,text="6",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label6.grid(row=x6,column=y6)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x5-1 and y==y5:
                label5.destroy()
                label.destroy()
                x=x+1
                x5=x5-1
                label5=Label(root,text="5",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label5.grid(row=x5,column=y5)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x4-1 and y==y4:
                label4.destroy()
                label.destroy()
                x=x+1
                x4=x4-1
                label4=Label(root,text="4",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label4.grid(row=x4,column=y4)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x3-1 and y==y3:
                label3.destroy()
                label.destroy()
                x=x+1
                x3=x3-1
                label3=Label(root,text="3",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label3.grid(row=x3,column=y3)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x2-1 and y==y2:
                label2.destroy()
                label.destroy()
                x=x+1
                x2=x2-1
                label2=Label(root,text="2",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label2.grid(row=x2,column=y2)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x1-1 and y==y1:
                label1.destroy()
                label.destroy()
                x=x+1
                x1=x1-1
                label1=Label(root,text="1",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label1.grid(row=x1,column=y1)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            if x1==0 and x2==0 and x3==0 and x4==1 and x5==1 and x6==1 and x7==2 and x8==2 and x==2 and y1==0 and y2==1 and y3==2 and y4==0 and y5==1 and y6==2 and y7==0 and y8==1 and y==2:
                time2=clock()
                labelmoves=Label(root,text='                ',font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                labeltime=Label(root,text='                              ',font=("Helvetica",17),bg='white')
                labeltime.grid(row=3,column=1,columnspan=2,sticky=W+E)
                delta_time=time2-time1
                rounded_time=round(delta_time,2)
                if  rounded_time>= 3600.000:
                    minutis= int(rounded_time//60)
                    secondi=round(rounded_time%60,2)
                    ore= int(minutis//60)
                    minuti= rounded_time%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeltime=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                elif rounded_time >= 60.000:
                    minuti= int(rounded_time//60)
                    secondi= round(rounded_time%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeltime=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                else:
                    labeltime=Label(root,text=rounded_time,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                root.unbind("<Left>",)
                root.unbind("<Right>")
                root.unbind("<Up>")
                root.unbind("<Down>")
                labelmoves=Label(root,text=repeat,font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                repeat=0
                labelsolved=Label(root,text=" SOLVED !!! ",fg='red2',font=("Helvetica",17),bd=3,relief='solid',bg='white')
                labelsolved.grid(row=3,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
                labelmoves.grid(row=1,column=6)
                labela=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labela.grid(row=2,column=11)
                labelb=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelb.grid(row=1,column=11)
                labelc=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelc.grid(row=1,column=9)
                labeld=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labeld.grid(row=2,column=9)
                labelf=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelf.grid(row=2,column=5)
                time_list.append(rounded_time)     
                move_list.append(repeat)
                lenght_time_list=len(time_list)
                summa=sum(time_list)
                minimo=min(time_list)
                massimo=max(time_list)
                mean=round(summa/lenght_time_list,2)
                label_repeat=Label(root,text=len(move_list),fg='black',bg='white',font=("Helvetica",17))
                label_repeat.grid(row=2,column=5)
                if  massimo>= 3600.000:
                    minutis= int(massimo//60)
                    secondi=round(massimo%60,2)
                    ore= int(minutis//60)
                    minuti= massimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labela=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                elif massimo >= 60.000:
                    minuti= int(massimo//60)
                    secondi= round(massimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labela=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                else:
                    labela=Label(root,text=massimo,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                if  minimo>= 3600.000:
                    minutis= int(minimo//60)
                    secondi=round(minimo%60,2)
                    ore= int(minutis//60)
                    minuti= minimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labelb=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                elif minimo >= 60.000:
                    minuti= int(minimo//60)
                    secondi= round(minimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labelb=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                else:
                    labelb=Label(root,text=minimo,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                if len(time_list)>2:
                    summa2=summa-minimo-massimo
                    lenght_time_list_average=lenght_time_list-2
                    average= round(summa2/lenght_time_list_average,2)
                    if average>= 3600.000:
                        minutis= int(average//60)
                        secondi=round(average%60,2)
                        ore= int(minutis//60)
                        minuti= average%60
                        if minuti <10 and ore >=1:
                            sgonz=str(minuti)
                            minuti='0'+sgonz
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        f=f"{ore}:{minuti}:{secondi}"
                        labelc=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    elif average >= 60.000:
                        minuti= int(average//60)
                        secondi= round(average%60,2)
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        e=f"{minuti}:{secondi}"                  
                        labelc=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    else:
                        labelc=Label(root,text=average,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                if mean>= 3600.000:
                    minutis= int(mean//60)
                    secondi=round(mean%60,2)
                    ore= int(minutis//60)
                    minuti= mean%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeld=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                elif mean >= 60.000:
                    minuti= int(mean//60)
                    secondi= round(mean%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeld=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                else:
                    labeld=Label(root,text=mean,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
        def Down(event):
            global time1,tempo,repeat,x,y,x8,y8,x7,y7,x6,y6,x5,y5,x4,y4,x3,y3,x2,y2,x1,y1,label8,label7,label6,label5,label4,label3,label2,label1,label
            if repeat==0:
                time1=clock()
            repeat+=1
            if x==x8+1 and y==y8:
                label8.destroy()
                label.destroy()
                x=x-1
                x8=x8+1
                label8=Label(root,text="8",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label8.grid(row=x8,column=y8)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x7+1 and y==y7:
                label7.destroy()
                label.destroy()
                x=x-1
                x7=x7+1
                label7=Label(root,text="7",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label7.grid(row=x7,column=y7)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x6+1 and y==y6:
                label6.destroy()
                label.destroy()
                x=x-1
                x6=x6+1
                label6=Label(root,text="6",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label6.grid(row=x6,column=y6)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x5+1 and y==y5:
                label5.destroy()
                label.destroy()
                x=x-1
                x5=x5+1
                label5=Label(root,text="5",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label5.grid(row=x5,column=y5)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x4+1 and y==y4:
                label4.destroy()
                label.destroy()
                x=x-1
                x4=x4+1
                label4=Label(root,text="4",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label4.grid(row=x4,column=y4)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x3+1 and y==y3:
                label3.destroy()
                label.destroy()
                x=x-1
                x3=x3+1
                label3=Label(root,text="3",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label3.grid(row=x3,column=y3)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            elif x==x2+1 and y==y2:
                label2.destroy()
                label.destroy()
                x=x-1
                x2=x2+1
                label2=Label(root,text="2",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label2.grid(row=x2,column=y2)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            #return x,y,x8,y8,label8,label9
            elif x==x1+1 and y==y1:
                label1.destroy()
                label.destroy()
                x=x-1
                x1=x1+1
                label1=Label(root,text="1",fg=w,font=("Helvetica",z),bd=border,relief=rel,padx=pad_orizzontal,bg=sfondo)
                label1.grid(row=x1,column=y1)
                label=Label(root,text="  ",fg=w,font=("Helvetica",z),bd=border,relief=rel1,padx=pad_orizzontal,bg=sfondo1)
                label.grid(row=x,column=y)
            if x1==0 and x2==0 and x3==0 and x4==1 and x5==1 and x6==1 and x7==2 and x8==2 and x==2 and y1==0 and y2==1 and y3==2 and y4==0 and y5==1 and y6==2 and y7==0 and y8==1 and y==2:
                time2=clock()
                labelmoves=Label(root,text='              ',font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                labeltime=Label(root,text='                              ',font=("Helvetica",17),bg='white')
                labeltime.grid(row=3,column=1,columnspan=2,sticky=W+E)
                delta_time=time2-time1
                rounded_time=round(delta_time,2)
                if  rounded_time>= 3600.000:
                    minutis= int(rounded_time//60)
                    secondi=round(rounded_time%60,2)
                    ore= int(minutis//60)
                    minuti= rounded_time%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeltime=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                elif rounded_time >= 60.000:
                    minuti= int(rounded_time//60)
                    secondi= round(rounded_time%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeltime=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                else:
                    labeltime=Label(root,text=rounded_time,fg='black',font=("Helvetica",17),bg='white')
                    labeltime.grid(row=1,column=4,columnspan=2,sticky=W+E)
                labelsolved=Label(root,text=" SOLVED !!! ",fg='red2',font=("Helvetica",17),bd=3,relief='solid',bg='white')
                labelsolved.grid(row=3,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
                labelmoves=Label(root,text=repeat,font=("Helvetica",17),bg='white')
                labelmoves.grid(row=1,column=6)
                labela=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labela.grid(row=2,column=11)
                labelb=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelb.grid(row=1,column=11)
                labelc=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelc.grid(row=1,column=9)
                labeld=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labeld.grid(row=2,column=9)
                labelf=Label(root,text='                ',fg='black',font=("Helvetica",17),bg='white')
                labelf.grid(row=2,column=5)
                time_list.append(rounded_time)     
                move_list.append(repeat)
                lenght_time_list=len(time_list)
                summa=sum(time_list)
                minimo=min(time_list)
                massimo=max(time_list)
                mean=round(summa/lenght_time_list,2)
                label_repeat=Label(root,text=len(move_list),fg='black',bg='white',font=("Helvetica",17))
                label_repeat.grid(row=2,column=5)
                if  massimo>= 3600.000:
                    minutis= int(massimo//60)
                    secondi=round(massimo%60,2)
                    ore= int(minutis//60)
                    minuti= massimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labela=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                elif massimo >= 60.000:
                    minuti= int(massimo//60)
                    secondi= round(massimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labela=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                else:
                    labela=Label(root,text=massimo,fg='black',font=("Helvetica",17),bg='white')
                    labela.grid(row=2,column=11)
                if  minimo>= 3600.000:
                    minutis= int(minimo//60)
                    secondi=round(minimo%60,2)
                    ore= int(minutis//60)
                    minuti= minimo%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labelb=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                elif minimo >= 60.000:
                    minuti= int(minimo//60)
                    secondi= round(minimo%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labelb=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                else:
                    labelb=Label(root,text=minimo,fg='black',font=("Helvetica",17),bg='white')
                    labelb.grid(row=1,column=11)
                if len(time_list)>2:
                    summa2=summa-minimo-massimo
                    lenght_time_list_average=lenght_time_list-2
                    average= round(summa2/lenght_time_list_average,2)
                    if average>= 3600.000:
                        minutis= int(average//60)
                        secondi=round(average%60,2)
                        ore= int(minutis//60)
                        minuti= average%60
                        if minuti <10 and ore >=1:
                            sgonz=str(minuti)
                            minuti='0'+sgonz
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        f=f"{ore}:{minuti}:{secondi}"
                        labelc=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    elif average >= 60.000:
                        minuti= int(average//60)
                        secondi= round(average%60,2)
                        if secondi <10 and minuti >= 1:
                            sgondo=str(secondi)
                            secondi='0'+sgondo
                        e=f"{minuti}:{secondi}"                  
                        labelc=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                    else:
                        labelc=Label(root,text=average,fg='black',font=("Helvetica",17),bg='white')
                        labelc.grid(row=1,column=9)
                if mean>= 3600.000:
                    minutis= int(mean//60)
                    secondi=round(mean%60,2)
                    ore= int(minutis//60)
                    minuti= mean%60
                    if minuti <10 and ore >=1:
                        sgonz=str(minuti)
                        minuti='0'+sgonz
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    f=f"{ore}:{minuti}:{secondi}"
                    labeld=Label(root,text=f,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                elif mean >= 60.000:
                    minuti= int(mean//60)
                    secondi= round(mean%60,2)
                    if secondi <10 and minuti >= 1:
                        sgondo=str(secondi)
                        secondi='0'+sgondo
                    e=f"{minuti}:{secondi}"                  
                    labeld=Label(root,text=e,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)
                else:
                    labeld=Label(root,mean,fg='black',font=("Helvetica",17),bg='white')
                    labeld.grid(row=2,column=9)        
                repeat=0          
                root.unbind("<Left>")
                root.unbind("<Right>")
                root.unbind("<Up>")
                root.unbind("<Down>")
        root.bind("<Left>",Left)
        root.bind("<Right>",Right)
        root.bind("<Up>",Up)
        root.bind("<Down>",Down)
        labelsolved=Label(root,text="                                ",fg='red2',font=("Helvetica",17),bg='MediumOrchid1')
        labelsolved.grid(row=3,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
        #algorithm
        k=0
        matrix=[[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5],[x6,y6],[x7,y7],[x8,y8]]#,[x,y]]
        lenght=len(matrix)
        while k<9:
            for n in range(0,lenght-1,1):
                lenght_list.append(n)
            random_lenght1=choice(lenght_list)
            random_lenght2=choice(lenght_list)
            while random_lenght1==random_lenght2:
                random_lenght2=choice(lenght_list)
            mat1=matrix.pop(random_lenght1)
            mat2=matrix.pop(random_lenght2)
            matrix.insert(random_lenght1,mat2)
            matrix.insert(random_lenght2,mat1)
            k+=1
        x1=matrix[0][0]
        y1=matrix[0][1]
        x2=matrix[1][0]
        y2=matrix[1][1]
        x3=matrix[2][0]
        y3=matrix[2][1]
        x4=matrix[3][0]
        y4=matrix[3][1]
        x5=matrix[4][0]
        y5=matrix[4][1]
        x6=matrix[5][0]
        y6=matrix[5][1]
        x7=matrix[6][0]
        y7=matrix[6][1]
        x8=matrix[7][0]
        y8=matrix[7][1]
        #=matrix[8][0]
        #y=matrix[8][1]
        label1=Label(root,text="1",fg=w,bg=sfondo,padx=pad_orizzontal,font=("Helvetica",z),bd=border,relief=rel)
        label1.grid(row=x1,column=y1)
        label2=Label(root,text="2",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label2.grid(row=x2,column=y2)
        label3=Label(root,text="3",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label3.grid(row=x3,column=y3)
        label4=Label(root,text="4",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label4.grid(row=x4,column=y4)
        label5=Label(root,text="5",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label5.grid(row=x5,column=y5)
        label6=Label(root,text="6",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label6.grid(row=x6,column=y6)
        label7=Label(root,text="7",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label7.grid(row=x7,column=y7)
        label8=Label(root,text="8",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
        label8.grid(row=x8,column=y8)
        label=Label(root,text="  ",bg=sfondo1,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel1)
        label.grid(row=x,column=y)
        #return x,y,x8,y8,x7,y7,x6,y6,x5,y5,x4,y4,x3,y3,x2,y2,x1,y1 ,label8,label7,label6,label5,label4,label3,label2,label1,label
    pad_orizzontal=30
    z=90
    border=10
    button_3x3.destroy()
    button_4x4.destroy()
    
    label1.grid(row=x1,column=y1)
    
    label2.grid(row=x2,column=y2)
    
    label3.grid(row=x3,column=y3)
    
    label4.grid(row=x4,column=y4)
    
    label5.grid(row=x5,column=y5)
    
    label6.grid(row=x6,column=y6)
    
    label7.grid(row=x7,column=y7)
    
    label8.grid(row=x8,column=y8)
    
    label.grid(row=x,column=y)
    labelsolved=Label(root,text="        ",font=("Helvetica",17),bg='MediumOrchid1')
    labelsolved.grid(row=4,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
    label_t=Label(root,text=" LAST TIME :",fg='Red2',relief='sunken',bd=2,font=("Helvetica",22))
    label_t.grid(row=0,column=4,columnspan=2,sticky=W+E)
    label_m=Label(root,text="MOVES :",fg='blue',relief='sunken',bd=2,font=("Helvetica",22))
    label_m.grid(row=0,column=6)
    label_st=Label(root,text=" STATISTICS :",fg='sea green',relief='sunken',bd=2,font=("Helvetica",22))
    label_st.grid(row=0,column=8,columnspan=4,sticky=W+E)
    label_st1=Label(root,text=" Average :",fg='red',bg='MediumOrchid1',font=("Helvetica",20))
    label_st1.grid(row=1,column=8)
    label_st2=Label(root,text=" Mean :",fg='red',bg='MediumOrchid1',font=("Helvetica",20))
    label_st2.grid(row=2,column=8)
    label_st3=Label(root,text=" Best solve :",fg='red',bg='MediumOrchid1',font=("Helvetica",20))
    label_st3.grid(row=1,column=10)
    label_st4=Label(root,text=" Worst solve :",fg='red',bg='MediumOrchid1',font=("Helvetica",20))
    label_st4.grid(row=2,column=10)
    label_st5=Label(root,text=" N. of solves :",fg='red',bg='MediumOrchid1',font=("Helvetica",20))
    label_st5.grid(row=2,column=4)
    button_scramble=Button(root,text=' SCRAMBLE',fg='black',font=("Helvetica",24),bd=border,relief='ridge',command=Scramble)
    button_scramble.grid(row=3,column=3,columnspan=3,sticky=W+E)
def grid22():
    def Scramble():
        global a,b,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,label14,label24,label34,label44,label54,label64,label74,label84,label94,label104,label114,label124,label134,label144,label154,label4z
        def Right(event):
            global a,b,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,label14,label24,label34,label44,label54,label64,label74,label84,label94,label104,label114,label124,label134,label144,label154,label4z
            def right_function(x,x8,y,y8,label8,label,num):
                if x==x8 and y==y8+1:
                    label8.destroy()
                    label.destroy()
                    y=y-1
                    y8=y8+1
                    label8=Label(root,text=num,fg=w,font=("Helvetica",zd),bd=border4,relief=rel,padx=pad_orizzontal4,bg=sfondo)
                    label8.grid(row=x8,column=y8)
                    label=Label(root,text="    ",fg=w,font=("Helvetica",zd),bd=border4,relief=rel1,padx=pad_orizzontal4,bg=sfondo1)
                    label.grid(row=x,column=y)
                    return x,x8,y,y8,label8,label,num
            right_function(a,a1,b,b1,label14,label4z,' 1 ')
            right_function(a,a2,b,b2,label24,label4z,' 2 ')
            right_function(a,a3,b,b3,label34,label4z,' 3 ')
            right_function(a,a4,b,b4,label44,label4z,' 4 ')
            right_function(a,a5,b,b5,label54,label4z,' 5 ')
            right_function(a,a6,b,b6,label64,label4z,' 6 ')
            right_function(a,a7,b,b7,label74,label4z,' 7 ')
            right_function(a,a8,b,b8,label84,label4z,' 8 ')
            right_function(a,a9,b,b9,label94,label4z,' 9 ')
            right_function(a,a10,b,b10,label104,label4z,'10')
            right_function(a,a11,b,b11,label114,label4z,'11')
            right_function(a,a12,b,b12,label124,label4z,'12')
            right_function(a,a13,b,b13,label134,label4z,'13')
            right_function(a,a14,b,b14,label144,label4z,'14')
            right_function(a,a15,b,b15,label154,label4z,'15')
            
            #label8.grid(row=x8,column=y8)
            #label.grid(row=x,column=y)
        def Left(event):
            global a,b,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,label14,label24,label34,label44,label54,label64,label74,label84,label94,label104,label114,label124,label134,label144,label154,label4z
            def left_function(x,x8,y,y8,label8,label,num):
                if x==x8 and y==y8-1:
                    label8.destroy()
                    label.destroy()
                    y=y+1
                    y8=y8-1
                    label8=Label(root,text=num,fg=w,font=("Helvetica",zd),bd=border4,relief=rel,padx=pad_orizzontal4,bg=sfondo)
                    label8.grid(row=x8,column=y8)
                    label=Label(root,text="    ",fg=w,font=("Helvetica",zd),bd=border4,relief=rel1,padx=pad_orizzontal4,bg=sfondo1)
                    label.grid(row=x,column=y)
                    return x,x8,y,y8,label8,label,num
            left_function(a,a1,b,b1,label14,label4z,' 1 ')
            left_function(a,a2,b,b2,label24,label4z,' 2 ')
            left_function(a,a3,b,b3,label34,label4z,' 3 ')
            left_function(a,a4,b,b4,label44,label4z,' 4 ')
            left_function(a,a5,b,b5,label54,label4z,' 5 ')
            left_function(a,a6,b,b6,label64,label4z,' 6 ')
            left_function(a,a7,b,b7,label74,label4z,' 7 ')
            left_function(a,a8,b,b8,label84,label4z,' 8 ')
            left_function(a,a9,b,b9,label94,label4z,' 9 ')
            left_function(a,a10,b,b10,label104,label4z,'10')
            left_function(a,a11,b,b11,label114,label4z,'11')
            left_function(a,a12,b,b12,label124,label4z,'12')
            left_function(a,a13,b,b13,label134,label4z,'13')
            left_function(a,a14,b,b14,label144,label4z,'14')
            left_function(a,a15,b,b15,label154,label4z,'15')
            #label8.grid(row=x8,column=y8)
            #label.grid(row=x,column=y)
        def Up(event):
            global a,b,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,label14,label24,label34,label44,label54,label64,label74,label84,label94,label104,label114,label124,label134,label144,label154,label4z
            def up_function(x,x8,y,y8,label8,label,num):
                if x==x8-1 and y==y8:
                    label8.destroy()
                    label.destroy()
                    x=x+1
                    x8=x8-1
                    label8=Label(root,text=num,fg=w,font=("Helvetica",zd),bd=border4,relief=rel,padx=pad_orizzontal4,bg=sfondo)
                    label8.grid(row=x8,column=y8)
                    label=Label(root,text="    ",fg=w,font=("Helvetica",zd),bd=border4,relief=rel1,padx=pad_orizzontal4,bg=sfondo1)
                    label.grid(row=x,column=y)
                    return x,x8,y,y8,label8,label,num
            up_function(a,a1,b,b1,label14,label4z,' 1 ')
            up_function(a,a2,b,b2,label24,label4z,' 2 ')
            up_function(a,a3,b,b3,label34,label4z,' 3 ')
            up_function(a,a4,b,b4,label44,label4z,' 4 ')
            up_function(a,a5,b,b5,label54,label4z,' 5 ')
            up_function(a,a6,b,b6,label64,label4z,' 6 ')
            up_function(a,a7,b,b7,label74,label4z,' 7 ')
            up_function(a,a8,b,b8,label84,label4z,' 8 ')
            up_function(a,a9,b,b9,label94,label4z,' 9 ')
            up_function(a,a10,b,b10,label104,label4z,'10')
            up_function(a,a11,b,b11,label114,label4z,'11')
            up_function(a,a12,b,b12,label124,label4z,'12')
            up_function(a,a13,b,b13,label134,label4z,'13')
            up_function(a,a14,b,b14,label144,label4z,'14')
            up_function(a,a15,b,b15,label154,label4z,'15')
            #label8.grid(row=x8,column=y8)
            #label.grid(row=x,column=y)
        def Down(event):
            #global a,b,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,label14,label24,label34,label44,label54,label64,label74,label84,label94,label104,label114,label124,label134,label144,label154,label4z
            print(a,a15,b,b15)
            def down_function(x,x8,y,y8,label8,label,num):
                if x==x8+1 and y==y8:
                    label8.destroy()
                    label.destroy()
                    x=x-1
                    x8=x8+1
                    label8=Label(root,text=num,fg=w,font=("Helvetica",zd),bd=border4,relief=rel,padx=pad_orizzontal4,bg=sfondo)
                    label8.grid(row=x8,column=y8)
                    label=Label(root,text="    ",fg=w,font=("Helvetica",zd),bd=border4,relief=rel1,padx=pad_orizzontal4,bg=sfondo1)
                    label.grid(row=x,column=y)
                    print('ciaon',x,x8,y,y8)
                    #return x,x8,y,y8,label8,label,num
                    return a,b,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,label14,label24,label34,label44,label54,label64,label74,label84,label94,label104,label114,label124,label134,label144,label154,label4z
            #if x==x8+1 and y==y8:
            down_function(a,a1,b,b1,label14,label4z,' 1 ')
            print(a,a15,b,b15)
            down_function(a,a2,b,b2,label24,label4z,' 2 ')
            print(a,a15,b,b15)
            down_function(a,a3,b,b3,label34,label4z,' 3 ')
            down_function(a,a4,b,b4,label44,label4z,' 4 ')
            down_function(a,a5,b,b5,label54,label4z,' 5 ')
            print(a,a15,b,b15)
            down_function(a,a6,b,b6,label64,label4z,' 6 ')
            down_function(a,a7,b,b7,label74,label4z,' 7 ')
            print(a,a15,b,b15)
            down_function(a,a8,b,b8,label84,label4z,' 8 ')
            down_function(a,a9,b,b9,label94,label4z,' 9 ')
            print(a,a15,b,b15)
            down_function(a,a10,b,b10,label104,label4z,'10')
            down_function(a,a11,b,b11,label114,label4z,'11')
            print(a,a15,b,b15)
            down_function(a,a12,b,b12,label124,label4z,'12')
            down_function(a,a13,b,b13,label134,label4z,'13')
            print(a,a15,b,b15)
            down_function(a,a14,b,b14,label144,label4z,'14')
            down_function(a,a15,b,b15,label154,label4z,'15')
            print(a,a15,b,b15)
            #label8.grid(row=x8,column=y8)
            #label.grid(row=x,column=y)
        root.bind("<Left>",Left)
        root.bind("<Right>",Right)
        root.bind("<Up>",Up)
        root.bind("<Down>",Down)
        labelsolved=Label(root,text="                                ",fg='red2',font=("Helvetica",17),bg='MediumOrchid1')
        labelsolved.grid(row=4,column=0,columnspan=3,rowspan=2,sticky=W+E+S+N)
        #algorithm
        k=0
        matrix=[[a1,b1],[a2,b2],[a3,b3],[a4,b4],[a5,b5],[a6,b6],[a7,b7],[a8,b8],[a9,b9],[a10,b10],[a11,b11],[a12,b12],[a13,b13],[a14,b14],[a15,b15]]#,[x,y]]
        lenght=len(matrix)
        while k<17:
            for n in range(0,lenght-1,1):
                lenght_list.append(n)
            random_lenght1=choice(lenght_list)
            random_lenght2=choice(lenght_list)
            while random_lenght1==random_lenght2:
                random_lenght2=choice(lenght_list)
            mat1=matrix.pop(random_lenght1)
            mat2=matrix.pop(random_lenght2)
            matrix.insert(random_lenght1,mat2)
            matrix.insert(random_lenght2,mat1)
            k+=1
        a1=matrix[0][0]
        b1=matrix[0][1]
        a2=matrix[1][0]
        b2=matrix[1][1]
        a3=matrix[2][0]
        b3=matrix[2][1]
        a4=matrix[3][0]
        b4=matrix[3][1]
        a5=matrix[4][0]
        b5=matrix[4][1]
        a6=matrix[5][0]
        b6=matrix[5][1]
        a7=matrix[6][0]
        b7=matrix[6][1]
        a8=matrix[7][0]
        b8=matrix[7][1]
        a9=matrix[8][0]
        b9=matrix[8][1]
        a10=matrix[9][0]
        b10=matrix[9][1]
        a11=matrix[10][0]
        b11=matrix[10][1]
        a12=matrix[11][0]
        b12=matrix[11][1]
        a13=matrix[12][0]
        b13=matrix[12][1]
        a14=matrix[13][0]
        b14=matrix[13][1]
        a15=matrix[14][0]
        b15=matrix[14][1]
        #=matrix[8][0]
        #y=matrix[8][1]
        label14=Label(root,text=" 1 ",fg=w,bg=sfondo,padx=pad_orizzontal4,font=("Helvetica",zd),bd=border4,relief=rel)
    
        label24=Label(root,text=" 2 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label34=Label(root,text=" 3 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label44=Label(root,text=" 4 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label54=Label(root,text=" 5 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label64=Label(root,text=" 6 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label74=Label(root,text=" 7 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label84=Label(root,text=" 8 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label94=Label(root,text=" 9 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label104=Label(root,text="10",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label114=Label(root,text="11",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label124=Label(root,text="12",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label134=Label(root,text="13",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label144=Label(root,text="14",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label154=Label(root,text="15",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
        
        label4z=Label(root,text="    ",bg=sfondo1,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border,relief=rel1)
        label14.grid(row=a1,column=b1)
    
        label24.grid(row=a2,column=b2)
        
        label34.grid(row=a3,column=b3)
        
        label44.grid(row=a4,column=b4)
        
        label54.grid(row=a5,column=b5)
        
        label64.grid(row=a6,column=b6)
        
        label74.grid(row=a7,column=b7)
        
        label84.grid(row=a8,column=b8)
        
        label94.grid(row=a9,column=b9)
        
        label104.grid(row=a10,column=b10)
        
        label114.grid(row=a11,column=b11)
        
        label124.grid(row=a12,column=b12)
        
        label134.grid(row=a13,column=b13)
        
        label144.grid(row=a14,column=b14)
        
        label154.grid(row=a15,column=b15)
        
        label4z.grid(row=a,column=b)
    border4=8
    button_3x3.destroy()
    button_4x4.destroy()
    pad_orizzontal4=2
    zd=70
    
    label14.grid(row=a1,column=b1)
    
    label24.grid(row=a2,column=b2)
    
    label34.grid(row=a3,column=b3)
    
    label44.grid(row=a4,column=b4)
    
    label54.grid(row=a5,column=b5)
    
    label64.grid(row=a6,column=b6)
    
    label74.grid(row=a7,column=b7)
    
    label84.grid(row=a8,column=b8)
    
    label94.grid(row=a9,column=b9)
    
    label104.grid(row=a10,column=b10)
    
    label114.grid(row=a11,column=b11)
    
    label124.grid(row=a12,column=b12)
    
    label134.grid(row=a13,column=b13)
    
    label144.grid(row=a14,column=b14)
    
    label154.grid(row=a15,column=b15)
    
    label4z.grid(row=a,column=b)
    button_scramble=Button(root,text=' SCRAMBLE',fg='black',font=("Helvetica",24),bd=border4,relief='ridge',command=Scramble)
    button_scramble.grid(row=4,column=4,columnspan=3,sticky=W+E)
    
if __name__=='__main__':
    x1=0
    x2=0
    x3=0
    x4=1
    x5=1
    x6=1
    x7=2
    x8=2
    x=2
    y1=0
    y2=1
    y3=2
    y4=0
    y5=1
    y6=2
    y7=0
    y8=1
    y=2
    
    pad_orizzontal=30
    z=90
    border=10
    time_list=[]
    move_list=[]
    time_of_repetition=0
    time1=0
    w='navy'
    rel='raise'
    rel1='sunken'
    sfondo='cyan'
    sfondo1='gray89'
    repeat=0
    border1=10
    lenght_list=[]
    root=Tk()
    root.title('Gioco del 15')
    root.geometry('800x600+700+30')
    matrix=[]
    root["bg"]="MediumOrchid1"
    
    
    label1=Label(root,text="1",fg=w,bg=sfondo,padx=pad_orizzontal,font=("Helvetica",z),bd=border,relief=rel)
    
    label2=Label(root,text="2",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label3=Label(root,text="3",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label4=Label(root,text="4",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label5=Label(root,text="5",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label6=Label(root,text="6",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label7=Label(root,text="7",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label8=Label(root,text="8",bg=sfondo,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel)
    
    label=Label(root,text="  ",bg=sfondo1,padx=pad_orizzontal,fg=w,font=("Helvetica",z),bd=border,relief=rel1)
    
    a1=0
    a2=0
    a3=0
    a4=0
    a5=1
    a6=1
    a7=1
    a8=1
    a9=2
    a10=2
    a11=2
    a12=2
    a13=3
    a14=3
    a15=3
    a=3
    b1=0
    b2=1
    b3=2
    b4=3
    b5=0
    b6=1
    b7=2
    b8=3
    b9=0
    b10=1
    b11=2
    b12=3
    b13=0
    b14=1
    b15=2 
    b=3
    border4=8
    pad_orizzontal4=2
    zd=70
    label14=Label(root,text=" 1 ",fg=w,bg=sfondo,padx=pad_orizzontal4,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label24=Label(root,text=" 2 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label34=Label(root,text=" 3 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label44=Label(root,text=" 4 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label54=Label(root,text=" 5 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label64=Label(root,text=" 6 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label74=Label(root,text=" 7 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label84=Label(root,text=" 8 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label94=Label(root,text=" 9 ",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label104=Label(root,text="10",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label114=Label(root,text="11",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label124=Label(root,text="12",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label134=Label(root,text="13",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label144=Label(root,text="14",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label154=Label(root,text="15",bg=sfondo,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border4,relief=rel)
    
    label4z=Label(root,text="    ",bg=sfondo1,padx=pad_orizzontal4,fg=w,font=("Helvetica",zd),bd=border,relief=rel1)
    
    button_3x3=Button(root,text=' 3x3 grid',fg='white',bg='blue4',font=("Helvetica",24),bd=border1,relief='sunken',command=grid33)
    button_3x3.pack(fill=X)
    button_4x4=Button(root,text=' 4x4 grid (classic)',fg='white',bg='blue4',font=("Helvetica",24),bd=border1,relief='sunken',command=grid22)
    button_4x4.pack(fill=X)
    root.mainloop()
