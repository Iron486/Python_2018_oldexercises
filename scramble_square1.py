from time import clock
from tkinter import*
from tkinter import messagebox
from random import sample,choice
# upper layer
a1=1
a2=1
b1=2
b2=2
c1=0
c2=0
d1=0
d2=0
e1=1
e2=1
f1=2
f2=2
# lower layer
g1=1
g2=1
h1=2
h2=2
i1=0
i2=0
l1=0
l2=0
m1=1
m2=1
n1=2
n2=2
scramble_situation_up_right=[a1,b1,c1,d1,e1,f1]
scramble_situation_up_left=[a2,b2,c2,d2,e2,f2]
scramble_situation_down_right=[g1,h1,i1,l1,m1,n1]
scramble_situation_down_left=[g2,h2,i2,l2,m2,n2]
possible_moves_up=[]
possible_moves_down=[]
numb1=1
numb2=2
numb3=3
scramble=[]
# first step: defining moves necessary to scramble as a function of possible moves
# second step: permute pieces involved into the scramble
# third step: insert the two precedent steps in a larger contest ( file "PROGRAMMA_DI_SCRAMBLE")

#FIRST STEP
for n in range(14):
    def scramble_square1_first_combinations(aa,ba,ab,bb,ac,bc,possible):
        if aa==ba and aa==1:
            possible.append('1')
        if aa+ab==2 and ba+bb==2 or (aa==ba and aa==2) :
            possible.append('2')
        if aa+ab+ac==3 and ba+bb+bc==3:
            possible.append('3')
    def scramble_square1_first_combinations_counterclockwise(aa,ba,ab,bb,ac,bc,possible):
        if aa==ba and aa==1:
            possible.append('-1')
        if aa+ab==2 and ba+bb==2 or (aa==ba and aa==2) :
            possible.append('-2')
        if aa+ab+ac==3 and ba+bb+bc==3:
            possible.append('-3')        
    scramble_square1_first_combinations(a1,a2,b1,b2,c1,c2,possible_moves_up)
    scramble_square1_first_combinations_counterclockwise(f1,f2,e1,e2,d1,d2,possible_moves_up)
    scramble_square1_first_combinations_counterclockwise(g1,g2,h1,h2,i1,i2,possible_moves_down)
    scramble_square1_first_combinations(n1,n2,m1,m2,l1,l2,possible_moves_down)
    random_up=choice(possible_moves_up)
    random_down=choice(possible_moves_down)
    random_up_space=' '+random_up+' '
    random_down_space=random_down+' '
    random_up_down='('+random_up_space+random_down_space+')'
    scramble.append(random_up_down)
    print(random_up,random_down)
    #SECOND STEP
    random_clockwise='1'
    random_counterclockwise='-1'
    random_clockwise_2='2'
    random_counterclockwise_2='-2'
    numb_1='1'
    numb_2='2'
    if n==0:
        c1=scramble_situation_up_right.pop(2)
        c2=scramble_situation_up_left.pop(2)
        i1=scramble_situation_down_right.pop(2)
        i2=scramble_situation_down_left.pop(2)
        d1=scramble_situation_up_right.pop(2)
        d2=scramble_situation_up_left.pop(2)
        l1=scramble_situation_down_right.pop(2)
        l2=scramble_situation_down_left.pop(2)
    def p(scramble_situation,scramble_situation_counterclockwise,numb,random,parameter):
        #1 or 2
        def nested(scramble_situation,scramble_situation_counterclockwise,parameter):
            if parameter==2: #2 is the indicator of inversion of the lists
                z=scramble_situation.pop()
                w=scramble_situation_counterclockwise.pop()
                z2=scramble_situation.pop()
                w2=scramble_situation_counterclockwise.pop()
                scramble_situation_counterclockwise.insert(0,z)
                scramble_situation.insert(0,w)
                scramble_situation_counterclockwise.insert(0,z2)
                scramble_situation.insert(0,w2)
            if parameter==1: #1 indicates the non-inversion
                x=scramble_situation.pop(0)
                y=scramble_situation_counterclockwise.pop(0)
                x2=scramble_situation.pop(0)
                y2=scramble_situation_counterclockwise.pop(0)
                scramble_situation_counterclockwise.append(x)
                scramble_situation.append(y)
                scramble_situation_counterclockwise.append(x2)
                scramble_situation.append(y2)
            if '-' in numb:
                print(scramble_situation_counterclockwise,scramble_situation)
                return scramble_situation_counterclockwise,scramble_situation 
            else:
                print(scramble_situation,scramble_situation_counterclockwise)
                return scramble_situation,scramble_situation_counterclockwise
        if (random==numb and (random=='1' or random=='-1')) or (random==numb and (random=='2' and  (scramble_situation[0]==2 and
        scramble_situation_counterclockwise[0]==2 )) or (random=='-2' and (scramble_situation[len(scramble_situation)-1]==2 and
     scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==2))):
            if parameter==2:
                z=scramble_situation.pop()
                w=scramble_situation_counterclockwise.pop()
                scramble_situation_counterclockwise.insert(0,z)
                scramble_situation.insert(0,w)
            if parameter==1:
                x=scramble_situation.pop(0)
                y=scramble_situation_counterclockwise.pop(0)
                scramble_situation_counterclockwise.append(x)
                scramble_situation.append(y)
            if '-' in numb:
                print(scramble_situation_counterclockwise,scramble_situation)
                print('ok')
                return scramble_situation_counterclockwise,scramble_situation 
            else:
                print(scramble_situation,scramble_situation_counterclockwise)
                print('ok')
                return scramble_situation,scramble_situation_counterclockwise
            #1-1/1-1
        elif random==numb and (random=='2' and (scramble_situation[0]==1 and scramble_situation_counterclockwise[0]==1 and
          scramble_situation[1]==1 and scramble_situation_counterclockwise[1]==1 )) or(random=='-2' and (scramble_situation[len(scramble_situation)-1]==1 and
            scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==1 and
        scramble_situation[len(scramble_situation)-2]==1 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-2]==1)):
            nested(scramble_situation,scramble_situation_counterclockwise,parameter)
        #1-2/1-2
        elif random==numb and (random=='3' and(scramble_situation[0]==1 and scramble_situation_counterclockwise[0]==1 and
        scramble_situation[1]==2 and scramble_situation_counterclockwise[1]==2 )) or (random=='-3' and (scramble_situation[len(scramble_situation)-1]==1 and
        scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==1 and
        scramble_situation[len(scramble_situation)-2]==2 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-2]==2)):
            nested(scramble_situation,scramble_situation_counterclockwise,parameter)
            print('1-2/1-2')
        #1-2/2-1
        elif random==numb and (random=='3' and(scramble_situation[0]==1 and scramble_situation_counterclockwise[0]==2
        and scramble_situation[1]==2 and scramble_situation_counterclockwise[1]==1 )) or (random=='-3' and (scramble_situation[len(scramble_situation)-1]==1 and
        scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==2 and
        scramble_situation[len(scramble_situation)-2]==2 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-2]==1)):
            nested(scramble_situation,scramble_situation_counterclockwise,parameter)
            print('1-2/2-1')
        #2-1/1-2
        elif random==numb and (random=='3' and(scramble_situation[0]==2 and scramble_situation_counterclockwise[0]==1 and
        scramble_situation[1]==1 and scramble_situation_counterclockwise[1]==2 )) or(random=='-3' and (scramble_situation[len(scramble_situation)-1]==2 and
        scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==1 and
        scramble_situation[len(scramble_situation)-2]==1 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-2]==2)):
            nested(scramble_situation,scramble_situation_counterclockwise,parameter)
            print('2-1/1-2')
        #2-1/2-1
        elif random==numb and (random=='3' and(scramble_situation[0]==2 and scramble_situation_counterclockwise[0]==2 and
        scramble_situation[1]==1 and scramble_situation_counterclockwise[1]==1 )) or(random=='-3' and (scramble_situation[len(scramble_situation)-1]==2 and
        scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==2 and
        scramble_situation[len(scramble_situation)-2]==1 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-2]==1)):
            nested(scramble_situation,scramble_situation_counterclockwise,parameter)
            print('2-1/2-1')
        # 1-1-1/1-1-1 don't use the function 'nested'!!!
        elif random==numb and (random=='3' and(scramble_situation[0]==1 and scramble_situation_counterclockwise[0]==1 and
        scramble_situation[1]==1 and scramble_situation_counterclockwise[1]==1 and scramble_situation[2]==1
        and scramble_situation_counterclockwise[2]==1)) or(random=='-3' and (scramble_situation[len(scramble_situation)-1]==1 and
        scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-1]==1 and
        scramble_situation[len(scramble_situation)-2]==1 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-2]==1 and
        scramble_situation[len(scramble_situation)-3]==1 and scramble_situation_counterclockwise[len(scramble_situation_counterclockwise)-3]==1)):
            print('1-1-1')
            if parameter==2: #2 is the indicator of inversion of the lists
                z=scramble_situation.pop()
                w=scramble_situation_counterclockwise.pop()
                z2=scramble_situation.pop()
                w2=scramble_situation_counterclockwise.pop()
                z3=scramble_situation.pop()
                w3=scramble_situation_counterclockwise.pop()
                scramble_situation_counterclockwise.insert(0,z)
                scramble_situation.insert(0,w)
                scramble_situation_counterclockwise.insert(0,z2)
                scramble_situation.insert(0,w2)
                scramble_situation_counterclockwise.insert(0,z3)
                scramble_situation.insert(0,w3)
            if parameter==1: #1 indicates the non-inversion
                x=scramble_situation.pop(0)
                y=scramble_situation_counterclockwise.pop(0)
                x2=scramble_situation.pop(0)
                y2=scramble_situation_counterclockwise.pop(0)
                x3=scramble_situation.pop(0)
                y3=scramble_situation_counterclockwise.pop(0)
                scramble_situation_counterclockwise.append(x)
                scramble_situation.append(y)
                scramble_situation_counterclockwise.append(x2)
                scramble_situation.append(y2)
                scramble_situation_counterclockwise.append(x3)
                scramble_situation.append(y3)
            if '-' in numb:
                print(scramble_situation_counterclockwise,scramble_situation)
                return scramble_situation_counterclockwise,scramble_situation 
            else:
                print(scramble_situation,scramble_situation_counterclockwise)
                return scramble_situation,scramble_situation_counterclockwise

    p(scramble_situation_up_right,scramble_situation_up_left,'1',random_up,1)
    p(scramble_situation_down_right,scramble_situation_down_left,'-1',random_down,1)
    p(scramble_situation_up_right,scramble_situation_up_left,'2',random_up,1)
    p(scramble_situation_down_right,scramble_situation_down_left,'-2',random_down,1)
    p(scramble_situation_up_left,scramble_situation_up_right,'-1',random_up,2)
    p(scramble_situation_down_left,scramble_situation_down_right,'1',random_down,2)
    p(scramble_situation_up_left,scramble_situation_up_right,'-2',random_up,2)
    p(scramble_situation_down_left,scramble_situation_down_right,'2',random_down,2)
    p(scramble_situation_up_right,scramble_situation_up_left,'3',random_up,1)
    p(scramble_situation_down_right,scramble_situation_down_left,'-3',random_down,1)
    p(scramble_situation_up_left,scramble_situation_up_right,'-3',random_up,2)
    p(scramble_situation_down_left,scramble_situation_down_right,'3',random_down,2)
    #print(scramble_situation_up_right,scramble_situation_down_right)
    scramble_situation_up_right=scramble_situation_down_right
    scramble_situation_down_right=scramble_situation_up_right
    scramble_situation_down_right.reverse()
    scramble_situation_up_right.reverse()
    #print(scramble_situation_up_right,scramble_situation_down_right)
    #def slash(
    n+=1
    #print(random_up,random_down)
slash='/'
print(slash.join(scramble))
















