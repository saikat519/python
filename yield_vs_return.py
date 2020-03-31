# if we want to use yield then we have to use loop to fetch yield values


def generetor_fun():
    yield 1
    yield 55
    yield 3
print('example : 1')
for i in generetor_fun():
    print(i)
'''
  yield  come back exactly there it has broken last time, after going where the function called
  see this program carefully
  output and yield
'''
# Another example::

def fun(a,b):
    yield a*b
    yield a**b
print('example : 2')
for i in fun(2,3):
    print(i)

'''
we can not print the return value like :
print(fun(1,2))
it will not work properly because yield and return are not same
'''
print('example : 3')
def fuck():
    yield 2
                    #it will not work properly
print(fuck())


# it will work if we use return
print('example : 4')
def work():
    return 2
print(work())

print('example : 5')

def gen_func(n):
    for i in n:
        yield i*i

nums=[11,2,3,5]
arr=[]
arr=gen_func(nums)

for i in arr:
    print(i)



