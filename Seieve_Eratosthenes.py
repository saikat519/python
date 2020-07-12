def prime(n):
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True
n=1000002
isPrime=[True for k in range(n)]
isPrime[0]=False
isPrime[1]=False
i=2
while(i*i<=n):
    if prime(i):
        for j in range(i*i,n,i):
            isPrime[j]=False
    i+=1
print(isPrime[6])

'''
Now i have calculated all prime numbers in the big Range 10^6
now i have to just use it
'''