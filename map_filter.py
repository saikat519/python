def plus(a):
    return a+5

nums=[1,23,44,56,67]

res1=list(map(plus,nums))
print(res1)
# same as
res2=list(map(lambda a:a+5,nums))
print(res2)


# Filter
def con(a):
    return a%2==0           # if even then returns True otherwise returns False
nums=[12,13,14,15]

a=filter(con,nums)
print(a)
print(list(a))
# same as
b=filter(lambda a:a%2==0,nums)
print(b)
print(list(b))