import matplotlib.pyplot as plt
def fibo(n):
    if n==1: 
        print[1]
        return [1]
    if n==2:
        print[1,1]
        return [1,1]
    a=1 
    b=1
    series=[a,b]
    x_numbers=[0] #x_numbers starts with 0 because range function starts also with 0
    y_numbers=[1] #y_numbers starts with 1, because the ratio between first two values is 1
    for i in range(n):
        c=a+b
        series.append(c)
        ratio=c/b
        x_numbers.append(i)
        y_numbers.append(ratio)    
        a=b
        b=c
        plt.title('RAPPORTO TRA DUE CIFRE SUCCESSIVE NELLA SEQUENZA DI FIBONACCI')
        plt.xlabel('Numero di cifre')
        plt.ylabel('Valore assunto dal rapporto')
        plt.plot(x_numbers,y_numbers)  
    plt.show()
    return series,ratio
n=int(input('scrivi numero di volte:' ))
fibo(n)






