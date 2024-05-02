import math

def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def find(a,b):
    for i in range (a,b+1):
        cnt = 0
        for j in range (1,i):
            if(isPrime(j)):
                cnt +=1
        if isPrime(cnt):
            print(i)

find(50,100)