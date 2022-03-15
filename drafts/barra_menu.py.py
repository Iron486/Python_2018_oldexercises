from tkinter import *
#crea la finestra
finestra = Tk()
finestra.geometry('300x300+1100+400')
testo= Label(text="15 puzzle", fg="blue")
testo.pack()
bottone=Button(text="3x3 grid",).pack()

    
barra_menu = Menu(finestra)
menu_file = Menu(barra_menu,tearoff = 0)
barra_menu.add_cascade(label = "File", menu = menu_file)
menu_file.add_command(label="Nuovo")
menu_file.add_command(label="Apri")
menu_file.add_command(label="Salva")
menu_file.add_command(label="Esci")
menu_modifica = Menu(barra_menu,tearoff = 0)
barra_menu.add_cascade(label = "Modifica", menu = menu_modifica)
menu_modifica.add_command(label="Nuovo")
menu_modifica.add_command(label="Apri")
menu_modifica.add_command(label="Salva")
menu_modifica.add_command(label="Esci")
finestra.config(menu=barra_menu)
                       
finestra.mainloop()



                 
