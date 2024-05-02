import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def Fn(n):
    if isPrime(n):
        return n
    return 0

def find(l,r):
    sum = 0
    for i in range (l,r+1):
        for j in range (i+1,r+1):
            sum += Fn(i)*Fn(j)
    print(sum)
find(0,5)