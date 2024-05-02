import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def nhapAB():
    a=int(input())
    b=int(input())
    while a>b:
        print('a không đc lớn hơn b')
        a = int(input('Nhập số a: '))
        a = int(input('Nhập số b: '))
    return a,b
print('nhập vào a,b: ')
a,b=nhapAB()
cnt = 0
for i in range (a,b):
    if isPrime(i):
        cnt+=1
print('số nguyên tố trong khoảng a,b: ')
print(cnt)
