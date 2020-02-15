'''
List Comperihention is nothing but an easier way to solve list operation:::
'''


num=[1,2,3,4,5,55]

my_arr=[]

for i in num:
    my_arr.append(i)

print(my_arr)

# This is same as ::

a=[111,21,33,422,555,66]

arr=[i for i in a]
print(arr)

# Taking array inputs without range::
print('Enter list Elements:')
ab=[int(i) for i in input().split()]
print(ab)
ac=[i*i*i for i in ab]
print(ac)
ar=[12,13,14,16,21,31]
print(ar)
ad=[i for i in ar if i%2==0]
print(ad)