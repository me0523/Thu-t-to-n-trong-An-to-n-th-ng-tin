def gcd(a,b):
    while b>0:
        tmp = a%b
        a = b
        b =tmp
    return a

def find(m,n,d):
    for a in range(m,n+1):
        for b in range (m,n+1):
            if(gcd(a,b)==d):
                print(a,' ', b)

find(50,100,22)