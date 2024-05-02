import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def find(n):
    for i in range (1,n+1):
        if isPrime(i):
            j = i+2
            if isPrime(j):
                print(i,' ',j)

find(50)