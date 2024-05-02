import math
def eratothenes(n):
    prime=[True for i in range(0,n+1)]
    prime[0] = False
    prime[1] = False
    p=2
    for p in range(2,n):
        if (prime[p]==True):
            for i in range(p+p,n+1,p):
                prime[i]=False
    return prime

a = int(input('Nhập vào A: '))
b = int(input('Nhập vào B: '))

prime = eratothenes(b)
res=[]

print("Các số thoả mãn: ")
for i in range(1,int(math.sqrt(b))):
    if i*i<b:
        for j in range(1,int(math.sqrt(b))):
            if (a<=i*i+j*j<=b) and prime[i*i+j*j]:
                res.append(i*i+j*j)
res =[int(i) for i in set(res)]
res.sort()
if len(res)==0:
    print('Không có số nào')
else:
    for i in res:
        print(i,end=' ')