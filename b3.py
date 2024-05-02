import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def soNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('vui lòng nhập vào số nguyên dương n = '))
    return n

print('Nhập vào số nguyên dương n: ')
n = soNguyenDuong()
k,q,p,s=0,0,0,0
for i in range (1,n+1):
    if n%i==0:
        s+=1
        p+=i
        if isPrime(i):
            k+=1
            q+=i
print('N+p+s-q-k = ')
print(n+p+s-q-k)
