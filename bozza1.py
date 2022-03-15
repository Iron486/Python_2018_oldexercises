from tkinter import *

class AppBase:
    def __init__(self, Genitore):
        self.mioGenitore = Genitore                        # (10)
        self.st1="Seconda Prova di Classe"                 # (12)
        self.st2="Ciao Classe"                             # (14)
        self.quadro1 = Frame(Genitore)                     # (20)
        self.quadro1["background"] = "#FFFF7F"             # (22)
        self.quadro1.pack()                                # (24)
        self.label1 = Label(self.quadro1, text=self.st1,   # (30)
            background="cyan", foreground="blue")
        self.label1.pack(padx=30, pady=10)                 # (32)
        self.puls1 = Button(self.quadro1)                  # (40)
        self.puls1.configure(text = "Cambia",              # (42)
            background = "orange", borderwidth = 1)
        self.puls1.pack(side = LEFT)                       # (44)
        self.puls1.bind("<Button-1>", self.puls1Press1)    # (46)
        self.puls1.bind("<Button-3>", self.puls1Press3)    # (48)
	
        self.puls2 = Button(self.quadro1)                  # (50)
        self.puls2.configure(text = "Uscita",              # (52)
            background = "red", borderwidth = 1)
        self.puls2.pack(side = RIGHT)                      # (54)
        self.puls2.bind("<Button-1>", self.puls2Press1)    # (56)
        self.puls2.bind("<Double-Button-3>",               # (58)
	    self.puls2Press3D)
    def puls1Press1(self, evento):                         # (60)
        if self.puls1["background"] == "orange":
            self.puls1["background"] = "green"
        else:
            self.puls1["background"] = "orange"
    def puls1Press3(self, evento):                         # (70)
        if self.label1["text"] == self.st2:
            self.label1["text"] = self.st1
        else:
            self.label1["text"] = self.st2
    def puls2Press1(self, evento):                         # (80)
        self.mioGenitore.destroy()
    def puls2Press3D(self, evento):                        # (85)
        self.label1["text"] = self.st1
        self.puls1["background"] = "orange"

# Programma Principale
def main():
    finestra = Tk()
    finestra.title("Tk Prova")
    appBase = AppBase(finestra)
    finestra.mainloop()                                    # (90)

main()
