flag=0

def fibo(n):
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
        return sum
n=int(input('Enter a Num:'))
result=fibo(n)
print("The nth fibonacci number is::{}".format(result))
print('count:{}'.format(flag))