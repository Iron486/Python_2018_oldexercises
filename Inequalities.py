from sympy import Symbol,Poly,sympify,solve_rational_inequalities,solve_poly_inequality,solve_univariate_inequality,sin,cos,tan,log
from sympy.core.sympify import SympifyError
def isolve():
    ny=function1.is_polynomial()
    nr=function1.is_rational_function()
    if ny==True:
        poly=Poly(I_member,x)
        a=solve_poly_inequality(poly,relation)
        print(a)
    if nr==True:
        try:           
            numer,denom=I_member.as_numer_denom()
            p1=Poly(numer)           
            p2=Poly(denom)
            b=solve_rational_inequalities((p1,p2),relation)
            print(b)
        except NotImplementedError:
            print('Inserisci disequazioni con numeratore e denominatore non trascendentale')

    if nr==False and ny==False:
        try:          
            c=solve_univariate_inequality(function1,x,relational=False)
            print(c)
        except TypeError:
            print('Non è permesso scrivere funzioni composte')
        except NotImplementedError:
            print('Non è permesso inserire funzioni di diversa tipologia')

if __name__=='__main__':
    n=0
    while n >=0:
        try:         
            x=Symbol('x')
            function0=input('Scrivi una funzione --> ')
            function1=sympify(function0)
            I_member= function1.lhs # Extract the function
            relation=function1.rel_op  # Extract the sign
            isolve()
            n+=1
        except SympifyError:
            print('Disequazione non accettabile')
        except SyntaxError:
            print('Disequazione non accettabile')
    
