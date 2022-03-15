import tkinter as tk

def getFrameGrid (parent,tab):
    frame=tk.Frame(parent,bg='white')
    r=c=0
    for riga in tab:
        c=0
        for e in riga:
            lab = tk.Label(frame,text=e,bg='gray80')
            lab.grid(padx=2,pady=2,row=r,column=c)
            c+=1
            r+=1
    return frame

def getTabella(righe,colonne):
    tab = []
    for r in range(righe):
        riga = []
        for c in range(colonne):
            t = str( (r+1,c+1) )
            riga.append(t)
            tab.append(riga)
    return tab

root = tk.Tk()
root['bg'] = 'gray40'

tabella1 = getTabella(4,7)
griglia1 = getFrameGrid(root,tabella1)
griglia1.pack(padx=10,pady=10)

tabella2 = getTabella(9,5)
griglia2 = getFrameGrid(root,tabella2)
griglia2.pack(padx=10,pady=10)

root.mainloop()
