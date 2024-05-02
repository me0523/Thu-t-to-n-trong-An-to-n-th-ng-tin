import math

def decimalToArr(p,w,n):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    arr = []
    for i in range(0, t):
        arr.append((n >> (w * i)) & (2 ** w - 1))
    arr.reverse()
    return arr

def arrToDecimal(p,w,arr):
    n=0
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    for i in range (0,t):
        n = (n<<w) +arr[i]
    return n

def congchinhsacboi(p,w,arra,arrb):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    e = 0

    arrc = []
    for i in range (0,t):
        arrc.append((arra[i]+arrb[i]+e)&(2**w-1))
        e = ((arra[i]+arrb[i]+e)>>w)&1
    arrc.reverse()
    return e,arrc

def truchinhxacboi(p,w,arra,arrb):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    e = 0
    arrc = []
    for i in range(0, t):
        arrc.append((arra[i] - arrb[i] - e) & (2 ** w - 1))
        e = ((arra[i] - arrb[i] - e) >> w) & 1
    arrc.reverse()
    return e, arrc

def congFp(arra,arrb,p,w):
    e,arrc = congchinhsacboi(p,w,arra,arrb)
    if(e==1) or (arrToDecimal(arrc,w,p)>=p):
        arrp = decimalToArr(p,w,p)
        return truchinhxacboi(p,w,arrc,arrp)
    return e,arrc

a=765432
b=123456
arra = decimalToArr(214783647,8,a)
arrb = decimalToArr(214783647,8,b)
e,arrc,=congFp(arra,arrb,214783647,8)
c = arrToDecimal(214783647,8,arrc)
print(e)
print(arrc)
print(c)