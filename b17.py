import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def find(a,b,c,n):
    for i in range (0,n):
        if isPrime(a**2 + b*i +c):
            print(i)
            break

find(4,5,6,7)