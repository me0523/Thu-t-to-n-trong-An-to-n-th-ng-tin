import math
import random


def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def find(n):
    p = [n]
    prime = []
    for i in range (0,n):
        x = random.randint(0,10**5)
        p.append(x)
        if isPrime(x):
            prime.append(x)
    print(p)
    if len(prime) == 0:
        print('không có snt nào')
    else:
        for i in prime:
            print(i)

find(5)