print('Program to find out the probability to have an oral exam ')
number1=int(input('Insert the first page of the book -> '))
number2=int(input('Insert the last page of the book -> '))
list_effective=[]
def function_2(stringa):
    string_separated=list(stringa)
    print(string_separated)
    for number in string_separated:
        numbert=int(number)
        list_effective.append(numbert)
    string=str(sum(list_effective))
    return string
for n in range(number1,number2):
    string=str(n)
    while n > number2:
        print(string)
        function_2(string)

    
        
    
    
        
        
        
