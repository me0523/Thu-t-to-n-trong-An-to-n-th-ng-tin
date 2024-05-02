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
