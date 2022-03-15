from sympy import Symbol,latex,sympify
from sympy.core.sympify import SympifyError
n=0
while n >=0:
    try:
        x=Symbol('x')
        a=input('Inserisci la funzione da trasformare da formato Python a formato LaTex --> ')
        b=sympify(a)
        print(latex(b))
        n +=1
    except SympifyError:
        print("Inserisci correttamente l'espressione")

