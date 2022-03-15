from tkinter import*
from time import clock
fi=Tk()
fi.geometry('800x800+360+25')
label=Label(fi,text="0.000",font=("Helvetica",30)).pack()
def timer_stop(event):
    stop_time=clock()
    label=Label(fi,text=stop_time,font=("Helvetica",30)).pack()
def timer_start(event):
    start_time=0.0
    start_time=clock()
fi.bind('<Return>',timer_start)
fi.bind('a',timer_stop)
fi.mainloop()



        
     





