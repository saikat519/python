def fun(n, isprime):
    i = 2
    primes = []
    while (i * i <= n):
        for j in range(i * i, n, i):
            isprime[j] = True
        i += 1
    for i in range(2, n):
        if isprime[i] == False:
            primes.append(i)
    return primes


try:
    q = int(input())
    for i in range(q):
        k = int(input())
        n = 800090
        isPrime = [False for i in range(n)]
        isPrime[0] = True
        isPrime[1] = True
        t = fun(n, isPrime)
        print(t[k - 1])
except:
    pass