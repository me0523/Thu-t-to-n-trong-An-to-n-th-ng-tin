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
            for j in range (i,n+1):
                if isPrime(j):
                    tong = i+j
                    hieu = int(math.fabs(i-j))
                    if isPrime(tong) and isPrime(hieu):
                        print(i,' ',j)

find(500)