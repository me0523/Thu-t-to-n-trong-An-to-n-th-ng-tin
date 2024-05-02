def isQprime(n):
    cnt = 2
    for i in range (2,n):
        if n%i==0:
            cnt += 1;
    return cnt == 4

def soNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('vui lòng nhập vào số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = soNguyenDuong()
empty = True
for i in range (2,n+1):
    if isQprime(i):
        empty = False
        print(i, end=' ')

if empty:
    print('không có số nào')