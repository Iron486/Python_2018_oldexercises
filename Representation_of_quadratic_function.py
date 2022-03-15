#Quadratic function calculator
from matplotlib import pyplot as plt
def frange(start,stop,step):
    while start < stop:
        numbers.append(start)
        start= start+step
        # print(numbers)    *if this function is activated, it prints the ordinate couples x,y.
    return numbers
#Representation
def graf1(numbers,y_numbers):   
    for x in numbers :
        y_numbers.append(x**2+2*x+1)
    plt.plot(numbers,y_numbers)
    plt.show()

        
            
        

if __name__=='__main__':
    numbers=[]
    y_numbers=[]
    frange(-100,100,1)
    graf1(numbers,y_numbers)
#Answer to the question in the book:
# It's a nonlinear function,to be exact is a second grade polynomial function.


