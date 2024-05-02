import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def find(n):
    for i in range(0,n):
        for j in range(0,i):
            if isPrime(j) ==True:
                if(i%j==0 and i%pow(j,2)==0):
                    print(i)

find(20)