
import random


test = random.randint(1,100)
def isPrime(test):
    '''
    Purpose: returns true if its prime and false if it's not
    '''
    cur = True
    for i in range(2,test):
        run = isDivisible(test,i)
        if run == True:
            cur = False
    return cur
        
        
def isDivisible(x,y):
    '''
    Purpose: returns true if y is a factor of x
    '''
    if x % y == 0:
        return True
    else:
        return False
    

result = isPrime(test)
if result == True:
    print(f'Is {test} a prime number: Yes')
else:
    print(f'Is {test} a prime number: No')


#2
def isPerfect(test):
    factor = 0
    for i in range(1,test):
        check = isDivisible(test,i)
        if check == True:
            factor += i
    if factor == test:
        return True
    else:
        return False


yay = isPerfect(test)
if yay == True:
    print(f'{test} is also a perfect number')
else:
    print(f'{test} is not a perfect number')        
        

