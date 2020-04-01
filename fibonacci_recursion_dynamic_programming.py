flag=0
memo=[0,1]
n=int(input('Enter The Num:'))
for i in range(n+1):
    x=-1
    memo.append(x)
def fibo(n):
    global memo
    if memo[n] != -1:
        return memo[n]

    global flag
    flag+=1
    if n<0:
        return None
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        sum = fibo(n-1)+fibo(n-2)
        memo.append(sum)
        return sum




result=fibo(n)
print("The nth fibonacci number is::{}".format(result))
print('count:{}'.format(flag))