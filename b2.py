import math
def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

def soNguyenDuong():
    n = int(input())
    while n<2 or n>10:
        n = int(input('vui lòng nhập vào số nguyên dương có giá trị từ 2-10'))
    return n

print('nhập vào số nguyên dương n có giá trị từ 2-10')
n = soNguyenDuong()
print('các số nguyên tố có n chữ số: ')
for i in range (10**(n-1),10**n):
    if isPrime(i):
        print(i)
