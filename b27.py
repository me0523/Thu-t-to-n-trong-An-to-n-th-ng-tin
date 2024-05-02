import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a,b):
    while b>0:
        tmp = a % b
        a = b
        b = tmp
    return a

def find(a,b):
    for i in range (a,b+1):
        for j in range (a,b+1):
            if(isPrime(gcd(i,j))):
                print(i,' ',j)

find(10,30)