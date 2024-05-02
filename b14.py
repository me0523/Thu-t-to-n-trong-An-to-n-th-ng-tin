import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def reverse(n):
    res = 0
    while n>0:
        res = res*10 + n%10
        n = n//10
    return res

def find():
    for i in range (100,1000):
        if isPrime(i):
            rev = reverse(i)
            for j in range (1,int(math.sqrt(rev))+1):
                if(j*j*j == rev):
                    print(i)

find()