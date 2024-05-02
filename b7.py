import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def daoChuSo(n):
    res = 0
    while n>0:
        res = res*10 + n%10
        n = n // 10
    return res

def emirp(n):
    dao = daoChuSo(n)
    if n==dao:
        return False
    if isPrime(n) and isPrime(dao):
        return True
    return False

def findEmirp(n):
    for i in range (1,n+1):
        if emirp(i):
            print(i)

findEmirp(300)